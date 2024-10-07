import numpy as np 
import pandas as pd

def generate_transportation_lanes(lanes=25):    
    '''
    Create a python script that generates a transportation lanes dataset with the following conditions:
    - 100 rows
    - Columns: 'lane_id', 'origin', 'destination', 'distance', 'cost_per_mile'
    - 'lane_id' column should be a unique identifier for each lane
    - 'origin' column should be a random city from the list of cities below
    - 'destination' column should be a random city from the list of cities below, different from the 'origin'
    - 'cost_per_mile' column should be a random float between 1.0 and 2.0
    - List of city: ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
    - probability of selecting cities should be uneven (e.g., higher probability for New York and Los Angeles)

    Returns:
        pd.DataFrame: A DataFrame containing the transportation lanes data.
    '''

    # List of cities
    city = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']

    # Generate unique lane_ids
    lane_ids = np.arange(1, lanes + 1)  # Unique lane_id from 1 to 100

    # Generate random origin and destination city
    origins = np.random.choice(city, lanes)
    destinations = np.random.choice(city, lanes)
    for i in range(lanes):
        while origins[i] == destinations[i]:
            destinations[i] = np.random.choice(city)

    # Generate random cost_per_mile between 1.0 and 2.0
    cost_per_miles = np.random.uniform(1.0, 2.0, lanes)

    # Create the DataFrame
    df = pd.DataFrame({
        'lane_id': lane_ids,
        'origin': origins,
        'destination': destinations,
        'cost_per_mile': cost_per_miles
    })

    # Optionally, save the DataFrame to a CSV file
    df.to_csv('data/transportation_lanes.csv', index=False)
    

    
