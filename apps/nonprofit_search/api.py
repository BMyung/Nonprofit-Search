import requests
import json
import random

headers = {
    'Accept': 'application/json',
}
params = (
    ('app_id', '01f4f7f1'),
    ('app_key', 'ec2821aebc8a6c15029c9fc2b5b7e147'),
)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://api.data.charitynavigator.org/v2/Categories, headers=headers, params = params)

pro_response = requests.get('https://projects.propublica.org/nonprofits/api/v2/organizations/204562686.json')
pro_nonprofit = pro_response.json()
for i in range(0,3):
        rev_i = pro_nonprofit['filings_with_data'][i]['totrevenue']
        exp_i = pro_nonprofit['filings_with_data'][i]['totfuncexpns']
        total_i = rev_i - exp_i
        print(i)
        print(total_i)