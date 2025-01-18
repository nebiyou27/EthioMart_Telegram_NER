import pandas as pd
import re
import json
import unicodedata


class TelegramPreprocessor:
    def __init__(self):
        # Common Amharic unicode ranges
        self.amharic_range = re.compile(r'[\u1200-\u137F]+')

    def clean_text(self, text):
        """Clean and normalize text content."""
        if not isinstance(text, str):
            return ""

        # Remove emojis and special characters
        text = self._remove_emojis(text)
        # Normalize unicode characters
        text = unicodedata.normalize('NFKC', text)
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove URLs
        text = re.sub(r'http\S+|www.\S+', '', text)
        return text.strip()

    def _remove_emojis(self, text):
        """Remove emojis and other special characters."""
        emoji_pattern = re.compile(
            "[" "\U0001F600-\U0001F64F" "\U0001F300-\U0001F5FF"
            "\U0001F680-\U0001F6FF" "\U0001F1E0-\U0001F1FF"
            "\U00002702-\U000027B0" "\U000024C2-\U0001F251" "]+",
            flags=re.UNICODE,
        )
        return emoji_pattern.sub('', text)

    def extract_phone_numbers(self, text):
        """Extract phone numbers from text."""
        phone_pattern = re.compile(r'\b\d{10}\b')
        return phone_pattern.findall(text)

    def separate_amharic_english(self, text):
        """Separate Amharic and English text."""
        amharic_text = []
        english_text = []

        for word in text.split():
            if self.amharic_range.search(word):
                amharic_text.append(word)
            elif word.isascii():
                english_text.append(word)

        return {
            'amharic': ' '.join(amharic_text),
            'english': ' '.join(english_text),
        }

    def process_message(self, message):
        """Process a single message."""
        cleaned_text = self.clean_text(message)
        separated_text = self.separate_amharic_english(cleaned_text)
        phone_numbers = self.extract_phone_numbers(cleaned_text)

        return {
            'cleaned_text': cleaned_text,
            'amharic_text': separated_text['amharic'],
            'english_text': separated_text['english'],
            'phone_numbers': phone_numbers,
        }

    def process_dataframe(self, df):
        """Process the entire DataFrame."""
        processed_data = []

        for _, row in df.iterrows():
            processed_message = self.process_message(row['Message'])

            processed_row = {
                'channel_title': row['Channel Title'],
                'channel_username': row['Channel Username'],
                'message_id': row['ID'],
                'timestamp': row['Date'],
                **processed_message,
            }

            processed_data.append(processed_row)

        return pd.DataFrame(processed_data)


def main():
    # Read the CSV file
    df = pd.read_csv('data/telegram_data.csv')

    # Initialize preprocessor
    preprocessor = TelegramPreprocessor()

    # Process the data
    processed_df = preprocessor.process_dataframe(df)

    # Save processed data
    processed_df.to_csv('processed_telegram_data.csv', index=False)

    # Save a sample in JSON format for inspection
    sample = processed_df.head().to_dict(orient='records')
    with open('sample_processed_data.json', 'w', encoding='utf-8') as f:
        json.dump(sample, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
