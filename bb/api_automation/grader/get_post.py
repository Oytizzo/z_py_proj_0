import requests

# set the URL of the endpoint
url_grader_get_page = sr.Get_Shared_Variables("url_grader_get_page")
url_grader_submit_page = sr.Get_Shared_Variables("url_grader_submit_page")

# set the Bearer Authorization token
token = f'Bearer {sr.Get_Shared_Variables("grader_token")}'

# set the headers
headers = {'Authorization': token}

max_submit_page = 100
submit_page_count = 0


def grader_get_page(url, headers):
    pass


def grader_submit_page(url, headers, body):
    pass


while True:
    # Todo: send the GET request with the headers
    response_of_get_page = requests.get(url_grader_get_page, headers=headers)
    json_response_of_get_page = response_of_get_page.json()
    print(json_response_of_get_page)

    # Todo: check the response status code
    if response_of_get_page.status_code == 200:
        # Todo: process the response data
        req_body_grader_submit_page = {
          "UserId": json_response_of_get_page['data']['userID'],
          "StudentID": json_response_of_get_page['data']['studentID'],
          "BookPageId": json_response_of_get_page['data']['bookPageId'],
          "NoOfQuestions": 5,
          "NoOfCorrectAnswered": 4
        }
        image_url = json_response_of_get_page['data']['submittedPagePath']
        image_data = requests.get(image_url).content
        # print(url_grader_submit_page, token, json_response_of_get_page, image_url)

        # Todo: send the POST request with image file for submitpage url
        response_submit_page = requests.post(url=url_grader_submit_page,
                                             headers=headers,
                                             data=req_body_grader_submit_page,
                                             files={"SubmittedFiles": ('image.jpg', image_data)})

        # Todo: check the response status code
        if response_submit_page.status_code == requests.codes.ok:
            print('Image uploaded successfully!')
            submit_page_count += 1
        else:
            print('Error uploading image')

        sr.Set_Shared_Variables("http_response", response_submit_page.json())

    elif response_of_get_page.status_code == 204:
        data = response.json()
    else:
        print('Error getting data')
