import requests

from_currency = "USD"
to_currency = "EUR"
amount = 10

url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"

try:
    response = requests.get(url, timeout=5)
    data = response.json()
    print("API Response:", data)
except Exception as e:
    print("Request failed:", e)
