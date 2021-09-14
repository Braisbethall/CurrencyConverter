import requests
import json


currency_code = input()
json_r = requests.get(f"http://www.floatrates.com/daily/{currency_code}.json")
json_file = json_r.text
py_object = json.loads(json_file)
cache = dict()
if currency_code in ("USD", "usd"):
    cache["eur"] = py_object["eur"]
elif currency_code in ("EUR", "eur"):
    cache["usd"] = py_object["usd"]
else:
    cache["usd"] = py_object["usd"]
    cache["eur"] = py_object["eur"]
while True:

    if cache == py_object:
        break
    currency_code_to_receive = input()
    amount_of_money = float(input())
    print("Checking the cache...")
    if currency_code_to_receive in cache:
        print("Oh! It is in the cache!")
        value = py_object[currency_code_to_receive.lower()]
        rate = value["inverseRate"]
        print(f"You received {round(amount_of_money / rate, 2)} {currency_code_to_receive.upper()}.")
    else:
        print("Sorry, but it is not in the cache!")
        cache[currency_code_to_receive.lower()] = py_object[currency_code_to_receive.lower()]
        value = py_object[currency_code_to_receive.lower()]
        rate = value["inverseRate"]
        print(f"You received {round(amount_of_money / rate, 2)} {currency_code_to_receive}.")
print(py_object)
print(cache)
