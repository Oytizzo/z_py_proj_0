import requests
import os
import configparser

config = configparser.ConfigParser()
config.read(r'C:\Users\User\Desktop\private.conf')

grader_username = config.get('bb', 'grader_username')
grader_password = config.get('bb', 'grader_password')
# api_server = sr.Get_Shared_Variables("ApiServer")
# response_grader_login = sr.Get_Shared_Variables("response_grader_login")
# data = sr.Get_Shared_Variables("req_body_grader_submit_page")

api_server = config.get('bb', 'api_server')

url_grader_login = f"{api_server}/api/Auth/Login"
req_body_grader_login = {
    "username": grader_username,
    "password": grader_password
}
response_grader_login = requests.post(url_grader_login,
                                      json=req_body_grader_login).json()

grader_id = response_grader_login["data"]["userID"]
token = response_grader_login["data"]["token"]
url_grader_get_page = f"{api_server}/api/Grader/GetPage?Id={grader_id}"
url_grader_submit_page = f"{api_server}/api/Grader/SubmitPage"
list_of_pages_graded_in_this_session = []
count = 0

print("="*50)
while True:
    response_grader_get_page = requests.get(url=url_grader_get_page,
                                            headers={"Authorization": f"Bearer {token}"})
    response_grader_get_page_json = response_grader_get_page.json()

    print(f"GetPage => {response_grader_get_page_json}")

    if response_grader_get_page_json["data"] is None and \
            response_grader_get_page_json["message"] == "No data found." and \
            response_grader_get_page_json["errorCode"] == 204:
        print("-"*50)
        print("No more page!")
        break

    req_body_grader_submit_page = {
        "UserId": grader_id,
        "StudentID": response_grader_get_page_json['data']['studentID'],
        "BookPageId": response_grader_get_page_json['data']['bookPageId'],
        "NoOfQuestions": 5,
        "NoOfCorrectAnswered": 4
    }

    image_url = response_grader_get_page_json['data']['submittedPagePath']

    image_data = requests.get(image_url).content

    # send the POST request with the image file
    response_grader_submit_page = requests.post(url_grader_submit_page,
                                                headers={"Authorization": f"Bearer {token}"},
                                                data=req_body_grader_submit_page,
                                                files={"SubmittedFiles": ('image.jpg', image_data)})
    response_grader_submit_page_json = response_grader_submit_page.json()
    print("-" * 50)
    print(f"SubmitPage => {response_grader_submit_page_json}")
    # check the response status code
    if response_grader_submit_page.status_code == requests.codes.ok and \
            response_grader_submit_page_json["message"] == "success.":
        count += 1
        graded_page = {"count": count,
                       'response_grader_GetPage': response_grader_get_page_json,
                       'response_grader_SubmitPage': response_grader_submit_page_json}
        list_of_pages_graded_in_this_session.append(graded_page)
        print('Image uploaded successfully!')
        print("-"*50)
        print(graded_page)
    else:
        print('Error uploading image')
    print("="*50)
# sr.Set_Shared_Variables("http_response", response_grader_submit_page_json)
