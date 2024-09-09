import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    combined = pd.concat([person, address])
    return combined[['firstName', 'lastName', 'city', 'state']]