

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def dim_user(num_rows=2000):
    """
    Generate a sample user dataset.

    Create a python script that generates a user dataset with the following conditions:
    - 300 rows
    - Columns: 'user_id', 'sign_up_date, 'zip_code'
    - 'user_id' column should be a unique identifier for each user
    - 'sign_up_date' column should be a random date between 1/1/2024 and 12/31/2024
    - 'convert_date' column should be a random date between 1/1/2024 and 12/31/2024 (can be greater than or equal to sign_up_date)
    - 'convert_date' is only populated for 20% of the users
    - 'zip_code' column should be a random 5-digit integer between 10000 and 99999
    - 'user_type' column should randomly select among ['Power Seeker', 'Philosopher', 'Casual User', 'Adventurer'] with the following distribution: Power Seeker (10%), Philosopher (20%), Casual User (50%), Adventurer (20%)

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

    # Generate random convert_date, with a 20% chance of being populated
    convert_dates = []
    for sign_up_date in sign_up_dates:
        if random.random() <= 0.2:  # 20% chance to have a convert_date
            # Generate convert_date as a random date >= sign_up_date
            convert_date = sign_up_date + timedelta(days=random.randint(0, 100))
            convert_dates.append(convert_date)
        else:
            # 80% chance to have no convert_date (represented by None)
            convert_dates.append(None)

    # Generate random zip codes (5-digit integers between 10000 and 99999)
    zip_codes = np.random.randint(10000, 100000, num_rows)

    user_types = ['Power Seeker', 'Philosopher', 'Casual User', 'Adventurer']
    user_type_weights = [0.1, 0.2, 0.5, 0.2]
    user_type = np.random.choice(user_types, num_rows, p=user_type_weights)

    # Create the DataFrame
    user_data = pd.DataFrame({
        'user_id': user_ids,
        'sign_up_date': sign_up_dates,
        'convert_date': convert_dates,
        'zip_code': zip_codes,
        'user_type': user_type
    })

    # Optionally, save the DataFrame to a CSV file
    user_data.to_csv('data/dim_user.csv', index=False)