import os

def create_project_structure(base_path):
    # Define the folder structure
    folders = [
        "data/raw",
        "data/preprocessed",
        "scripts",
        "models",
        "notebooks",
        "logs"
    ]
    
    files = [
        ".gitignore",
        "README.md",
        "requirements.txt"
    ]
    
    # Create folders
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")
    
    # Create files
    for file in files:
        file_path = os.path.join(base_path, file)
        with open(file_path, "w") as f:
            if file == "README.md":
                f.write("# EthioMart Telegram NER\n\nThis project focuses on fine-tuning LLMs for Amharic Named Entity Recognition (NER) to extract entities such as product names, prices, and locations from Telegram e-commerce channels.")
            if file == ".gitignore":
                f.write("env/\n__pycache__/\n*.pyc\n*.pkl\n*.log\n*.csv\n")
            if file == "requirements.txt":
                f.write("telethon\npandas\nnumpy\nnltk\ntransformers\ntorch\ndatasets\nmatplotlib\nscikit-learn\n")
        print(f"Created file: {file_path}")

if __name__ == "__main__":
    # Define the base path for the project
    base_path = os.getcwd()  # Change this to your desired project directory
    print(f"Creating project structure in: {base_path}")
    create_project_structure(base_path)
