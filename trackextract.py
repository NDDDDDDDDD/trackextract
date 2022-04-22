import requests
from collections import Counter
import json

urls = open('urls.txt')
urls = urls.readlines()
items = []
thirdparty = []

for i in urls:
    i = i.replace("\n","")
    items.append(i)
for l in items:
    r = requests.post('https://blacklight.api.themarkup.org/', json ={'inUrl': f'https://{l}'})
    if r.status_code == requests.codes.ok:
        r = json.loads(r.text)
        if "status': 'success'" in str(r):
            r = r['hosts']
            r = r['requests']
            r = r['third_party']
            for line in r:
                print(line.replace("www.",""))
                thirdparty.append(line)
            c = Counter(thirdparty)
        else:
            pass
    else:
        pass
c = Counter(thirdparty)
c = str(c)
c = c.split("'")
title = input("\nEnter file name: ")
for line in c:
    line = line.replace(' ', '')
    line = line.replace('"[', '')
    line = line.replace("'","")
    line = line.replace("(", "")
    line = line.replace("www.", "")
    if "." in line:
        with open(f'{title}.txt', 'a') as file:
            file.write(f'{line}\n')
    else:
        pass
