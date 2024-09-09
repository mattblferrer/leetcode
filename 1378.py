import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    employees = pd.merge(employees, employee_uni, on='id', how='left')
    return employees[['unique_id', 'name']]