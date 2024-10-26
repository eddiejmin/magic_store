import numpy as np 
import pandas as pd
import random

np.random.seed(0)
regions = ['West', 'East', 'North', 'South']

def dim_quote(rows=100000):
    '''
    Create a script to create a dimension table for sales quotes.

    Conditions:
    - 10,000 rows
    - Columns: 'quote_id', 'quote_date', 'customer_id', 'sales_rep_id', 'product_id', 'quantity', 'unit_price'
    - 'quote_id' column should be a unique identifier for each quote
    - 'quote_date' column should be a random date between 2024-01-01 and 2024-12-31
    - 'account_id' column should be a random integer between 1 and rows
    - 'sales_rep_id' column should be a random integer between 1 and 10
    - 'product_id' column should be a random integer between 1 and 10
    - 'quantity' column should be pareto distribution with a mean of 500
    - 'status' column should be a random choice between 'won', 'lost' with probabilities 0.2 and 0.8 respectively
    - 'unit_price' will be created after referencing dim_product table since we want to utilize the 'list_price' column
    - 'margin' column is derived from a linear regression model with random noise
    - 'unit_price' column is derived from Margin of the product
    - 'close_date' column should be random date after 'quote_date' and before 'quote_date' + 30 days
    '''

    # Create a dictionary with the data
    data = {
        'quote_id': np.arange(1, rows+1),
        'quote_date': np.random.choice(pd.date_range(start='2024-01-01', end='2024-12-31'), rows),
        'account_id': np.random.randint(1, rows+1, rows),
        'sales_rep_id': np.random.randint(1, 11, rows),
        'product_id': np.random.randint(1, 12, rows),
        'quantity': np.random.pareto(a=3, size=rows) * 500,
        'status': np.random.choice(['won', 'lost'], rows, p=[0.2, 0.8]),
        'region': np.random.choice(regions, rows)
    }

    # Create the DataFrame
    df = pd.DataFrame(data)

    # Round the 'quantity' column to the nearest integer
    df['quantity'] = df['quantity'].round().astype(int)

    # Create the 'close_date' column
    df['close_date'] = df['quote_date'] + pd.to_timedelta(np.random.randint(1, 30, rows), unit='D')

    df['days_to_close'] = (df['close_date'] - df['quote_date']).dt.days

    # Load the dim_product table
    dim_product = pd.read_csv('data/dim_product.csv')

    # Merge the dim_product table with the df DataFrame
    df = pd.merge(df, dim_product[['product_id', 'list_price']], on='product_id', how='left')
    
    # Create the 'unit_price' column
    df['unit_price'] = df['list_price']

    # Create random options for the slope
    bias = (np.random.uniform(0.6, 0.9, size=5)).tolist()

    # Create the 'margin' column using custom function
    df['margin'] = df.groupby('product_id')['quantity'].transform(margin)

    # Set price to be slightly lower if status is 'won'
    win_bias = np.random.normal(5, 5, 1).item() # Randomly select a value from the normal distribution with mean 10 and std 5
    win_adjustment = np.log1p(df['quantity']) * 0.1 +  win_bias # Create an adjustment based on the quantity - this should be a positive number
    df.loc[df['status'] == 'won', 'margin'] = df['margin'] - win_adjustment

    days_to_close_adjustment = np.log1p(df['days_to_close']) * 10 # Create an adjustment based on the days to close - this should be a positive number
    df['margin'] = df['margin'] - days_to_close_adjustment

    # Add positive adjustment since data is skewed towards zero
    df['margin'] = df['margin'] + 30


      # Define fixed region biases for each region
    region_bias_map = dict({
        'West': np.random.uniform(10, 15),
        'East': np.random.uniform(5, 10),
        'North': np.random.uniform(-5, 0),
        'South': np.random.uniform(-10, -5)
    })

    # Apply the region bias to the dataframe
    df['region_bias'] = df['region'].map(region_bias_map)

    # Add the region bias to the margin
    df['margin'] = df['margin'] + df['region_bias']
    
    # Cap margin at 0 and 100
    df.loc[df['margin'] < 0, 'margin'] = 0
    df.loc[df['margin'] > 100, 'margin'] = 100
    
    # Create the 'unit_price' column
    df['unit_price'] = df['list_price'] * (df['margin'] / 100)

    # round the unit price to 2 decimal places
    df['unit_price'] = df['unit_price'].round(2)

    # Set ceiling for unit price as list_price
    df.loc[df['unit_price'] > df['list_price'], 'unit_price'] = df['list_price']

    # Drop quantities set at 1000 (limitation of the pareto distribution)
    df = df[df['quantity'] < 1000]

    # Optionally, save the DataFrame to a CSV file
    df.to_csv('data/dim_quote.csv', index=False)


def margin(qty):
    '''
    Create the 'margin' column in the DataFrame.
    '''
    # Create random options for the slope
    slope = (np.random.uniform(1, 10, size=5)).tolist()[-1]
    bias = (np.random.uniform(60, 90, size=10)).tolist()[-1]

    # Create the 'margin' column
    margin = -1 * np.log1p(qty) * slope + bias + np.random.normal(0, 10, len(qty)) 

    # Cap margin at 0 and 100
    margin = np.clip(margin, 0, 100)
    return margin
