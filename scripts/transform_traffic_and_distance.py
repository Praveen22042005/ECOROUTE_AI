```
# Convert Traffic Data from a matrix format to a pairwise format
traffic_data_melted = pd.DataFrame(traffic_data.stack()).reset_index()
traffic_data_melted.columns = ['Origin', 'Destination', 'Traffic_Delay']

# Similarly for Distance Matrix
distance_matrix_melted = pd.DataFrame(distance_matrix.stack()).reset_index()
distance_matrix_melted.columns = ['Origin', 'Destination', 'Distance']

# Display the first few rows of the melted data
print("Traffic Data Melted:")
print(traffic_data_melted.head())

print("\nDistance Matrix Melted:")
print(distance_matrix_melted.head())
```
