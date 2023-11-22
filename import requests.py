import requests
application = "amazon-pr"
URL = "https://aws.amazon.com/"

try:
    response = requests.head(URL)
except Exception as e:
    print(f"NOT OK: {str(e)}")
else:
    if response.status_code == 200:
        print (application) 
        print("OK") 
    else:
        print(f"NOT OK: HTTP response code {response.status_code}")

application = "GOOGLE-pr"
URL = "https://www.google.co.in/"

try:
    response = requests.head(URL)
except Exception as e:
    print(f"NOT OK: {str(e)}")
else:
    if response.status_code == 200:
        print (application) 
        print("OK") 
    else:
        print(f"NOT OK: HTTP response code {response.status_code}")        