"""
The Client for the Ruby API.

This will provide the login for Basic HTTP authentication.
"""
import requests
from requests.auth import HTTPBasicAuth


class Client:
    @staticmethod
    def _login(username: str, passcode: str):
        return HTTPBasicAuth(username, passcode)

    @staticmethod
    def new_user(user_id: str, passcode: int) -> str:
        data = {
            "user_id": user_id,
            "passcode": str(passcode)
        }

        response = requests.post("https://ruby-weight-management.herokuapp.com/api/new-user/", json=data)

        print(response.text)
        return response.json()['message']


