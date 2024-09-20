import requests 
import random
import json
import string

# Base URL 
base_url = "https://gorest.co.in"

# Authentication Token 
auth_token = "Bearer dcbf5d16c6a97aaf3eeaa873c411c8edf18d6673edba15ee65ed2c03ba6f20ca"

# GET Request
def get_request():
    url = base_url + "/public/v2/users/7413580"
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    print(f"json response body: {json_data}")

# POST Request 

# PUT Request 

# DELETE Request

# Calling the requests
get_request()