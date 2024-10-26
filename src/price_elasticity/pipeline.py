import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
import pickle

from .price_elasticity_cluster import PriceElasticityCluster


def train_pipeline():
    '''
    Create a training pipeline to fit the price elasticity model
    '''
    # load the data
    DATA_PATH = 'data/dim_quote.csv'
    df = pd.read_csv(DATA_PATH)
    train_df = df.query("status == 'won'")

    # split the data
    y = train_df['margin']
    X = train_df.drop(columns=['margin'])

    # split test-train data using stratification by region
    X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=41,
            stratify=X['region'] if X['region'].nunique() > 1 else None
        )

    # instantiate the model
    estimator = PriceElasticityCluster()

    # fit the model
    estimator.fit(X_train, y_train)

    # save the model
    with open('trained_models/model.pkl', 'wb') as f:
        pickle.dump(estimator, f)

    # apply model to full dataset and save predictions
    df = estimator.predict(df)

    # save the predictions
    df.to_csv(DATA_PATH, index=False)


if __name__ == '__main__':
    train_pipeline()


