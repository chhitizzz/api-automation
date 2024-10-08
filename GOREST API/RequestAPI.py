import random
import requests
import json
import string

# Base URL 
base_url = "https://gorest.co.in"

# Authentication Token 
auth_token = "Bearer dcbf5d16c6a97aaf3eeaa873c411c8edf18d6673edba15ee65ed2c03ba6f20ca"

# Generate random email id
def generate_random_email():
    domain = "test.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

# Using a static list of names
names_list = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Helen", "Ivy", "Jack"]

def generate_random_name():
    name = ' '.join(random.sample(names_list, 2))  # Randomly pick two names
    return name

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
        "name": generate_random_name(),
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print(f"json POST response body: {json_str}")
    user_id = json_data["id"]
    name_check = json_data["name"]
    return user_id, name_check  # Return both user_id and name_check

# PUT Request 
def put_request(user_id, name_check):
    url = base_url + f"/public/v2/users/{user_id}"
    print(f"PUT Request URL: {url}")
    headers = {"Authorization": auth_token}
    data = {
        "name": name_check,  # Use the original name (name_check) for validation
        "email": generate_random_email(),
        "gender": "male",
        "status": "inactive"
    }
    response = requests.put(url, json=data, headers=headers)

    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print(f"json PUT response body: {json_str}")
    assert json_data["id"] == user_id
    assert json_data["name"] == name_check  # Assert that the name hasn't changed

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
get_request()
user_id, name_check = post_request()  # Store both user_id and name_check
put_request(user_id, name_check)
delete_request(user_id)
get_deleted_user(user_id)
