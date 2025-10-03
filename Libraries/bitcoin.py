import sys
import requests

def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        bitcoins = float(sys.argv[1])
        if bitcoins <= 0:
            raise ValueError
    except ValueError:
        sys.exit("Command-line argument is not a Number.")

    API_KEY = "c8ef0c4a23ea6bbb0e9181539faba5fc740dbf925ecfcb4fc7a0efc899a148f6"
    url = "https://rest.coincap.io/v3/assets/bitcoin"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error: Unable to fetch Bitcoin price.")
    except (KeyError, ValueError):
        sys.exit("Error: Unexpected response format.")

    total_cost = bitcoins * price
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
