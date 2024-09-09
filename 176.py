import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset='salary').sort_values(
        by='salary', ascending=False)  # remove duplicates and sort descending
    if employee.shape[0] < 2:  # if less than 2 employees, return null
        employee['salary'] = None
    else:
        employee = employee[1:2]  # get second employee by salary
    return employee[['salary']].rename(columns={'salary':'SecondHighestSalary'})