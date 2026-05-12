import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

# ── 1. Load the dataset ──────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "heart.csv")

df = pd.read_csv(csv_path)
print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"\nColumns: {df.columns.tolist()}")
print(f"\nTarget distribution:\n{df['target'].value_counts()}")

# ── 2. Split features and label ──────────────────────────────────────────────
X = df.drop("target", axis=1)
y = df["target"]

# ── 3. Train/test split ──────────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTraining samples : {len(X_train)}")
print(f"Test samples     : {len(X_test)}")

# ── 4. Train the model ───────────────────────────────────────────────────────
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("\nModel trained successfully.")

# ── 5. Evaluate ──────────────────────────────────────────────────────────────
y_pred = model.predict(X_test)
accuracy = model.score(X_test, y_test)
print(f"\nTest Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=["No Disease", "Disease"]))

# ── 6. Save the model ────────────────────────────────────────────────────────
model_path = os.path.join(BASE_DIR, "heart_model.joblib")
joblib.dump(model, model_path)
print(f"\nModel saved → {model_path}")