import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_logging_data(num_rows=10000):
    """
    Generate a sample e-commerce logging dataset with the following columns:
    - request_id
    - user_id
    - timestamp
    - page_name
    - action (view, click)

    The data should have at least 1000 rows.
    - request_id should be a unique identifier for each row
    - user_id should be a random number between 1 and 10
    - timestamp should be between 2024-01-01 and 2024-12-31
    - page_name should be ['home', 'product', 'cart', 'checkout', 'confirmation']
    - 'checkout' can only occur after 'cart'
    - 'confirmation' can only occur after 'checkout'
    - action should be ['view', 'click']
    
    Args:
        num_rows (int): Number of rows to generate.

    Returns:
        pd.DataFrame: A DataFrame containing the logging data.
    """
    # Parameters
    request_ids = range(1, num_rows + 1)
    user_ids = np.random.randint(1, 300, num_rows)  # Random user_id between 1 and 10
    page_names = ['home', 'product', 'cart', 'checkout', 'confirmation']
    actions = ['view', 'click']

    # Generate random timestamps between 2024-01-01 and 2024-12-31
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    timestamps = [start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds()))) for _ in range(num_rows)]

    # Generate random page_names and actions
    page_name = np.random.choice

    # Create the DataFrame
    df = pd.DataFrame({
        'request_id': request_ids,
        'user_id': user_ids,
        'timestamp': timestamps,
        'page_name': np.random.choice(page_names, num_rows),
        'action': np.random.choice(actions, num_rows)
    })

    # Optionally, save the DataFrame to a CSV file
    df.to_csv('data/usage_log.csv', index=False)
    
