import numpy as np
import pandas as pd 

def dim_product():
    

    '''
    Using python create a product dataset that would be sold at a wizarding store 
    The dataset should have the following columns:
    - 'item': The name of the product
    - 'list_price': The price of the product
    - 'cost': The cost of the product
    - 'weight': The weight of the product
    - 'category': The category of the product
    - 'sub_category': The sub category of the product
    - 'manufacturer': The manufacturer of the product
    - 'brand': The brand of the product
    - 'sku': The sku of the product
    '''

    # Create a dictionary with the data
    data = {
        'item_id' : np.arange(1, 11),
        'item_name': [
            'Elder Wand', 'Invisibility Cloak', 'Resurrection Stone',
            'Firebolt Broomstick', 'Polyjuice Potion', 'Time-Turner',
            'Marauder\'s Map', 'Felix Felicis', 'Deluminator', 'Pensieve'
        ],
        'list_price': [250.00, 300.00, 150.00, 200.00, 50.00, 500.00, 100.00, 75.00, 120.00, 220.00],
        'cost': [150.00, 200.00, 100.00, 120.00, 30.00, 350.00, 60.00, 40.00, 70.00, 140.00],
        'weight': [0.5, 1.0, 0.2, 2.5, 0.5, 0.8, 0.3, 0.1, 0.4, 1.2],
        'category': [
            'Wands', 'Apparel', 'Artifacts', 'Transportation', 'Potions',
            'Artifacts', 'Accessories', 'Potions', 'Accessories', 'Artifacts'
        ],
        'sub_category': [
            'Core Wands', 'Cloaks', 'Magical Stones', 'Broomsticks', 'Transformative Potions',
            'Time Manipulation', 'Maps', 'Luck Potions', 'Light Manipulation', 'Memory Devices'
        ],
        'manufacturer': [
            'Ollivanders', 'Deathly Hallows Inc.', 'Deathly Hallows Inc.',
            'Nimbus Racing Brooms', 'Moste Potente Potions Co.', 'Ministry of Magic',
            'Weasleys\' Wizard Wheezes', 'Slug & Jiggers Apothecary', 'Dumbledore Labs', 'Ministry of Magic'
        ],
        'brand': [
            'Elder Series', 'Stealth Wear', 'Resurrection Line', 'Firebolt Series',
            'Polyjuice Brand', 'Time-Turner Series', 'Marauder\'s Collection', 'Felix Brand', 'Deluminator Series', 'Pensieve Collection'
        ],
        'sku': [
            'WND001', 'CLK002', 'ART003', 'BRM004', 'PTN005', 'ART006', 'ACC007', 'PTN008', 'ACC009', 'ART010'
        ]
    }

    # Create the DataFrame
    df = pd.DataFrame(data)

    # Optionally, save the DataFrame to a CSV file
    df.to_csv('data/dim_product.csv', index=False)
    
