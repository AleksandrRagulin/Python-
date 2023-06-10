import sys
import requests
template = "http://numbersapi.com/"
params = {
    "json": "true"
}
arr = []
while True:
    _str = input()
    if _str:
        arr.append(_str)
    else:
        break

for tmp in arr:
    api_url = template + tmp + "/math"
    res = requests.get(api_url,params=params)
    if res.json()["found"]:
        print("Interesting")
    else:
        print("Boring")






