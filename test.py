# Creating the model validation script
from pathlib import Path
import joblib
from sklearn.datasets import load_iris

model_file = Path("models/iris_model.pkl")
assert model_file.exists(), "Train the model before testing"
model = joblib.load(model_file)
X, y = load_iris(return_X_y=True)
accuracy = model.score(X, y)
assert accuracy >= 0.80, f"Accuracy too low: {accuracy:.3f}"
print(f"Model validation passed; dataset accuracy: {accuracy:.3f}")
