import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    transactions = transactions[['account', 'amount']]
    transactions = transactions.groupby('account').sum().reset_index()
    merged = pd.merge(users, transactions).rename(columns={'amount': 'balance'})
    return merged[merged.balance > 10000][['name', 'balance']]