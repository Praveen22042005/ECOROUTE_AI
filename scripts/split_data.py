```
# Splitting the dataset into features (X) and target variable (y)
X = complete_data.drop(columns=['Distance'])  # Features
y = complete_data['Distance']  # Target variable

# Importing train_test_split
from sklearn.model_selection import train_test_split

# Splitting the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the shape of the training and testing sets
print(f"Training data shape: {X_train.shape}, Testing data shape: {X_test.shape}")
```
