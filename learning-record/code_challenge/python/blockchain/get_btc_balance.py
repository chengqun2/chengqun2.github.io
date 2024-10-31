from pip._vendor import requests

def get_eth_balance(address, api_key):
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == '1':
        balance = int(data['result']) / 10**18  # Convert from Wei to Ether
        return balance
    else:
        raise Exception(f"Error: {data['message']}")

# Example usage
api_key = 'XJHE8ZM2D2HFS1BYF5V7QCHD316ZW2B87Y'
address = '0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5'
balance = get_eth_balance(address, api_key)
print(f"The balance of the address: {address} is {balance} ETH.")

