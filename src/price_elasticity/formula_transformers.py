import numpy as np 
from sklearn.base import BaseEstimator, TransformerMixin
from patsy import dmatrix
import re

# Create a custom transformer to transform the formula into a matrix
class FormulaTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, formula):
        super().__init__()
        self.formula = formula

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        """
        this is a hacky way to get the column names from the formula
        split the formula by the * operator and then split by the + operator
        this will give us all the columns in the formula
        """

        # Identify what is in the formula
        formula_columns = re.split(" \* | \+ ", self.formula)

        non_formula_columns = list(set(X.columns) - set(formula_columns))

        # Append the non formula columns to the formula and split by + operator
        if non_formula_columns:
            formula = self.formula + " + " + " + ".join(non_formula_columns)
        else:
            formula = self.formula

        X_formula = dmatrix(formula_like=formula, data=X)

        design_info = X_formula.design_info
        for k in design_info.factor_infos:
            if design_info.factor_infos[k].type == "categorical":
                self.categories = list(design_info.factor_infos[k].categories)
                break
        self.columns = design_info.column_names
        return np.array(X_formula)

    def get_feature_names(self):
        return self.columns

    def get_categories(self):
        return self.categories
