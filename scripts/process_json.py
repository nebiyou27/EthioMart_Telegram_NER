import json
import pandas as pd
from glob import glob
import os

# Define directory paths
json_dir = "data/json/"
processed_dir = "data/preprocessed/"
merged_file = os.path.join(processed_dir, "merged_data.csv")

# Ensure the processed directory exists
os.makedirs(processed_dir, exist_ok=True)

# Function to load and merge JSON files into a DataFrame
def load_and_merge_json(json_dir):
    """
    Loads all JSON files from the specified directory and merges them into a single DataFrame.
    
    Args:
        json_dir (str): Directory containing the JSON files.
    
    Returns:
        pd.DataFrame: DataFrame containing the merged data from all JSON files.
    """
    # Get list of all JSON files in the directory
    json_files = glob(os.path.join(json_dir, "*.json"))
    data = []
    
    # Iterate over each JSON file and load its content
    for file in json_files:
        with open(file, 'r', encoding='utf-8') as f:
            data.extend(json.load(f))
    
    # Return the merged data as a DataFrame
    return pd.DataFrame(data)

# Main function to execute the script
def main():
    """
    Main function to load, merge, and save JSON data to a CSV file.
    """
    print("Loading and merging JSON files...")
    df = load_and_merge_json(json_dir)
    
    # Save the merged data to a CSV file
    print(f"Saving merged data to {merged_file}...")
    df.to_csv(merged_file, index=False)
    print("Done!")

# Entry point of the script
if __name__ == "__main__":
    main()
