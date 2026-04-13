# 📩 Spam SMS Detection using Machine Learning

# 1. Import Libraries
import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report


# 2. Load Dataset
df = pd.read_csv("spam.csv", encoding='latin-1')

# Keep only required columns
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

print("Dataset Loaded Successfully!\n")
print(df.head())


# 3. Data Preprocessing
# Convert labels: ham → 0, spam → 1
df['label'] = df['label'].map({'ham': 0, 'spam': 1})


# 4. Train-Test Split
X = df['message']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# 5. Convert Text to Numerical (TF-IDF)
vectorizer = TfidfVectorizer(stop_words='english')

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)


# 6. Train Model (Naive Bayes)
model = MultinomialNB()
model.fit(X_train_vec, y_train)


# 7. Evaluate Model
y_pred = model.predict(X_test_vec)

print("\nModel Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


# 8. Custom Prediction Function
def predict_sms(text):
    text_vec = vectorizer.transform([text])
    result = model.predict(text_vec)

    if result[0] == 1:
        return "Spam "
    else:
        return "Not Spam "


# 9. Test with Custom Input
print("\nTest the model with your own message:")
while True:
    msg = input("\nEnter SMS (or type 'exit' to quit): ")

    if msg.lower() == "exit":
        print("Exiting...")
        break

    print("Prediction:", predict_sms(msg))


# 10. Save Model & Vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("\nModel and Vectorizer saved successfully!")
