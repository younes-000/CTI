# This script is used to get the information of an indicator from the OTX API

import requests
import json

API_KEY = "here your api" # Replace with your OTX API key
BASE_URL = "https://otx.alienvault.com/api/v1" # Base URL for OTX API


HEADERS = {
    "X-OTX-API-KEY": API_KEY,
    "Content-Type": "application/json"
}

def get_indicator(indicator_type: str, indicator: str, section: str = "general"):
   # here I will get the indicator type and the indicator itself
    url = f"{BASE_URL}/indicators/{indicator_type}/{indicator}/{section}"
    resp = requests.get(url, headers=HEADERS) # Make a GET request to the OTX API
    resp.raise_for_status() # Raise an error for bad responses
    return resp.json() # Return the JSON response


if __name__ == "__main__":
    IPV4 = input("Enter the IPV4 address: ") # here you put the IPV4 address
    data = get_indicator("IPv4", IPV4, section="general") # Call the function to get the indicator data
    print(json.dumps(data, indent=2))
