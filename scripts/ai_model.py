# Training the Model

# Import necessary libraries
from sklearn.linear_model import LinearRegression

# One-hot encoding for categorical variables
X = pd.get_dummies(X, drop_first=True)

# Splitting the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Importing the Linear Regression model
model = LinearRegression()

# Training the model with the training data
model.fit(X_train, y_train)

# Displaying the model coefficients
print("Model coefficients:", model.coef_)



# Saving the Model

# Assuming you have a GridSearchCV object named 'grid_search'
best_model = grid_search.best_estimator_

# Save the model to a file
import joblib

model_filename = 'route_optimization_model.pkl'
joblib.dump(best_model, model_filename)

print(f'Model saved as {model_filename}')

