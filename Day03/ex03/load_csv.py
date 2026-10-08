import pandas as pd

def load(path: str) -> pd.DataFrame: 
    """Load a CSV file into a pandas DataFrame."""
    if not isinstance(path, str):
        return None
    p = pd.read_csv(path)
    print("Loading dataset of dimensions", p.shape)
    return(p)