import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employees, salaries, how='outer')
    return merged.loc[(merged['name'].isna()) | (merged['salary'].isna())][['employee_id']]