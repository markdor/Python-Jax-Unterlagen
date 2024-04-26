import json

data = {"LARRY": {
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
}, "TIM": {
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'California'
}, "MIKE": {
    'name': 'Mike',
    'website': 'JavaProfi.com',
    'from': 'Zurich'
}
}

with open('response-data.json', 'w') as outfile:
    json.dump(data, outfile)

with open('response-data.json') as json_file:
    data = json.load(json_file)
    for p in data.values():
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
