```
import pandas as pd

# Load each dataset
warehouse_data = pd.read_csv('warehouse_data.csv')
delivery_data = pd.read_csv('delivery_data.csv')
traffic_data = pd.read_csv('traffic_data.csv')
distance_matrix = pd.read_csv('distance_matrix.csv')
vehicle_data = pd.read_csv('vehicle_data.csv')

# Display the first few rows of each dataset to check the data
print("Warehouse Data")
print(warehouse_data.head())

print("\nDelivery Data")
print(delivery_data.head())

print("\nTraffic Data")
print(traffic_data.head())

print("\nDistance Matrix")
print(distance_matrix.head())

print("\nVehicle Data")
print(vehicle_data.head())

```
