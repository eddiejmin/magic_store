import pandas as pd
import random

'''
Create a python script to create a dim_account dataset with the following conditions:
- account_id: unique identifier for each account
- account_name: name of the account
- city: city where the account is located

The dataset should have 10 accounts with the following information:
- account_id: 1 to 10
- account_name: randomly generated magic themed names
- city: randomly selected from the top 10 cities in the US by population
'''

# List of top 10 cities in the US by population (as of recent census data)
top_10_cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"
]

# List of magic themed account names
magic_names = [
    "Enchanted Elixirs", "Mystical Potions", "Wizardly Wares",
    "Sorcerer's Supplies", "Magical Ingredients", "Enchanted Artifacts",
    "Mystic Charms", "Spellbound Scrolls", "Alchemy Emporium", "Wizard's Workshop"
]

# Function to generate the dim_account dataset
def dim_account():
    # Create account_id and account_name
    account_id = list(range(1, 11))
    account_name = magic_names

    # Randomly assign cities to accounts from the top 10 cities
    city = random.choices(top_10_cities, k=10)

    # Create the DataFrame
    df = pd.DataFrame({
        'account_id': account_id,
        'account_name': account_name,
        'city': city
    })

    df.to_csv('data/dim_account.csv', index=False)