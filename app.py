import streamlit as st
import pickle

# 1. Load the Model
with open("nlp_model.pkl", "rb") as f:
    model = pickle.load(f)

# 2. Page Setup
st.title("📧 SmartInbox: AI Ticket Classifier")
st.write("Enter a customer complaint to automatically route it to the right department.")

# 3. User Input
user_text = st.text_area("Customer Email Content:", "I want to return my damaged item.")

# 4. Prediction Logic
if st.button("Classify Ticket"):
    if user_text:
        # Predict
        category = model.predict([user_text])[0]
        
        # Get Probability (Confidence Score)
        probs = model.predict_proba([user_text])[0]
        confidence = max(probs)
        
        # Display
        st.subheader(f"📂 Category: {category}")
        st.progress(confidence)
        st.write(f"Confidence: {confidence:.1%}")
        
        # Actionable Advice
        if category == "Billing":
            st.info("Route to: Finance Department (finance@company.com)")
        elif category == "Technical":
            st.info("Route to: Tech Support (support@company.com)")
        else:
            st.info("Route to: Returns & Logistics (returns@company.com)")
    else:
        st.warning("Please enter some text first.")

# Sidebar
st.sidebar.markdown("### How it works")
st.sidebar.write("This app uses **TF-IDF Vectorization** to convert words into math, and a **Naive Bayes Classifier** to predict the category.")