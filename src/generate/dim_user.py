

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def dim_user(num_rows=300):
    """
    Generate a sample user dataset.

    Create a python script that generates a user dataset with the following conditions:
    - 300 rows
    - Columns: 'user_id', 'sign_up_date, 'zip_code'
    - 'user_id' column should be a unique identifier for each user
    - 'sign_up_date' column should be a random date between 1/1/2024 and 12/31/2024
    - 'zip_code' column should be a random 5-digit integer between 10000 and 99999

    Args:
        num_rows (int): Number of rows to generate.

    Returns:
        pd.DataFrame: A DataFrame containing the user data.
    """
    # Generate unique user_ids
    user_ids = np.arange(1, num_rows + 1)  # Unique user_id from 1 to num_rows

    # Generate random sign-up dates between 2024-01-01 and 2024-12-31
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    sign_up_dates = [start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds()))) for _ in range(num_rows)]

    # Generate random zip codes (5-digit integers between 10000 and 99999)
    zip_codes = np.random.randint(10000, 100000, num_rows)

    # Create the DataFrame
    user_data = pd.DataFrame({
        'user_id': user_ids,
        'sign_up_date': sign_up_dates,
        'zip_code': zip_codes
    })

    # Optionally, save the DataFrame to a CSV file
    user_data.to_csv('data/dim_user.csv', index=False)