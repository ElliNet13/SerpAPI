import os
import requests
import json
from sys import exit

# Define the cache folder
cache_folder = "serpapi_cache"

# Create the cache folder if it doesn't exist
if not os.path.exists(cache_folder):
    os.makedirs(cache_folder)

# Fetch API key from environment variable
api_key = os.getenv("SERPKEY")

def get_search_results(search_query):
    # Check if the cache file exists
    cache_file = os.path.join(cache_folder, f"{search_query}.json")
    if os.path.exists(cache_file):
        # If cache file exists, load the data from it
        with open(cache_file, "r") as f:
            data = json.load(f)
    else:
        # If cache file doesn't exist, fetch data from SerpAPI
        url = f"https://serpapi.com/search.json?q={search_query}&api_key={api_key}"
        response = requests.get(url)
        data = response.json()
        # Cache the data by saving it to a file
        with open(cache_file, "w") as f:
            json.dump(data, f)
    return data

search_query = input("Get question about: ")
data = get_search_results(search_query)

# Extract the first link from the search results
try:
 first_link = data["related_questions"][0]["question"]
except:
 first_link = "No related questions found...\nSo here's an ad instead: " + data["ads"][0]["title"]
 print(first_link)
 exit()

print("First question:", first_link)
input("Press enter to see answer... ")
print(data["related_questions"][0]["snippet"])