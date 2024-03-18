import json

with open('json_example.json', encoding='utf8') as f:
    strfile = f.read()
    templates = json.loads(strfile)

print(templates)
print(type(templates))

