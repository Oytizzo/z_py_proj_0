import requests
import json


class BBAnswerKey:
    def __init__(self, server, email, password, username="string", auth_token="string"):
        self.server = server
        login_url = f"{self.server}/api/UserLogin/BBLoginNew"
        payload = json.dumps({
            "username": "string",
            "password": password,
            "email": email,
            "auth_token": "string"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", login_url, headers=headers, data=payload)
        self.auth_token = response.json().get("data").get("Auth_Token")

    def BBLoginNew(self, email, password, username="string", auth_token="string"):
        login_url = f"{self.server}/api/UserLogin/BBLoginNew"
        payload = json.dumps({
            "username": "string",
            "password": password,
            "email": email,
            "auth_token": "string"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", login_url, headers=headers, data=payload)
        self.auth_token = response.json().get("data").get("Auth_Token")

        return json.dumps(response.json(), indent=4)

    def GetDigitalKeyBook(self, subject, level, week):
        url = f"{self.server}/api/AnswerKey/GetDigitalKeyBook?subject={subject}&level={level}&week={week}"
        payload = {}
        headers = {
            'Authorization': f'Bearer {self.auth_token}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)


        # return response.text
        return json.dumps(response.json(), indent=4)


if __name__ == "__main__":
    test_server = ""
    dev_server = ""
    prod_server = ""

    bba = BBAnswerKey(server=prod_server, email="test@example.com", password="pass#2")
    print(bba.GetDigitalKeyBook(subject="English", level="Level O1", week="26-Z Test"))
