from numpy import nan
import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    counts = my_numbers['num'].value_counts().reset_index()
    single = counts[counts['count'] == 1][['num']].sort_values(by='num')
    if single.size == 0:  # if no number appears only once (null)
        return pd.DataFrame([nan], columns=['num'])
    return single.tail(1)