#!/usr/bin/env python
# coding: utf-8

# In[70]:


import json
from urllib.request import urlopen

with urlopen('http://livescore-api.com/api-client/scores/live.json?key=6r94GgdPiJ5ciqdx&secret=70Qx0KjZN2uD6jfdLohrFuhXem9wNm4U') as response:
    source = response.read()

data = json.loads(source)

print("Livescores : ")
for match in data['data']['match']:
    print(json.dumps(match, indent = 2))




# In[ ]:





# In[ ]:





# In[73]:



country_string = "Brazil" # Enter the name of the Country
with urlopen('http://livescore-api.com/api-client/countries/list.json?key=6r94GgdPiJ5ciqdx&secret=70Qx0KjZN2uD6jfdLohrFuhXem9wNm4U') as response:
    source2 = response.read()
data_2 = json.loads(source2)

country_id = ""
for ctr in data_2['data']['country']:
    #print (ctr['id'] , "  ", ctr['name'])
    if ctr['name'] == country_string:
        country_id = ctr['id']

str_url = "http://livescore-api.com/api-client/scores/live.json?key=6r94GgdPiJ5ciqdx&secret=70Qx0KjZN2uD6jfdLohrFuhXem9wNm4U&country="
str_url += country_id
request = urllib.request.Request(str_url)
response = urlopen(request)
source = response.read()
data_c = json.loads(source)

print("\n Brazil's livescores : ")

for m in data_c['data']['match']:
    print(json.dumps(m, indent = 2))


# In[59]:


fxt_url = "http://livescore-api.com/api-client/fixtures/matches.json?key=6r94GgdPiJ5ciqdx&secret=70Qx0KjZN2uD6jfdLohrFuhXem9wNm4U"

request = urllib.request.Request(fxt_url)
response = urlopen(request)
source = response.read()
data_f = json.loads(source)

print("tomorrow fixtures : ")
for fx in data_f['data']['fixtures'] :
    if fx['date'] == '2018-11-21' :
        print(json.dumps(fx, indent = 2))


# In[ ]:




