import numpy as np
from generate.generate import generate 
from price_elasticity.pipeline import train_pipeline as train_pricing_elasticity_pipeline

def main():
    np.random.seed(0)
    generate()
    train_pricing_elasticity_pipeline()


if __name__ == '__main__':
    main()
