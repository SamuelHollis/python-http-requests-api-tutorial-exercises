import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
print(response.text)

date = response.json()

hour = date['hours']
minutes = date['minutes']
seconds = date['seconds']

if response.status_code == 200:
    print(f"Current time: {hour}hrs {minutes}min {seconds}sec")
    
else:
    print('something went wrong')

