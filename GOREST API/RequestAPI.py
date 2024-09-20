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
    url = base_url + "/public/v2/users/"
    print(f"GET Request URL: {url}")
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print(f"json response body: {json_str}")

# POST Request 
def post_request():
    url = base_url + "/public/v2/users/"
    print(f"POST Request URL: {url}")
    headers = {"Authorization": auth_token}
    data = {
        "name": "API Automation",
        "email": "testautomation@test.com",
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print(f"json response body: {json_str}")
    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == "API Automation"
    return user_id 

# PUT Request 
def put_requests():
    url = base_url + "/public/v2/users/"
    print(f"POST Request URL: {url}")
    headers = {"Authorization": auth_token}
    data = {
        "name": "API Automation",
        "email": "testautomation@test.com",
        "gender": "male",
        "status": "active"
    }


# DELETE Request

# Calling the requests
# get_request()
post_request()