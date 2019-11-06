import json


def get_data(value):
    with open("/home/andrii/HW/common/flask_hw3/data.json") as file:
        for i in json.load(file):
            if value == i['name']:
                return i

def get_len():
    array = []
    with open("/home/andrii/HW/common/flask_hw3/data.json") as file:
        for i in json.load(file):
            array.append(i['name'])
    return array

#print(get_data("potato"))
#print(get_len())