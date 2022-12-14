def clean_name(name):
    return "".join([c for c in name if c.isalpha()])


def get_username(sender_id):
    import requests
    import os
    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getChat"
    body = {"chat_id": sender_id}
    response = requests.post(url, data=body)
    response = response.json()
    name = response["result"]["first_name"]
    return name

def req_json(endpoint):
    import requests
    url = f"http://sci/api/{endpoint}"
    payload = ""
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()
    return response


def last_info(data=None, dictionary=None):

    attributes = list(dictionary.keys())
    values = list(dictionary.values())

    req = []
    if len(attributes) == 1:
        req = [x for x in data
               if x[attributes[0]] in values[0]
               ]
    elif len(attributes) == 2:
        req = [x for x in data
               if x[attributes[0]] in values[0]
               and x[attributes[1]] in values[1]
               ]
    elif len(attributes) == 3:
        req = [x for x in data
               if x[attributes[0]] in values[0]
               and x[attributes[1]] in values[1]
               and x[attributes[2]] in values[2]
               ]

    elif len(attributes) == 4:
        req = [x for x in data
               if x[attributes[0]] in values[0]
               and x[attributes[1]] in values[1]
               and x[attributes[2]] in values[2]
               and x[attributes[3]] in values[3]
               ]
    elif len(attributes) == 5:
        req = [x for x in data
               if x[attributes[0]] in values[0]
               and x[attributes[1]] in values[1]
               and x[attributes[2]] in values[2]
               and x[attributes[3]] in values[3]
               and x[attributes[4]] in values[4]
               ]

    return req[0]


def all_info(data=None, dictionary=None):

    attributes = list(dictionary.keys())
    values = list(dictionary.values())

    req = []
    if len(attributes) == 1:
        req = [x for x in data
               if x[attributes[0]] in values[0]
               ]
    elif len(attributes) == 2:
        req = [x for x in data
               if x[attributes[0]] in values[0]
               or x[attributes[1]] in values[1]
               ]
    elif len(attributes) == 3:
        req = [x for x in data
               if x[attributes[0]] in values[0]
               or x[attributes[1]] in values[1]
               or x[attributes[2]] in values[2]
               ]

    elif len(attributes) == 4:
        req = [x for x in data
               if x[attributes[0]] in values[0]
               or x[attributes[1]] in values[1]
               or x[attributes[2]] in values[2]
               or x[attributes[3]] in values[3]
               ]
    elif len(attributes) == 5:
        req = [x for x in data
               if x[attributes[0]] in values[0]
               or x[attributes[1]] in values[1]
               or x[attributes[2]] in values[2]
               or x[attributes[3]] in values[3]
               or x[attributes[4]] in values[4]
               ]

    return req
