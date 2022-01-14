"""
The Client for the Ruby API.

This will provide the login for Basic HTTP authentication.
"""
import requests
from requests.auth import HTTPBasicAuth
from .User import User
from typing import Optional


class Client:
    @staticmethod
    def _login(username: str, passcode: str):
        return HTTPBasicAuth(username, passcode)

    @staticmethod
    def new_user(user_id: str, passcode: int) -> Optional[User]:
        data = {
            "user_id": user_id,
            "passcode": str(passcode)
        }

        response = requests.post("https://ruby-weight-management.herokuapp.com/api/new-user/", json=data)

        assert "SUCCESS" in response.json()['message'], f"User cannot be created. Here's the server message:\n{response.json()['message']}"

        return User(user_id, passcode)


