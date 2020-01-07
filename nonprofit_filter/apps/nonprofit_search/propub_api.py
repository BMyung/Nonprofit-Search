import requests
import json

response = requests.get('https://projects.propublica.org/nonprofits/api/v2/search.json?q=Anaheim&state%5Bid%5D=CA&ntee%5Bid%5D=2&c_code%5Bid%5D=3')

count = 0 
for i in range(0,70):
    charities = response.json()
    if charities["organizations"][i]["city"] == 'ANAHEIM':
        count +=1
        print(count)
        print(charities["organizations"][i]["name"])
    if count == 20:
        break