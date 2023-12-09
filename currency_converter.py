import requests

API_KEY = 'fca_live_pm6Td8yVGA0vcaDTKIgZSKu5kZc8aplhKiJdQr8w'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURRENCIES = ["USD", "CAD", "EUR", "INR", "AUD", "CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Sorry,the requested currency is unavailable")
        return None
        
while True:
    base = input("Enter the Currency (q for quit): ").upper()

    if base == "Q":
        break
    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")
