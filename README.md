# 📧 SmartInbox: AI Support Ticket Classifier

An NLP-powered web application that automatically categorizes messy, unstructured customer support emails into appropriate departments (Billing, Technical, or Returns). 

## 📌 The Business Problem
Customer support teams waste hundreds of hours manually reading and routing emails. This project solves that bottleneck by using Natural Language Processing (NLP) to instantly analyze text and predict the correct category with high confidence.

## 🧠 How It Works (The NLP Pipeline)
1. **Text Vectorization:** Uses `TfidfVectorizer` to convert English text into a mathematical matrix. It downweights common words (like "the" or "is") and extracts high-value keywords (like "wifi" or "invoice").
2. **Classification:** Uses a `MultinomialNB` (Naive Bayes) probabilistic algorithm to calculate the likelihood of the email belonging to a specific department based on those extracted keywords.

## 🛠️ Tech Stack
* **Python 3.9**
* **Scikit-Learn:** `make_pipeline`, `TfidfVectorizer`, `MultinomialNB`
* **Pandas:** Data manipulation and simulated data generation
* **Streamlit:** Interactive web frontend for real-time inference

## 🚀 How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/kapish48/smart-inbox-classifier.git
cd smart-inbox-classifier

**2. Install dependencies**
pip install -r requirements.txt

**3. Generate the data & train the model**
python generate_emails.py
python model.py

**4. Run the Interface**
streamlit run app.py


