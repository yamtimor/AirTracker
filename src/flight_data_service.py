import requests

API_BASE_URL = "https://opensky-network.org/api/states/all"

def get_flight_data():
    try:
        response = requests.get(API_BASE_URL)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching flight data: {e}")
        return None

if __name__ == "__main__":
    flight_data = get_flight_data()
    if flight_data:
        print(flight_data)
    else:
        print("Failed to retrieve flight data.")
