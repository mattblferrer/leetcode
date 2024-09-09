import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    products = products[(products['low_fats'] == 'Y') & 
        (products['recyclable'] == 'Y')]  # filter by low fats and recyclable
    return products[['product_id']]  # return only product_id