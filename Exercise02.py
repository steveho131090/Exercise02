import json
import pandas as pd
import time
import base64
import re
import requests
url = 'https://raw.githubusercontent.com/IOTechSystems/exercises/main/exercise-02/data/data.json'
urlOutPut = 'https://raw.githubusercontent.com/IOTechSystems/exercises/main/exercise-02/output-schema/schema.json'

tempUrl = requests.get(url)
data = tempUrl.json()
tempUrlOutPut = requests.get(urlOutPut)
outJson = tempUrlOutPut.json()
now = int(time.time())

valueTotal = 0
uuidArr = []

for idx, obj in enumerate(data['Devices']):
    if int(obj['timestamp']) < now:
        data['Devices'].remove(obj)

for obj in data['Devices']:
    valueTotal += int(base64.b64decode(obj['value']))
    uuid = re.split(':|, ', obj['Info'])
    uuidArr.append(uuid[1])

outJson['required'][0] = 'ValueTotal', str(valueTotal)
outJson['required'][1] = 'uuid', uuidArr

with open(r'C:\Users\steve\Desktop\outJson.json', 'w') as temp:
    json.dump(outJson, temp)
