import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
df = pd.read_csv("data/heart.csv")

# Features & target
X = df.drop("target", axis=1)
y = df["target"]

# ✅ SCALE DATA
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# ✅ SAVE BOTH
joblib.dump(model, "app/model/model.pkl")
joblib.dump(scaler, "app/model/scaler.pkl")

print("✅ Model and scaler saved successfully!")