import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
from api import groq_api_call

def perform_forecast(input_data, model_name="llama3-8b-8192"):
    """Perform forecast using Groq API."""
    forecast_result = groq_api_call(f"models/{model_name}/predictions", input_data)
    if forecast_result is None:
        return None

    try:
        forecasts = forecast_result['predictions']
        forecast_df = pd.DataFrame(forecasts, columns=['date', 'value'])
        forecast_df['date'] = pd.to_datetime(forecast_df['date'])
        forecast_df.set_index('date', inplace=True)
        return forecast_df
    except KeyError:
        logging.error(f"Unexpected API response format: {forecast_result}")
        return None

def evaluate_forecast(forecast_df, test_data):
    """Evaluate the forecast accuracy."""
    combined = pd.concat([test_data['feature1'], forecast_df['value']], axis=1)
    combined.columns = ['actual', 'predicted']
    combined = combined.dropna()
    
    mae = mean_absolute_error(combined['actual'], combined['predicted'])
    rmse = np.sqrt(mean_squared_error(combined['actual'], combined['predicted']))
    
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Root Mean Squared Error (RMSE): {rmse}")
    return combined
