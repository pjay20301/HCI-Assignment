import json

f = open('newirctc.side')

data = json.load(f)

numClicks = 0
numMouseOver = 0
numMouseout = 0
numSearch = 0
for i in data['tests']:
    for j in i['commands']:
            if(j['command'] == 'click'):
                numClicks += 1
                if((".primaryBtn" in j['target']) or (".train_Search" in j['target']) or ("BE_train_search_btn" in j['target'])):
                    numSearch += 1
            elif(j['command'] == 'mouseOver'):
                numMouseOver += 1   
            elif(j['command'] == 'mouseOut'):
                numMouseout += 1
            

print(numClicks)
print(numMouseOver)
print(numMouseout)
print(numSearch)

f.close()