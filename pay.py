import requests

API_URL = "https://api.strike.me/v1/payments"
API_KEY = "your_strike_api_key"

def ssend_payment(amount, recipient):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "amount": amount,
        "recipient": recipient,
        # other required fields per API docs
    }
    response = requests.post(API_URL, json=data, headers=headers)
    return response.json()

def send_payment(amount, recipient):
    pass