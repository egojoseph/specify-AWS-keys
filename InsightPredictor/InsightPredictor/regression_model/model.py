import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Generate synthetic data
X = np.random.rand(100, 1) * 10
y = 3 * X.flatten() + np.random.randn(100) * 2

# Train the model
model = LinearRegression()
model.fit(X, y)

# Predict and evaluate
predictions = model.predict(X)
mse = mean_squared_error(y, predictions)
print(f"Mean Squared Error: {mse:.2f}")

# Save model
joblib.dump(model, "linear_model.pkl")
