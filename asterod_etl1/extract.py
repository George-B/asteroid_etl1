import requests
from logger import logger
from config import API_KEY

def fetch_asteroids(start_date, end_date):
    try:
        response = requests.get(
            "https://api.nasa.gov/neo/rest/v1/feed",
            params={
                "start_date": start_date,
                "end_date": end_date,
                "api_key": API_KEY
            }
        )

        print("STATUS CODE:", response.status_code)
        print("RESPONSE:", response.text[:200])

        response.raise_for_status()
        return response.json()

    except Exception as e:
        print("ERROR:", e)
        logger.error(f"API request failed: {e}")
        return None