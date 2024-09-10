import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users.loc[users['mail'].str.contains(
        '^[A-Za-z][A-Za-z0-9_\-\.]*@leetcode\.com$', regex=True)]