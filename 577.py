import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee, bonus, on='empId', how='left')
    filtered = merged[(merged['bonus'] < 1000) | (pd.isnull(merged['bonus']))]
    return filtered[['name', 'bonus']]