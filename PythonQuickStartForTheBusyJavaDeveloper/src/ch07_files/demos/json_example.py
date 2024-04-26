import json

data = {"TIM": {"name": "Tim", "age": 50, "city": "Kiel"},
        "MIKE": {"name": "Mike", "age": 50, "city": "Zürich"},
        "INFO": ["This", "is", "an", "information"],
        "CHECKSUM": 4711}

with open('data.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

with open('data.json') as json_file:
    data = json.load(json_file)
    print(data)
