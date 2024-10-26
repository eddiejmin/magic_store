import numpy as np
import pandas as pd 
from .price_elasticity import PriceElasticity

class PriceElasticityCluster():
    """
    Since there are multiple products in the dataset, we need to train multiple models in a loop 
    and save the models in a dictionary.
    """

    def __init__(self):
        self.models = {}

    def fit(self, X, y):
        '''
        Fit the model to the data
        '''
        for product_id in X['product_id'].unique().tolist():
            X_product = X[X['product_id'] == product_id]
            y_product = y[X['product_id'] == product_id]
            model = PriceElasticity()
            model.fit(X_product, y_product)
            self.models[product_id] = model
        return self

    def predict(self, X):
        '''
        Predict the price elasticity for each product
        '''

        X = X.reset_index(drop=True)

        # only evaluate products that are in the model
        df_skip = X[~X["product_id"].isin(self.models.keys())]
        df_eval = X[X["product_id"].isin(self.models.keys())]

        # Predict FMV
        for i in df_eval["product_id"].unique().tolist():
            model = self.models[i]
            index = df_eval[df_eval["product_id"] == i].index
            X_eval = df_eval.loc[index]
            y_pred = model.predict(X_eval)
            df_eval.loc[index, "prediction"] = y_pred

        # Combine the two dataframes
        df = pd.concat([df_skip, df_eval], axis=0)

        # Return the dataframe in the original order
        df = df.sort_index()
        return df
        