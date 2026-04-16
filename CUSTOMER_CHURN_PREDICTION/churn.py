#  Customer Churn Prediction

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# 1. Load Dataset
df = pd.read_csv("churn.csv")

print("✅ Dataset Loaded")
print(df.head())
print(df.info())


# 2. Drop unnecessary columns
df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1, inplace=True)


# 3. Encode ONLY categorical columns
le = LabelEncoder()

categorical_cols = ['Geography', 'Gender']

for col in categorical_cols:
    df[col] = le.fit_transform(df[col])


# 4. Handle missing values
df = df.fillna(0)


# 5. Split features & target
X = df.drop('Exited', axis=1)
y = df['Exited']


#  DEBUG CHECK
print("\nAny NaN left?\n", X.isnull().sum())


# 6. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# 7. Train Model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)


# 8. Evaluate
y_pred = model.predict(X_test)

print("\n📊 Accuracy:", accuracy_score(y_test, y_pred))
print("\n📄 Report:\n", classification_report(y_test, y_pred))
