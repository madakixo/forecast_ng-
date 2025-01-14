import pandas as pd
from config import CSV_FILE_PATH

def load_data():
    """Load data from CSV file."""
    try:
        df = pd.read_csv(CSV_FILE_PATH)
        df['date_column'] = pd.to_datetime(df['date_column'])
        df.set_index('date_column', inplace=True)
        return df
    except FileNotFoundError:
        logging.error("CSV file not found or cannot be read.")
        raise
    except KeyError:
        logging.error("Expected column 'feature1' not found in CSV.")
        raise

def prepare_data_for_api(df):
    """Prepare data for API call."""
    # Split data into train and test for evaluation
    train_data = df.iloc[:-len(df)//10]  # Using last 10% for testing
    test_data = df.iloc[-len(df)//10:]
    
    data = train_data['feature1'].to_dict()
    return train_data, test_data, {
        "inputs": [
            {"name": "series", "data": data}
        ]
    }
