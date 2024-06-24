import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")



if response.status_code == 200:
    print(response.text)
else:
    print("Something went wrong")