## This section explains the data variables present in the route optimization project. These variables are used in the AI model to predict optimal delivery routes, manage vehicle capacities, and calculate delivery times and costs.

1. Origin

- Definition: The starting location of a delivery route, represented as an identifier (numeric code).

  - Example: 0 (represents a specific warehouse or depot).

2. Destination

- Definition: The final location where goods are delivered, represented as an identifier (numeric code).
  
  - Example: 0 (represents a specific delivery location).

3. Traffic_Delay

- Definition: The amount of delay caused by traffic on the route between the origin and destination, usually measured in minutes or hours.
  
  - Example: 48.96 (48.96 minutes of delay due to traffic).

4. Distance

- Definition: The distance between the origin and destination, typically measured in kilometers or miles.
  
  - Example: 41.33 (41.33 miles or kilometers between origin and destination).

5. Vehicle_ID

- Definition: A unique identifier for the vehicle used for the delivery.
  
  - Example: 0 (the identifier for the first vehicle in the fleet).

6. Vehicle_1_Capacity

- Definition: The total capacity (in units or weight) that vehicle 1 can carry on a delivery route.
  
  - Example: 1718 (the vehicle can carry up to 1718 units or a specific weight of goods).

7. Vehicle_2_Capacity

- Definition: The total capacity (in units or weight) that vehicle 2 can carry.
  
  - Example: 1420 (the vehicle can carry up to 1420 units or a specific weight of goods).

8. Vehicle_3_Capacity

- Definition: The total capacity (in units or weight) that vehicle 3 can carry.
  
  - Example: 1237 (the vehicle can carry up to 1237 units or a specific weight of goods).

9. Vehicle_4_Capacity

- Definition: The total capacity (in units or weight) that vehicle 4 can carry.
  
  - Example: 1855 (the vehicle can carry up to 1855 units or a specific weight of goods).

10. Vehicle_5_Capacity

- Definition: The total capacity (in units or weight) that vehicle 5 can carry.
  
  - Example: 669 (the vehicle can carry up to 669 units or a specific weight of goods).

11. Load

- Definition: The amount of goods or products that the vehicle is carrying for a specific delivery.
  
  - Example: 1473 (the vehicle is currently carrying 1473 units or a specific weight of goods).

12. Fuel_Consumption

- Definition: The fuel consumption of the vehicle for this delivery, measured in liters per kilometer or miles per gallon.
  
  - Example: 14.09 (14.09 liters of fuel are consumed per unit of distance).

13. Latitude

- Definition: The latitude coordinate of the delivery location.
  
  - Example: 40.7447 (geographic latitude of the delivery location).

14. Longitude

- Definition: The longitude coordinate of the delivery location.
  
  - Example: -74.2163 (geographic longitude of the delivery location).

15. Delivery_Location_ID

- Definition: A unique identifier for the delivery location.
  
  - Example: 0 (an identifier representing a specific delivery location).

16. Demand

- Definition: The number of goods required at the delivery location.
  
  - Example: 144 (144 units are needed at the delivery destination).

17. Delivery_Time_Window

- Definition: The time window in which the delivery must be completed, typically expressed as 'Morning', 'Afternoon', or 'Evening'.
  
  - Example: Morning (the delivery must take place in the morning).
