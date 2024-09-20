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
    print(f"json GET response body: {json_str}")

# POST Request 
def post_request():
    url = base_url + "/public/v2/users/"
    print(f"POST Request URL: {url}")
    headers = {"Authorization": auth_token}
    data = {
        "name": "API Automation",
        "email": "automate2@test.com",
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print(f"json POST response body: {json_str}")
    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == "API Automation"
    return user_id 

# PUT Request 
def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print(f"PUT Request URL: {url}")
    headers = {"Authorization": auth_token}
    data = {
        "name": "API Automation Labs",
        "email": "testautomationlabs332@auto.com",
        "gender": "male",
        "status": "inactive"
    }
    response = requests.put(url, json=data, headers=headers)

    # Debugging
    # print(f"PUT Response status code: {response.status_code}")
    # print(f"Response body: {response.text}")

    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print(f"json PUT response body: {json_str}")
    assert json_data["id"] == user_id
    assert json_data["name"] == "API Automation Labs"


# DELETE Request
def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print(f"DELETE Request URL: {url}")
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204 
    print("------ USER HAS BEEN DELETED ------")

# Checking if the user is deleted or not
def get_deleted_user(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print(f"GET Request URL: {url}")
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 404
    print(f"------ RESOURCE NOT FOUND ------")

# Calling the requests
# get_request()
user_id = post_request()
# put_request(user_id)
delete_request(user_id)
get_deleted_user(user_id)