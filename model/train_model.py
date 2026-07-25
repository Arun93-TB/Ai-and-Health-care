import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("dataset.csv")

# Features
X = data.drop("Disease", axis=1)

# Target
y = data["Disease"]

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Save Model
joblib.dump(model, "disease_model.pkl")

print("=" * 40)
print("✅ AI Model Trained Successfully")
print("Model saved as disease_model.pkl")
print("=" * 40)