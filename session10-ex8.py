import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# Email Spam Dataset 
data = {
    "Word_Frequency": [8, 1, 9, 2, 7, 1, 10, 3],
    "Link_Count": [3, 0, 4, 1, 2, 0, 5, 1],
    "Email_Length": [150, 40, 170, 60, 140, 35, 180, 70],
    "Spam": ["Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No"]
}

df = pd.DataFrame(data)


# Encode Target Labels
df["Spam"] = df["Spam"].map({
    "No": 0,
    "Yes": 1
})


# Features and Target
X = df[["Word_Frequency", "Link_Count", "Email_Length"]]
y = df["Spam"]


# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)


# Train Random Forest Model
rf = RandomForestClassifier(
    n_estimators=50,
    random_state=42
)

rf.fit(X_train, y_train)


# Predictions
y_pred = rf.predict(X_test)


# Model Evaluation
print("RANDOM FOREST EMAIL SPAM CLASSIFIER RESULTS")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))


# Feature Importance
print("\nFEATURE IMPORTANCE")
for feature, importance in zip(X.columns, rf.feature_importances_):
    print(feature, ":", importance)
