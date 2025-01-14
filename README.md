# forecast_ng-
# use 1960_owards data


# Time Series Forecast Application

This application uses the Groq API with the Llama3-8b-8192 model to perform time series forecasting. It includes user authentication for security and provides visualizations of the forecast results.

## Features

- **Time Series Forecasting:** Utilizes the Groq API for real-time predictions.
- **User Authentication:** Basic user registration and login system using SQLite database for storing hashed passwords.
- **Performance Metrics:** Calculates Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
- **Visualization:** Dynamic plotting of actual vs. predicted values and error over time.

## Setup

### Prerequisites

- Python 3.8 or higher
- A Groq API key (for API access)

### Installation

1. **Clone the repository:**

 
   git clone [your-repository-url]
   cd [project-directory]

Install dependencies:
bash
`pip install -r requirements.txt`

Set up environment variables:
Create a .env file in the project root directory and add:
`GROQ_API_KEY=your_api_key_here`

Or set it in your environment:
On Unix/Linux/MacOS:
bash
`export GROQ_API_KEY=your_api_key_here`
On Windows:
cmd
`set GROQ_API_KEY=your_api_key_here`

Usage
To run a forecast:
bash
`python main.py --forecast`
To register a new user:
bash
`python main.py --register`

Structure
`config.py:` Configuration settings including database and API setup.

`api.py`: Handles API calls to Groq.

`data.py`: Data loading and preparation.

`forecast.py`: Contains the logic for performing forecasts and evaluating them.


`visualize.py`: Handles visualization of forecast results.

`auth.py`: Manages user authentication.


`main.py`: Entry point of the application.

Notes
Ensure your your_time_series_data.csv file is in the same directory as the script or adjust CSV_FILE_PATH in config.py.
This is a basic implementation. For production, consider more robust database solutions and security practices.
