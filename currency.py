import requests

API_KEY = 'fca_live_dUj6R8DfIcRZrjq2NwTJqHZv3Q3NY5WYds0pgOXV'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "JPY", "EUR","BRL" ]

def convert_currency (base):
    currencies= ",".join(CURRENCIES)
    url= f"{BASE_URL}&base_currency={base}&currencies={currencies}"   
    try :
        response= requests.get(url) 
        data = response.json()
        return data["data"]
    except:
        print("invalid currency")
        return None

while True:
    base=input("what curency would you like to convert? (q for quit): ").upper()
    if base =="Q":
        break
    data = convert_currency(base)
    if not data:
        continue
    del data[base]
    for ticker, value in data.items():
      print(f"{ticker}: {value}")