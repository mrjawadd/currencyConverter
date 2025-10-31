from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "9997e0c481e68d274858e578a1174a38"  # Your API key

# List of 50+ major currencies
currency_codes = [
    "USD","EUR","GBP","JPY","AUD","CAD","CHF","CNY","INR","NZD",
    "SGD","HKD","SEK","KRW","NOK","MXN","BRL","ZAR","TRY","RUB",
    "MYR","THB","IDR","PHP","PLN","DKK","HUF","CZK","ILS","CLP",
    "PKR","AED","SAR","COP","EGP","VND","BDT","NGN","KWD","QAR",
    "LKR","OMR","KES","TWD","UAH","BGN","RON","ISK","MAD","JOD"
]

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert?access_key={API_KEY}&from={from_currency}&to={to_currency}&amount={amount}"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("success") and "result" in data:
            return round(data["result"], 2)
        else:
            return None
    except requests.exceptions.RequestException:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    converted_amount = None
    if request.method == 'POST':
        amount = request.form.get('amount')
        from_curr = request.form.get('from_currency')
        to_curr = request.form.get('to_currency')

        if not amount or not from_curr or not to_curr:
            converted_amount = "Please fill in all fields."
        else:
            try:
                amount = float(amount)
                result = convert_currency(amount, from_curr, to_curr)
                if result is not None:
                    converted_amount = f"{amount} {from_curr} = {result} {to_curr}"
                else:
                    converted_amount = "Conversion failed. Check currency codes or your internet."
            except ValueError:
                converted_amount = "Please enter a valid number."
    
    return render_template('index.html', result=converted_amount, currencies=currency_codes)

if __name__ == "__main__":
    app.run(debug=True)
