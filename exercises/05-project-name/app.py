import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project1.php")

response_body = response.json()
if response.status_code == 200:
    name_response = response_body['name']
    print(name_response)
    
else:
    print('something went wrong')
