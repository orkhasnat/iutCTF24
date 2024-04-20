import csv
import json

def csv_to_json(csv_file):
    users = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, fieldnames=['name', 'email', 'password'])
        for row in reader:
            user_data = {
                "name": row['name'],
                "email": row['email'],
                "password": row['password'],
                "type": "user",
                "verified": True,
                "hidden": False,
                "banned": False,
                "fields": []
            }
            users.append(user_data)
    return users

def main():
    csv_file = 'users.csv'
    json_data = csv_to_json(csv_file)
    with open('users.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

if __name__ == "__main__":
    main()
