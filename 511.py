import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    players = activity.sort_values(by='event_date').drop_duplicates(subset='player_id')
    players = players.rename(columns={'event_date': 'first_login'})
    return players[['player_id', 'first_login']]