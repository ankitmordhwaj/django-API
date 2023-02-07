import requests
import json

url = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}

    json_data = json.dumps(data)
    r = requests.get(url= url, data= json_data)
    data = r.json()
    print(data)

def post_data():
    data = {
        'name': 'Anoop',
        'roll': '102',
        'city': 'UP'
    }
    json_data = json.dumps(data)
    r = requests.post(url=url, data= json_data)
   
    print(r.json())

def update_data():
    data = {
        'id': 8,
        'city': 'Gurgaon'
    }
    json_data = json.dumps(data)
    r = requests.put(url=url, data= json_data)
   
    print(r.json())

def delete_data():
    data = {
        'id': 16    }
    json_data = json.dumps(data)
    r = requests.delete(url=url, data= json_data)
   
    print(r.json())

# user_id = input("Enter ID: ")
# get_data(user_id )

# post_data()

# update_data()

delete_data()