import pandas as pd
import re

def tokenize_amharic(text):
    """Enhanced tokenization for Amharic and mixed-language text."""
    text = re.sub(r'[^\u1200-\u137F\s0-9a-zA-Z]', ' ', text)  # Remove special characters
    return [token.strip() for token in text.split() if token.strip()]

def tag_prices_and_phone(tokens):
    """Tag prices and phone numbers in tokens."""
    labeled_tokens = []
    in_price_context = False

    for token in tokens:
        if token == "ዋጋ፦":
            in_price_context = True
            labeled_tokens.append((token, "O"))
            continue
        
        # Check for phone numbers
        if re.match(r'^09\d{8}$', token):
            labeled_tokens.append((token, "B-PHONE"))
            in_price_context = False
        # Check for prices
        elif in_price_context and re.match(r'^\d+', token):
            labeled_tokens.append((token, "B-PRICE"))
            in_price_context = False
        else:
            labeled_tokens.append((token, "O"))
            in_price_context = False

    return labeled_tokens

def tag_locations(tokens):
    """Detect location-related entities based on keywords and context."""
    location_keywords = {"መገናኛ", "ፒያሳ", "አደባባይ", "ቢሮ", "ፎቅ", "ሱቅ"}
    labeled_tokens = []

    for i, token in enumerate(tokens):
        if token in location_keywords or re.match(r'^\d+ኛ$', token):  # e.g., 1ኛ
            label = "B-LOC" if i == 0 or labeled_tokens[-1][1] != "B-LOC" else "I-LOC"
            labeled_tokens.append((token, label))
        elif re.match(r'^S\d+$', token):  # e.g., S05, S06
            labeled_tokens.append((token, "B-LOC"))
        else:
            labeled_tokens.append((token, "O"))

    return labeled_tokens

def tag_products(tokens):
    """Ensure consistent tagging for product-related entities."""
    labeled_tokens = []
    product_keywords = {"High", "Quality", "Door", "Seal", "Strip", "Stopper"}

    for i, token in enumerate(tokens):
        if token in product_keywords:
            label = "B-PRODUCT" if i == 0 or labeled_tokens[-1][1] != "B-PRODUCT" else "I-PRODUCT"
            labeled_tokens.append((token, label))
        else:
            labeled_tokens.append((token, "O"))

    return labeled_tokens

def process_message(message):
    """Process a single message and tag entities."""
    tokens = tokenize_amharic(message)
    price_tags = tag_prices_and_phone(tokens)
    location_tags = tag_locations(tokens)
    product_tags = tag_products(tokens)

    final_tags = []
    for (token, price_tag), (_, loc_tag), (_, prod_tag) in zip(price_tags, location_tags, product_tags):
        if price_tag != "O":
            final_tags.append((token, price_tag))
        elif loc_tag != "O":
            final_tags.append((token, loc_tag))
        elif prod_tag != "O":
            final_tags.append((token, prod_tag))
        else:
            final_tags.append((token, "O"))

    return final_tags

def convert_to_conll(messages, output_file):
    """
    Convert messages to CoNLL format with refined NER labels.
    
    Args:
        messages (list): List of messages to process.
        output_file (str): File path to save the CoNLL output.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for message in messages:
                tagged_tokens = process_message(message)
                for token, tag in tagged_tokens:
                    f.write(f"{token}\t{tag}\n")
                f.write("\n")  # Blank line between messages
        print(f"CoNLL data successfully saved to {output_file}")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Example usage
processed_data = pd.read_csv('data/processed_telegram_data.csv')  # Replace with your data
messages = processed_data['cleaned_text'].tolist()
output_path = "refined_telegram_ner.conll"
convert_to_conll(messages, output_path)

# Display a sample of the output
print("\nSample CoNLL format output:")
with open(output_path, 'r', encoding='utf-8') as f:
    print(f.read(500))  # Display the first 500 characters for brevity
