import requests
APP_ID = "58d5ce1fb2a34716b777b32343c4f86b"

# API Endpoint for getting Exchange Rate information is https://openexchangerates.org/api/latest.json
ENDPOINT_EXCHANGE_RATE = "https://openexchangerates.org/api/latest.json"

response_EXCHANGE_RATE = requests.get(f"{ENDPOINT_EXCHANGE_RATE}?app_id={APP_ID}")
print(response_EXCHANGE_RATE.content)

# For getting json output
exchange_dict = response_EXCHANGE_RATE.json()
print(exchange_dict)

usd_amount = 3700
inr_amount = usd_amount * exchange_dict['rates']['INR']

print(f"{usd_amount} USD is {inr_amount} INR")
