import json
import pandas as pd
from glob import glob
import os

# Paths
json_dir = "data/json/"
processed_dir = "data/preprocessed/"
merged_file = os.path.join(processed_dir, "merged_data.csv")

# Ensure processed directory exists
os.makedirs(processed_dir, exist_ok=True)

# Load and merge JSON files
def load_and_merge_json(json_dir):
    json_files = glob(os.path.join(json_dir, "*.json"))
    data = []
    for file in json_files:
        with open(file, 'r', encoding='utf-8') as f:
            data.extend(json.load(f))
    return pd.DataFrame(data)

# Process and save merged data
def main():
    print("Loading and merging JSON files...")
    df = load_and_merge_json(json_dir)
    
    # Save merged data to CSV
    print(f"Saving merged data to {merged_file}...")
    df.to_csv(merged_file, index=False)
    print("Done!")

if __name__ == "__main__":
    main()
