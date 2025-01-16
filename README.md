
# **EthioMart Telegram NER**

## **Overview**
EthioMart aims to revolutionize the Ethiopian e-commerce ecosystem by creating a centralized platform for Telegram-based e-commerce activities. This project focuses on fine-tuning large language models (LLMs) to perform **Named Entity Recognition (NER)** on Amharic text data extracted from Telegram channels. The extracted entities will populate EthioMart's centralized database, making it easier for users to explore products, prices, and locations in one unified platform.

---

## **Business Need**
Telegram is a popular platform for e-commerce in Ethiopia, with numerous independent channels operating in isolation. Customers and vendors face challenges due to the lack of a unified system for product discovery and transaction management. EthioMart addresses this gap by consolidating real-time data from multiple channels into a single platform, enabling seamless interaction between vendors and customers.

---

## **Key Objectives**
1. **Data Ingestion**: Extract real-time messages, images, and documents from Telegram e-commerce channels.
2. **Preprocessing**: Tokenize, normalize, and handle Amharic-specific linguistic features for text data.
3. **Named Entity Recognition**: Fine-tune LLMs to extract entities such as:
   - Product Names
   - Prices
   - Locations
4. **Model Comparison**: Evaluate and compare the performance of different NER models.
5. **Business Intelligence**: Use extracted entities to enhance the user experience and business insights.

---

## **Folder Structure**
```plaintext
EthioMart_Telegram_NER/
├── .github/
│   └── workflows/          # GitHub Actions workflows for CI/CD
├── data/
│   ├── raw/                # Raw data from Telegram channels
│   └── preprocessed/       # Preprocessed data ready for analysis
├── scripts/                # Python scripts for data ingestion and preprocessing
├── models/                 # Saved models and checkpoints
├── notebooks/              # Jupyter notebooks for experimentation
├── logs/                   # Log files for debugging and tracking
├── .gitignore              # Files and directories to ignore in Git
├── README.md               # Project overview and documentation
├── requirements.txt        # Python dependencies
```

---

## **Technologies Used**
- **Programming Languages**: Python
- **Libraries**:
  - Data Processing: `pandas`, `numpy`
  - NLP: `transformers`, `tokenizers`
  - Machine Learning: `scikit-learn`, `torch`
  - Amharic-specific Tools: `AmharicStemmer`
- **Version Control**: Git, GitHub
- **CI/CD**: GitHub Actions
- **Database**: PostgreSQL (for storing extracted entities)

---

## **Setup Instructions**

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/<your-username>/EthioMart_Telegram_NER.git
cd EthioMart_Telegram_NER
```

### **Step 2: Set Up a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **Step 3: Install Dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### **Step 4: Configure Telegram API**
1. Create a Telegram application on [Telegram's Developer Portal](https://my.telegram.org/apps).
2. Obtain your **API ID** and **API Hash**.
3. Create a `.env` file in the root directory and add:
   ```plaintext
   TELEGRAM_API_ID=your_api_id
   TELEGRAM_API_HASH=your_api_hash
   ```

### **Step 5: Run the Data Ingestion Script**
```bash
python scripts/data_ingestion.py
```

---

## **Key Features**
- **Real-Time Data Collection**: Fetch messages, images, and documents from multiple Telegram channels.
- **Amharic Text Processing**: Preprocess Amharic text, including tokenization and normalization.
- **NER Fine-Tuning**: Train and evaluate models to extract entities from Amharic text.
- **Business Intelligence**: Generate actionable insights for the Ethiopian e-commerce ecosystem.

---

## **Future Enhancements**
- Add support for multilingual NER.
- Deploy a real-time dashboard for monitoring data ingestion and model performance.
- Extend the system to include product recommendations and sentiment analysis.

---

## **Contributing**
We welcome contributions to improve this project! Please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature-name"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---
