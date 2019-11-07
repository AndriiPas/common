import json


def get_data(value):
    with open("data.json") as file:
        for i in json.load(file):
            if value == i['title']:
                return i
