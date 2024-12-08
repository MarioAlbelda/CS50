import requests
import sys

# Number n of Bitcoins to buy
try:
    n = float(sys.argv[1])
    # current price of a Bitcoin
    if n > 0:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = r.json()
        price = float(o["bpi"]["USD"]["rate_float"])
        # print the price of n Bitcoins
        amount = n * price
        print(f"${amount:,.4f}")

except IndexError:
    sys.exit("Missing command-line argument")

except TypeError:
    sys.exit("Command-line argument is not a number")

# Trying to catch some exceptions
except requests.RequestException:
    sys.exit("There was an ambiguous exception that occurred while handling your request.")

except requests.ConnectionError:
    sys.exit("A Connection error occurred")
