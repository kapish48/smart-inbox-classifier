#here we will create 500 fake emails catergorized into Billing technical and returns
import pandas as pd
import random 

#defining the vocabulary 
billing_words = ["invoice", "payment", "charge", "credit card", "receipt", "bill", "subscription"]
tech_words = ["wifi", "internet", "crash", "error", "slow", "bug", "screen", "login", "password"]
return_words = ["refund", "return", "exchange", "damaged", "wrong size", "shipment", "broken item"]

data = []

print ("generating 1000 support tickets")

for _ in range(1000):
    category = random.choice(["Biliing", "Technical", "Returns"])

    templates = [
        "I have issue with my {word}",
        "Please help, my {word} is not working.",
        "I need to discuss the {word}.",
        "Why is the {word} giving me trouble?",
        "Urgent: {word} issue.",
        "Can you check the status of my {word}?"
    ]

    if category == "Billing":
        word = random.choice(billing_words)
    elif category == "Technical":
        word = random.choice(tech_words)
    else: 
        word = random.choice(return_words)
    
   
    text = random.choice(templates).format(word=word)
    
    # Add to our list
    data.append([text, category])

df = pd.DataFrame(data, columns=["text", "category"])
df.to_csv("support_tickets.csv", index=False)
print("✅ 'support_tickets.csv' created successfully!")
print(df.head())

