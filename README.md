GoRest API Automation

This project demonstrates an automated testing script to interact with the GoRest API using Python. The script performs basic CRUD operations (Create, Read, Update, and Delete) on user resources. It uses Python's requests library to send HTTP requests to the API and validate the responses.
Features

    GET Users: Fetches and displays the list of users from the GoRest API.
    POST User: Creates a new user with a randomly generated name and email.
    PUT User: Updates the created user’s status to inactive and validates the changes.
    DELETE User: Deletes the created user and verifies successful deletion.
    Check Deletion: Verifies that the deleted user no longer exists.

Requirements

    Python 3.x
    requests library

You can install the requests library using pip:

bash

pip install requests

Setup

    Clone the repository:

bash

git clone https://github.com/yourusername/gorest-api-automation.git

    Navigate to the project directory:

bash

cd gorest-api-automation

    Add your authentication token inside the code or set it as an environment variable.

Usage
Running the Script

This script is divided into the following sections:

    get_request(): Fetches and prints the list of users.
    post_request(): Creates a new user with randomly generated details and returns the user_id.
    put_request(user_id, name_check): Updates the created user's status to inactive and ensures the name remains unchanged.
    delete_request(user_id): Deletes the created user using the user_id.
    get_deleted_user(user_id): Verifies that the user has been deleted by attempting to fetch the deleted user.

To execute the script:

bash

python automation.py

Example Workflow

    Fetches a list of users from the GoRest API.
    Creates a new user with a randomly generated name and email.
    Updates the newly created user’s status to inactive.
    Deletes the created user.
    Verifies that the deleted user no longer exists.
