import requests  # HTTP requests
import pandas as pd  # Data manipulation

def get_location():
    """Get user's current location using IP geolocation"""
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        loc = data.get("loc", "")
        
        if loc:
            # Split "lat,lng" string into coordinates
            latitude, longitude = map(float, loc.split(","))
            return latitude, longitude
        
        else:
            return None
    
    except Exception as e:
        print("Error:", e)
        return None

def get_five_starbucks_nearby():
    """Find 5 nearest Starbucks locations to user"""
    location = get_location()
    
    if not location:
        print("Could not retrieve location.")
        return None
    
    latitude, longitude = location
    
    try:
        # Load Starbucks data from GitHub
        data = pd.read_json("https://raw.githubusercontent.com/mmcloughlin/starbucks/refs/heads/master/locations.json")
        
        if data.empty:
            print("No Starbucks data available.")
            return None
        
        # Calculate distance using Euclidean formula
        data["distance"] = ((data["latitude"] - latitude) ** 2 + (data["longitude"] - longitude) ** 2) ** 0.5
        data = data.sort_values("distance")
        return data.head(5)
        
    except Exception as e:
        print(f"Error fetching Starbucks data: {e}")
        return None 


