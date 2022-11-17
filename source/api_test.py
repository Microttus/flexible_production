'''
Flexible production MAS5417 project
APIWether class
Martin Økter
25.10.2022
'''
import numpy as np
import requests

# Insert your own client ID here
client_id = 'd5398c91-5891-4c26-b199-990eebd37174'


# Define endpoint and parameters
endpoint = 'https://frost.met.no/observations/v0.jsonld'
geoendpoint = 'https://frost.met.no/sources/v0.jsonld'

Lat = 8.3540  #Input from User interface, Need some restrictions
Long = 58.2250   #Input from User interface, Need some restrictions

#POINT(8.3540 58.2250)

geoparameters = {
    'geometry': f'nearest(POINT({Lat} {Long}))'
}

# Issue an HTTP GET request
s = requests.get(geoendpoint, geoparameters, auth=(client_id, ''))
# Extract JSON data
geo_json = s.json()


loc_data = geo_json['data']
loc_id = loc_data[0]['id']
print(loc_data[0]['id'])
print(loc_data[0]['name'])
#print(loc_data) #To see whats inside

id_str = str(loc_id)

parameters = {
    'sources': id_str,
    'elements': 'mean(air_temperature P1D)',
    'referencetime': '2021-06-01/2022-06-01',
}

r = requests.get(endpoint, parameters, auth=(client_id,''))
temp_json = r.json()
#print(temp_json)
if r.status_code == 200:
    temp_data = temp_json['data']
    #print(temp_data)
    print('Data retrieved from frost.met.no!')
else:
    print('Error! Returned status code %s' % r.status_code)
    print('Message: %s' % temp_json['error']['message'])
    print('Reason: %s' % temp_json['error']['reason'])


#print(temp_data[0]['observations'][0]['value'])
#print(temp_data)


lenght = len(temp_data)
allTemp = []

for i in range(0, lenght):
    Temp = (temp_data[i]['observations'][0]['value'])
    #meanTemp = np.array(Temp)
    allTemp.append(Temp)

meanTemp = np.mean(allTemp)
print(meanTemp)
