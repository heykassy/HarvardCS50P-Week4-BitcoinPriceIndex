import json
from sys import argv, exit
import requests

if len(argv) != 2:
    exit("Missing command-line argument")


try:
    multiplier = float(argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
except ValueError:
    exit("Command-line argument is not a number")
except requests.RequestException:
    exit("There was an exception at request")

result = float(response["bpi"]["USD"]["rate"].replace(",", "")) * multiplier

print(f"${result:,.4f}")