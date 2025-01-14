import requests
import json
import logging
from config import GROQ_API_KEY, GROQ_API_URL

def groq_api_call(endpoint, data=None, method="POST"):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        if method == "POST":
            response = requests.post(f"{GROQ_API_URL}/{endpoint}", headers=headers, json=data)
        else:
            response = requests.get(f"{GROQ_API_URL}/{endpoint}", headers=headers)
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"API call failed: {str(e)}")
        return None
    except json.JSONDecodeError:
        logging.error("Failed to decode JSON from API response")
        return None
