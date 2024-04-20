import requests
import sys
import json
import time


# to notify ie send email change the url to users?notify=true
def add_user(url, session, user_data):
  r = session.post(
      f"{url}/api/v1/users?notify=true",
      json=user_data,
      headers={"Content-Type": "application/json"},
  )
  print(r.json())


def main():
  try:
    url = "https://iutctf.xyz"
    token = "ctfd_7c016dbe3b30e301e2862697801dab99c70c845906018e9519f7ee2a3a46dd24"
    json_file = sys.argv[1]
  except IndexError:
    print("Usage: python3 add_user.py <file.json>")
    sys.exit(1)

  url = url.strip("/")
  s = requests.Session()
  s.headers.update({"Authorization": f"Token {token}"})

  with open(json_file, 'r') as file:
    users = json.load(file)

  for user in users:
    add_user(url, s, user)
    time.sleep(1)


if __name__ == "__main__":
  main()
