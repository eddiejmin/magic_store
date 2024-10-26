import numpy as np 
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import FunctionTransformer
from category_encoders import TargetEncoder
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

from .formula_transformers import FormulaTransformer

class PriceElasticity:
    """
    Create a gridsearch pipeline to find the best price elasticity model using ridge regression 
    """
    def __init__(self):
        pass 

    def fit(self, X, y):
        # Define the numerical, categorical, and target
        num_attribs = ['quantity']
        cat_attribs = ['region']
        y_attribs = ['margin']
        
        # Create a pipeline to preprocess the data
        num_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('log_scaler', FunctionTransformer(np.log1p)),
        ])

        X_pipeline_standard = ColumnTransformer([
            ('num', num_pipeline, num_attribs),
            ('cat', TargetEncoder(), cat_attribs),
        ], remainder='drop')

        X_pipeline_standard.set_output(transform="pandas")

        # Since we used TargetEncoder we need to add interaction terms
        X_pipeline_interaction = Pipeline(
            [
                ("preprocess", X_pipeline_standard),
                ("formula", FormulaTransformer("num__quantity * cat__region")),  #
            ]
        )
        
        # Set the model
        model = TransformedTargetRegressor(
            regressor=Ridge(), 
            transformer=FunctionTransformer(np.log1p, np.expm1)
        )

        # Create the full pipeline
        full_pipeline = Pipeline([
            ('preprocess', X_pipeline_interaction),
            ('model', model)
        ])

        # Set the parameters for the gridsearch
        param_grid = {
            'model__regressor__alpha': [0, 0.01, 0.1, 1, 10]
        }

        # Create the gridsearch
        grid_search = GridSearchCV(
            full_pipeline, 
            param_grid, 
            cv=5, 
            n_jobs=-1,
            scoring='neg_mean_squared_error',
            refit=True
        )

        self.estimator = grid_search.fit(X, y)

        return self

    def predict(self, X):
        pred = self.estimator.predict(X)
        pred = self.clip(pred)
        return pred

    def clip(self, X):
        return np.clip(X, 0, 100)
    
    def get_coef(self):
        return self.estimator.best_estimator_['model'].regressor_.coef_