"""
The User module for ruby.py.
"""
import requests
from .Client import Client
from .WeightData import WeightData


class User:
    def __init__(self, username, passcode):
        self.login = Client._login(username, passcode)
        self.base = "https://ruby-weight-management.herokuapp.com"

    def get_weight(self, month):
        assert type(month) is str, "'month' must be either '-' or in xxxx-xx format."

        response = requests.get(f"{self.base}/api/weight/{month}/", auth=self.login)

        return WeightData(response.json())

    def update_weight(self, weight: float):
        assert type(weight) is float or type(weight) is int, "'weight' must be a number."

        data = {
            "user_id": self.login.username,
            "weight": str(weight)
        }

        response = requests.post(f"{self.base}/api/update-weight/", auth=self.login, json=data)

        return WeightData(response.json())
