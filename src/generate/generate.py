from .dim_orderitem import dim_orderitem
from .dim_product import dim_product
from .dim_store import dim_store
from .dim_account import dim_account
from .dim_user import dim_user
from .usage_log_v2 import generate_logging_data

def generate():
    # Generate the 'dim_orderitem' dataset
    dim_orderitem()

    # Generate the 'dim_product' dataset
    dim_product()

    # Generate the 'dim_store' dataset
    dim_store()

    # Generate the 'dim_account' dataset
    dim_account()

    # Generate the 'dim_user' dataset
    dim_user()

    # Generate the 'usage_log' dataset
    generate_logging_data()

# Run the pipeline
if __name__ == '__main__':
    generate()
    
