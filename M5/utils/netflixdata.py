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

        all_results = []
        if "results" in resp:
            results = resp["results"]

            # Loop through all results
            for result in results:
                # Rename keys and replace spaces with underscores
                fixed = {}
                for k, v in result.items():
                    if "." in k:
                        k = k.split(".")[1].strip()
                    fixed[k.replace(" ", "_")] = v

                all_results.append(fixed)

        return all_results
    
        # if "results" in resp:
        #     results = resp["results"]

        #     # Extract the first result (assuming it's a dictionary)
        #     if results and isinstance(results, list):
        #         first_result = results[0]

        #         # Rename keys and replace spaces with underscores
        #         fixed = {}
        #         for k, v in first_result.items():
        #             if "." in k:
        #                 k = k.split(".")[1].strip()
        #             fixed[k.replace(" ", "_")] = v

        #         return fixed

        # return {}

if __name__ == "__main__":
    # Assuming you have a utility function to handle API requests similar to the one used in the AlphaVantage example
    resp = Unogs.get_movie_info("series")
    for result in resp:
        print(result)
