import json

with open('json_example.json', encoding='utf8') as f:
    strfile = f.read()
    templates = json.loads(strfile)

print(json.dumps(templates, indent=4))
#print(templates)
print(type(templates))