```
# Import necessary libraries
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

# Load your merged dataset
complete_data = pd.read_csv('merged_delivery_data.csv')

# Check columns in complete_data
print("Columns in complete_data:", complete_data.columns)

# Ensure 'Delivery_Time_Window_x' is in the columns
if 'Delivery_Time_Window_x' in complete_data.columns:
    # Encoding categorical feature 'Delivery_Time_Window_x' using OneHotEncoder
    encoder = OneHotEncoder(drop='first', sparse_output=False)
    encoded_time_window = encoder.fit_transform(complete_data[['Delivery_Time_Window_x']])

    # Convert encoded features to DataFrame
    encoded_time_window_df = pd.DataFrame(encoded_time_window, columns=encoder.get_feature_names_out(['Delivery_Time_Window_x']))

    # Drop original categorical column and add the encoded columns
    complete_data = pd.concat([complete_data.drop(columns=['Delivery_Time_Window_x']), encoded_time_window_df], axis=1)

    # Display the data to check encoding
    print(complete_data.head())
else:
    print("'Delivery_Time_Window_x' not found in complete_data.")
  ```
