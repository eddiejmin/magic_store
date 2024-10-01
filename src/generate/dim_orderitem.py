import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def dim_orderitem(num_rows=10000):

    '''
    Create python script to create sales dataset the following conditions:
    - 10000 rows
    - Columns: 'data', 'store', 'item', 'quantity', 'price'
    - 'date' column should be a random date between 1/1/2023 and 12/31/2024
    - 'store_id' column should be a random integer between 1 and 10
    - 'item_id' column should be a random integer between 1 and 10
    - 'account_id' column should be a random integer between 1 and 1000
    - 'quantity' column should be a random integer between 1 and 100
    - 'discount' column that is normally distributed with mean=20, std=5
    - add seasonality by setting sales to be slightly higher during the summer and winter using a random multiplier between 0.8 and 1.2
    '''

     # Generate random dates between 1/1/2023 and 12/31/2024
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)
    date_range = [start_date + timedelta(days=random.randint(0, (end_date - start_date).days)) for _ in range(num_rows)]

    # Generate random integers for store, item, quantity, and price
    store_id = np.random.randint(1, 11, num_rows)
    item_id = np.random.randint(1, 11, num_rows)
    account_id = np.random.randint(1, 100, num_rows)
    quantity = np.random.randint(1, 101, num_rows)

    # Generate random discount values using a normal distribution with mean=20, std=5
    discount = np.random.normal(20, 5, num_rows)
    discount = np.clip(discount, 1, 100)  # Ensuring that discount values are between 1 and 100

   
    # Create the DataFrame
    df = pd.DataFrame({
        'date': date_range,
        'store_id': store_id,
        'item_id': item_id,
        'account_id': account_id,
        'quantity': quantity,
        'discount': np.round(discount, 0)  # Rounding discount to nearest integer
    })
    
     # Adjust quantity for seasonality (increase during summer and winter)
    df['month'] = df['date'].dt.month
    
    # Define summer and winter months
    summer_months = [6, 7, 8]  # June, July, August
    winter_months = [12, 1, 2]  # December, January, February
    
    # Apply randomized multipliers to quantity for summer and winter months
    summer_multipliers = np.random.uniform(1.1, 1.3, num_rows)  # Random multiplier between 1.1 and 1.3 for summer
    winter_multipliers = np.random.uniform(1.1, 1.3, num_rows)  # Random multiplier between 1.1 and 1.3 for winter
    
    # Apply the random multiplier to the quantity based on the month
    df.loc[df['month'].isin(summer_months), 'quantity'] *= summer_multipliers[df['month'].isin(summer_months)]
    df.loc[df['month'].isin(winter_months), 'quantity'] *= winter_multipliers[df['month'].isin(winter_months)]
    
    # Drop the 'month' column as it's no longer needed
    df.drop(columns=['month'], inplace=True)

    # Optionally, save the DataFrame to a CSV file
    df.to_csv('data/dim_orderitem.csv', index=False)