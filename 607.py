import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_id = company[company.name == 'RED']['com_id']  # get ID of RED
    red_orders = orders[orders.com_id.isin(red_id)][['sales_id']]
    return sales_person[~(sales_person.sales_id.isin(red_orders.sales_id))][['name']]