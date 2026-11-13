import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame and print its dimensions."""
    if not isinstance(path, str) or not path.endswith(".csv"):
        return None

    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except (FileNotFoundError, pd.errors.EmptyDataError,
            pd.errors.ParserError, Exception):
        return None
