import os
import requests
import sys


if len(sys.argv) == 1:
	sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
	sys.exit("Too many command-line arguments")


try:
	bitcoin_number = float(sys.argv[1])
except ValueError:
	sys.exit("Command-line argument is not a number")
else:
	if bitcoin_number < 1:
		sys.exit("The value has to be bigger than 0")


try:
	API_KEY = os.environ["COIN_CAP_API_KEY"]
except KeyError:
	sys.exit("Missing API key")
else:
	headers = {"Authorization": "Bearer " + API_KEY}
	url = "https://rest.coincap.io/v3/price/bysymbol/BTC"
	

try:
	response = requests.get(url, headers=headers)
	response.raise_for_status()
except requests.exceptions.RequestException as e:
	sys.exit(e)
else:
	bitcoin_price = float(response.json()["data"][0])
	result = bitcoin_price * bitcoin_number
	print(f"${result:,.4f}")
	
