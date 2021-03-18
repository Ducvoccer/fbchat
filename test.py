import requests

r = requests.get('https://ncov.moh.gov.vn/', verify=False)

print(type(r.text))