import json

data = {'name': 'Sudarshan',
        'age': 24,
        'address': 'Koteshwor'}


json_data = json.dumps(data)

print("JSON Data: \n", json_data)

decoded_data = json.loads(json_data)

print("Decoded Data: \n", decoded_data)


