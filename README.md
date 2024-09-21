# Gorest API Automation with Python

This repository demonstrates API automation for interacting with the [Gorest API](https://gorest.co.in). It includes sample scripts for performing **GET**, **POST**, **PUT**, and **DELETE** requests using Python's `requests` library and JSON data.

## Functionality

The script covers the following operations:

1. **GET**: Fetch all users.
2. **POST**: Create a new user with a randomly generated name and email.
3. **PUT**: Update the user data (change email and status).
4. **DELETE**: Delete the created user.
5. **Verification**: Ensure that the deleted user no longer exists.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- `requests` library

You can install the required package using `pip`:

```bash
pip install requests

How to Use

    Clone this repository:

    bash

git clone https://github.com/yourusername/gorest-api-automation.git

Set up your Authentication Token in the script:

    Replace the auth_token variable with your Gorest API token:

    python

    auth_token = "Bearer YOUR_AUTH_TOKEN_HERE"

Run the script:

bash

    python api_automation.py

Files Overview

    api_automation.py: The main script containing all functions for API operations and testing.
    generate_random_email(): Generates a random email for testing purposes.
    generate_random_name(): Randomly generates a user name from a predefined list.

API Operations

    GET Request: Fetches all users from the API.

    python

get_request()

POST Request: Creates a new user with randomly generated credentials.

python

user_id, name_check = post_request()

PUT Request: Updates the newly created user's email and status.

python

put_request(user_id, name_check)

DELETE Request: Deletes the user created in the POST request.

python

delete_request(user_id)

Check Deletion: Verifies that the user has been deleted.

python

    get_deleted_user(user_id)

Important Notes

    Security Warning: Handle your API token carefully. Avoid sharing or exposing it in public repositories.
    Educational Use Only: This code is for learning and testing purposes. Ensure you comply with Gorest's API usage policies.
