import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset='salary').sort_values(
        by='salary', ascending=False)  # remove duplicates and sort descending
    if employee.shape[0] < N or N < 1:  # if less than N employees, return null
        employee['salary'] = None
        employee = employee[0:1]  # get first row = null
    else:
        employee = employee[N-1:N]  # get nth employee by salary
    return employee[['salary']].rename(columns={'salary':'getNthHighestSalary('+str(N)+')'})