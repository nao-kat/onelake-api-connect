#Create a sample CSV file for testing
import pandas as pd
import os

# sample data
data = [
    [1, "N", 142, 236, 1, 2.15, 10.5, 0.5, 0.5, 1, 0, 12.5, 1],
    [2, "N", 236, 142, 2, 5.2, 20, 0.5, 0.5, 2.5, 0, 23.5, 2],
    [1, "N", 100, 151, 1, 3.4, 13, 0.5, 0.5, 1.5, 0, 15.5, 1],
    [2, "N", 230, 90, 1, 4.0, 16, 0.5, 0.5, 3, 0, 20, 2],
    [1, "N", 90, 230, 3, 2.0, 9.5, 0.5, 0.5, 0.5, 0, 11, 1],
    [2, "N", 79, 256, 1, 6.5, 23, 0.5, 0.5, 2.5, 0, 26.5, 1],
    [1, "N", 140, 100, 2, 2.8, 11, 0.5, 0.5, 1.2, 0, 13.2, 2],
    [2, "N", 237, 85, 1, 3.9, 15.5, 0.5, 0.5, 2.8, 0, 19.3, 2],
    [1, "N", 50, 90, 1, 2.25, 10, 0.5, 0.5, 1, 0, 12, 1],
    [2, "N", 251, 42, 1, 5.8, 21, 0.5, 0.5, 2, 0, 24, 2],
    [1, "N", 89, 36, 1, 2.75, 10.5, 0.5, 0.5, 1, 0, 12.5, 1],
    [2, "N", 36, 89, 2, 4.8, 18, 0.5, 0.5, 3, 0, 22, 2],
    [1, "N", 64, 25, 1, 2.3, 9, 0.5, 0.5, 0.5, 0, 10.5, 1],
    [2, "N", 25, 64, 1, 5.1, 20, 0.5, 0.5, 2.2, 0, 23.7, 2],
    [1, "N", 130, 110, 2, 3.75, 14, 0.5, 0.5, 2, 0, 17, 1]
]

# coumn names
columns = [
    "vendorid", "store_and_fwd_flag", "Pickup_location_id", "Dropoff_location_id",
    "passenger_count", "trip_distance", "fare_amount", "extra", "mta_tax",
    "tip_amount", "tolls_amount", "total_amount", "payment_type"
]

# Create DataFrame, and add ID
df = pd.DataFrame(data, columns=columns)
df.insert(0, "id", range(1, len(df) + 1))

# path to save the CSV file
output_path = "<path>"
df.to_csv(output_path, index=False)

output_path
