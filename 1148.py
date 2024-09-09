import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    same = views[views.author_id == views.viewer_id]
    return same.sort_values(by='author_id').rename(columns={'author_id': 'id'})[['id']].drop_duplicates()