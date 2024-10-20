```
# Convert both columns to string
complete_data['Destination'] = complete_data['Destination'].astype(str)
delivery_data['Delivery_Location_ID'] = delivery_data['Delivery_Location_ID'].astype(str)

# Now perform the merge
complete_data = pd.merge(complete_data, delivery_data, left_on='Destination', right_on='Delivery_Location_ID')

# Display the first few rows of the complete dataset
print(complete_data.head())
```
