import pandas as pd

# Example data for prediction with the correct features
data = {
    'Origin': [0],
    'Destination': [1],
    'Traffic_Delay': [0.5],
    'Vehicle_ID': [0],
    'Vehicle_1_Capacity': [1000],
    'Vehicle_2_Capacity': [800],
    'Vehicle_3_Capacity': [600],
    'Vehicle_4_Capacity': [400],
    'Vehicle_5_Capacity': [200],
    'Load': [300],
    'Fuel_Consumption': [0.2],
    'Latitude_x': [40.74],
    'Longitude_x': [-74.01],
    'Delivery_Location_ID_x': [0],
    'Demand_x': [150],
    'Latitude_y': [40.74],
    'Longitude_y': [-74.01],
    'Delivery_Location_ID_y': [1],
    'Demand_y': [200],
    'Delivery_Time_Window_x_Evening': [0],
    'Delivery_Time_Window_x_Morning': [1],
    'Delivery_Time_Window_y_Evening': [0],
    'Delivery_Time_Window_y_Morning': [1]
}

# Create the DataFrame
input_df = pd.DataFrame(data)

# Display the input DataFrame
print("Input DataFrame:")
print(input_df)

# Make predictions
try:
    predictions = model.predict(input_df)
    print("Predictions:", predictions)
except Exception as e:
    print("Error during prediction:", e)
