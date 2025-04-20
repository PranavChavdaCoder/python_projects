import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    response = requests.get(url)
    data = response.json()

    converted = data['rates'][to_currency]
    print(f"{amount} {from_currency} = {converted} {to_currency}")

# User Input
print("Welcome to Currency Converter!")
amount = float(input("Enter amount: "))
from_curr = input("From currency (e.g., USD): ").upper()
to_curr = input("To currency (e.g., INR): ").upper()

convert_currency(amount, from_curr, to_curr)
