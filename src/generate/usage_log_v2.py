
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
    - page_load_time should be a normal distribution with mean=3.0 and std=1.0
    
    Args:
        num_rows (int): Number of rows to generate.

    Returns:
        pd.DataFrame: A DataFrame containing the logging data.
    """

    user_id_range = (1, 2000)
    page_names = ['Home', 'Product Catalog', 'Cart', 'Checkout', 'Confirmation']
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
        sequence = ['Home']
        if random.random() < 0.35:  # 35% chance the user views a product
            sequence.append('Product Catalog')
            if random.random() < 0.2:  # 20% chance the user adds to cart
                sequence.append('Cart')
                if random.random() < 0.1:  # 10% chance the user proceeds to checkout
                    sequence.append('Checkout')
                    if random.random() < 0.4:  # 40% chance the user reaches confirmation
                        sequence.append('Confirmation')
        return sequence

    # Initialize lists for data
    request_ids = []
    user_ids = []
    timestamps = []
    page_name_list = []
    actions_list = []
    page_load_times = []

    # Generate dataset
    for _ in range(num_rows):
        request_ids.append(str(uuid.uuid4()))  # unique identifier for each row
        user_ids.append(random.randint(*user_id_range))  # random user ID
        timestamps.append(random_timestamp(start_date, end_date))  # Random timestamp
        sequence = generate_page_sequence()
        page_name = random.choice(sequence)  # Page name based on the sequence
        page_name_list.append(page_name)
        actions_list.append(random.choice(actions))  # Random action
        page_load_times.append(max(0.1, random.normalvariate(3.0, 1.0)))

    # Create DataFrame
    df = pd.DataFrame({
        'request_id': request_ids,
        'user_id': user_ids,
        'timestamp': timestamps,
        'page_name': page_name_list,
        'action': actions_list, 
        'page_load_times': page_load_times
    })
    # Optionally, save the DataFrame to a CSV file
    df.to_csv('data/usage_log.csv', index=False)
