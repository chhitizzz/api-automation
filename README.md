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
```

## How to Use

1. Clone this repository:

```bash

git clone https://github.com/yourusername/gorest-api-automation.git
```

2. Set up your Authentication Token in the script:

    Replace the auth_token variable with your Gorest API token:
```bash 
    auth_token = "Bearer YOUR_AUTH_TOKEN_HERE"
```

3. Run the script:

```bash

    python RequestAPI.py
```

## Files Overview

1. RequestAPI.py: The main script containing all functions for API operations and testing.
2. generate_random_email(): Generates a random email for testing purposes.
3. generate_random_name(): Randomly generates a user name from a predefined list.
   
