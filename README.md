# 🤖 Machine Learning Projects Portfolio

This repository contains a collection of machine learning projects completed as part of my practical training.  
Each project focuses on solving a real-world problem using appropriate data preprocessing, feature engineering, and model selection techniques.

---

## 📌 Repository Overview

| Project | Problem Type | Approach | Model |
|--------|-------------|----------|------|
| 📩 Spam SMS Detection | Binary Classification (Text) | TF-IDF | Naive Bayes |
| 🎬 Movie Genre Classification | Multi-class NLP | TF-IDF | Logistic Regression |
| 👥 Customer Churn Prediction | Binary Classification | Feature Engineering | Random Forest |

---

## 🧠 What This Repository Demonstrates

- End-to-end ML workflow (data → model → evaluation)
- Handling structured and unstructured data
- Text processing using NLP techniques
- Feature encoding and preprocessing
- Model evaluation using real metrics
- Debugging real-world dataset issues

---

## 📂 Project Details

---

### 📩 Spam SMS Detection

**Goal:** Classify SMS messages as Spam or Ham.

**Pipeline:**
- Text cleaning
- TF-IDF vectorization
- Multinomial Naive Bayes model

**Why this model?**  
Naive Bayes performs well for text classification due to probabilistic word distribution.

**Result:**  
Achieves high accuracy (~96%) on test data.

## ▶️ Example

Input:
"Congratulations! You have won a free lottery ticket. Call now!"

Output:
Spam ❌
Input:
"Hey, are we meeting today?"

Output:
Not Spam ✅

---

### 🎬 Movie Genre Classification

**Goal:** Predict movie genre based on plot description.

**Challenges solved:**
- Non-standard dataset format (`:::` separator)
- Handling noisy and long text
- Feature dimensionality control

**Pipeline:**
- Data parsing & cleaning
- TF-IDF feature extraction
- Logistic Regression model

**Why Logistic Regression?**  
Efficient for high-dimensional sparse data (like TF-IDF vectors).

## ▶️ Example

Input:
"A detective investigates a mysterious murder in a small town."

Output:
Crime / Thriller

---

### 👥 Customer Churn Prediction

**Goal:** Predict whether a customer will leave a bank.

**Key Steps:**
- Removed irrelevant features (ID, Name)
- Encoded categorical variables (Geography, Gender)
- Handled missing values
- Trained Random Forest model

**Why Random Forest?**
- Handles non-linear relationships
- Works well with tabular data
- Robust to overfitting

**Result:**
- Accuracy: ~86%
- Balanced performance across classes

## ▶️ Example

Input:
CreditScore: 600
Geography: France
Gender: Male
Age: 40
Balance: 60000
IsActiveMember: 0

Output:
Churn ❌ (Customer likely to leave)

---

📁 Project Structure

CodSoft-ML-internship/
 ├── SPAM_SMS_DETECTION/
 │    ├── spam_detector.py
 │    ├── spam.csv
 │
 ├── MOVIE_GENRE_CLASSIFICATION/
 │    ├── movie_classification.py
 │    ├── movie_dataset.csv
 │
 ├── CUSTOMER_CHURN_PREDICTION/
 │    ├── churn.py
 │    ├── churn.csv
 │
 └── README.md

 ---

 ## 🧠 Tech Stack

- **Programming Language:** Python 🐍  
- **Libraries:**
  - Pandas
  - NumPy
  - Scikit-learn  
- **Concepts:**
  - Machine Learning
  - Natural Language Processing (NLP)
  - Data Preprocessing
  - Model Evaluation

---

💡Key Learnings

- Real-world data is messy → requires cleaning & debugging
- Model performance depends heavily on preprocessing
- TF-IDF is powerful for text-based problems
- Feature selection improves model stability
- Debugging is a core ML skill, not optional
  


