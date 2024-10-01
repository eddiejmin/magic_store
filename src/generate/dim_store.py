import pandas as pd
import random

# List of top 10 cities in the US by population (as of recent census data)
top_10_cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"
]

# Function to generate the dim_store dataset
def dim_store():
    '''
    Create python script to create a dim_store dataset the following conditions:
    - store_id: unique identifier for each store
    - store_name: name of the store
    - store_city: city where the store is located
    - is_online: online or offline

    The dataset should have 10 stores with the following information:
    - store_id: 1 to 10
    - store_name: randomly generated store names
    - store_city can be in the top 10 cities in the US by population 
    - is_online: 50% of the stores are online and 50% are offline
    ''' 

    # Create store_id and store_name
    store_id = list(range(1, 11))
    store_name = [f"Store {i}" for i in store_id]

    # Randomly assign cities to stores from the top 10 cities
    store_city = random.choices(top_10_cities, k=10)

    # Create the is_online column with 50% of stores being online and 50% offline
    is_online = random.choices([True, False], k=10)

    # Create the DataFrame
    df = pd.DataFrame({
        'store_id': store_id,
        'store_name': store_name,
        'store_city': store_city,
        'is_online': is_online
    })
    
    df.to_csv('data/dim_store.csv', index=False)
