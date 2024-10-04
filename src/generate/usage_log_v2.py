
import pandas as pd
import random
import uuid
from datetime import datetime, timedelta

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
    - user_id should be a random number between 1 and 300
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

    user_id_range = (1, 300)
    page_names = ['home', 'product', 'cart', 'checkout', 'confirmation']
    actions = ['view', 'click']
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)

    # Function to generate random timestamps between the given start and end date
    def random_timestamp(start, end):
        delta = end - start
        random_seconds = random.randint(0, int(delta.total_seconds()))
        return start + timedelta(seconds=random_seconds)

    # Helper to ensure proper sequence rules are followed for 'cart', 'checkout', and 'confirmation'
    def generate_page_sequence():
        sequence = ['home']
        if random.random() < 0.35:  # 35% chance the user views a product
            sequence.append('product')
            if random.random() < 0.2:  # 20% chance the user adds to cart
                sequence.append('cart')
                if random.random() < 0.1:  # 10% chance the user proceeds to checkout
                    sequence.append('checkout')
                    if random.random() < 0.4:  # 40% chance the user reaches confirmation
                        sequence.append('confirmation')
        return sequence

    # Initialize lists for data
    request_ids = []
    user_ids = []
    timestamps = []
    page_name_list = []
    actions_list = []

    # Generate dataset
    for _ in range(num_rows):
        request_ids.append(str(uuid.uuid4()))  # unique identifier for each row
        user_ids.append(random.randint(*user_id_range))  # random user ID
        timestamps.append(random_timestamp(start_date, end_date))  # Random timestamp
        sequence = generate_page_sequence()
        page_name = random.choice(sequence)  # Page name based on the sequence
        page_name_list.append(page_name)
        actions_list.append(random.choice(actions))  # Random action

    # Create DataFrame
    df = pd.DataFrame({
        'request_id': request_ids,
        'user_id': user_ids,
        'timestamp': timestamps,
        'page_name': page_name_list,
        'action': actions_list
    })
    # Optionally, save the DataFrame to a CSV file
    df.to_csv('data/usage_log.csv', index=False)
