import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = ((triangle.x + triangle.y > triangle.z) &
                            (triangle.x + triangle.z > triangle.y) &
                            (triangle.y + triangle.z > triangle.x)).astype(str)
    
    return triangle.replace({'True': 'Yes', 'False': 'No'})