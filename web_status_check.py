import requests

def check_website_status(url):
  try:
    response = requests.get(url)
    return response.status_code
  except requests.exceptions.RequestException as e:
    return None

def main():
  websites = ["https://aws.amazon.com/", "https://aws.amazon.com/css"]

  for website in websites:
    status_code = check_website_status(website)
    if status_code is None:
          print(f"{website} is down.")
    elif status_code == 200:
      print(f"{website} is up and running.")
    else:
      print(f"{website} is returning a status code of {status_code}.")

if __name__ == "__main__":
  main()