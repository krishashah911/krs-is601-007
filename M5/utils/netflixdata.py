import os
import requests
import mysql.connector
from datetime import datetime
# fix for testing just this file
if __name__ == "__main__":

    import sys
    # Get the parent directory of the current script (api.py)
    CURR_DIR = os.path.dirname(os.path.abspath(__file__))

    # Add the parent directory to the Python path
    PARENT_DIR = os.path.join(CURR_DIR, "..")  # Go up one level from utils to project folder
    sys.path.append(PARENT_DIR)
from utils.api import API

class Unogs(API):
    @staticmethod
    def get_movie_info(type):
        params = {}
        params["type"] = f"{type}"
        url = "/search/titles"
        resp = API.get(url, params)
        
        # You might need to adjust the parsing logic based on the actual structure of the API response
        fixed = resp  # Assuming the structure of the response is already in the desired format
        
        return fixed
    
    

if __name__ == "__main__":
    # Assuming you have a utility function to handle API requests similar to the one used in the AlphaVantage example
    resp = Unogs.get_movie_info("series")
    print(resp)