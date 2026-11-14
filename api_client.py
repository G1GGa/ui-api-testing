import requests

class APIClient:
    def __init__(self, base_url:str):
        self.base_url = base_url

    def get_user(self, user_id: int):
        url = f"{self.base_url}/users/{user_id}"
        response = requests.get(url)
        return response

    def create_post(self, title:str, body:str, user_id: int):
        url = f"{self.base_url}/posts"
        payload = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        response = requests.post(url, json=payload)
        return response