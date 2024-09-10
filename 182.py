import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return person.loc[person.duplicated(subset=['email'])].rename(
        columns={'email': 'Email'})[['Email']].drop_duplicates()