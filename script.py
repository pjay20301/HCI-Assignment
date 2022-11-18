import json

f = open('HCI.side')

data = json.load(f)

numClicks = 0

for i in data['tests']:
    for j in i['commands']:
            if(j['command'] == 'click'):
                numClicks += 1

print(numClicks)

f.close()