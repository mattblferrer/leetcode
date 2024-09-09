import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(sales, product)[['product_name', 'year', 'price']]