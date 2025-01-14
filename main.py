import argparse
import logging
from data import load_data, prepare_data_for_api
from forecast import perform_forecast, evaluate_forecast
from visualize import visualize_forecast
from auth import authenticate_user, register_user

# Configure Logging
logging.basicConfig(
    filename='groq_forecast_log.log',
    level=logging.ERROR,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

def main():
    parser = argparse.ArgumentParser(description="Time Series Forecast Application")
    parser.add_argument("--forecast", action="store_true", help="Run forecast")
    parser.add_argument("--register", action="store_true", help="Register a new user")
    args = parser.parse_args()

    if args.register:
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        if register_user(username, password):
            print("User registered successfully.")
        else:
            print("Registration failed. Username might already exist.")
        return

    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if not authenticate_user(username, password):
        print("Authentication failed.")
        return

    if args.forecast:
        try:
            df = load_data()
            train_data, test_data, input_data = prepare_data_for_api(df)
            
            forecast_df = perform_forecast(input_data)
            if forecast_df is not None:
                combined = evaluate_forecast(forecast_df, test_data)
                visualize_forecast(df, combined)
            else:
                print("Forecasting failed.")
        except FileNotFoundError as e:
            logging.error(f"Data file not found: {e}")
            print("Error: Data file not found.")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            print("An unexpected error occurred. Check logs for details.")
    else:
        print("No action specified. Use --forecast to run a forecast or --register to add a new user.")

if __name__ == "__main__":
    main()
