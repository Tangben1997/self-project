import json

IPinfo = [
    {
        'add': '123.0.4.2',
        'port': '2019'
    },
    {
        'add': '127.0.0.1',
        'port': '5552'
    }
]

json_str=json.dumps(IPinfo)

print(type(json_str))
print(json_str)