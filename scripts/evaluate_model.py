import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, confusion_matrix, accuracy_score, f1_score, classification_report

# Step 1: Define your actual values (y_true) and predicted values (y_pred)
y_true = np.array([150, 200, 300, 250, 100])  # Example actual values
y_pred = np.array([155, 195, 295, 240, 90])   # Example predicted values

# Step 2: Calculate regression metrics
mae = mean_absolute_error(y_true, y_pred)
mse = mean_squared_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)
rmse = np.sqrt(mse)

# Print regression metrics
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("R² Score:", r2)

# Step 3: Convert predictions to classes (for binary classification)
mean_value = np.mean(y_true)
y_true_classes = [1 if value >= mean_value else 0 for value in y_true]
y_pred_classes = [1 if value >= mean_value else 0 for value in y_pred]

# Step 4: Calculate confusion matrix and classification metrics
cm = confusion_matrix(y_true_classes, y_pred_classes)
accuracy = accuracy_score(y_true_classes, y_pred_classes)
f1 = f1_score(y_true_classes, y_pred_classes, average='weighted')

# Print classification metrics
print("Confusion Matrix:\n", cm)
print("Accuracy:", accuracy)
print("F1 Score:", f1)

# Step 5: Generate classification report
report = classification_report(y_true_classes, y_pred_classes)
print("Classification Report:\n", report)
