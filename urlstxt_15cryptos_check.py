import requests
from bs4 import BeautifulSoup
import re

# Regular expressions for each of the 15 most popular cryptocurrencies
crypto_regex = {
    "Bitcoin": r'\b(1[1-9A-HJ-NP-Za-km-z]{25,34}|3[1-9A-HJ-NP-Za-km-z]{25,34}|bc1[a-zA-HJ-NP-Z0-9]{6,74})\b',
    "Ethereum": r'\b(0x[a-fA-F0-9]{40})\b',
    "Binance Coin": r'\b(bnb[a-zA-Z0-9]{38})\b',
    "Cardano": r'\b(addr1[a-zA-Z0-9]{58})\b',
    "Solana": r'\b([a-zA-Z0-9]{105})\b',
    "XRP": r'\b(r[0-9a-zA-Z]{24,34})\b',
    "Polkadot": r'\b(1[1-9A-HJ-NP-Za-km-z]{24,34})\b',
    "Dogecoin": r'\b(D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32})\b',
    "Avalanche": r'\b(P-avalanche[1-9A-HJ-NP-Za-km-z]{78})\b',
    "Terra": r'\b(terra1[0-9A-Za-z]{38})\b',
    "Chainlink": r'\b(0x[a-fA-F0-9]{40})\b',  # Similar to Ethereum
    "Litecoin": r'\b([LM3][a-km-zA-HJ-NP-Z1-9]{26,33})\b',
    "Bitcoin Cash": r'\b((bitcoincash:)?(q|p)[a-z0-9]{41})\b',
    "Algorand": r'\b([A-Z2-7]{58})\b',
    "Polygon": r'\b(0x[a-fA-F0-9]{40})\b'  # Similar to Ethereum
}

# Function to search for cryptocurrency addresses on a website
def search_crypto_addresses(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        found_addresses = []

        for crypto, regex in crypto_regex.items():
            addresses = re.findall(regex, response.text)
            if addresses:
                found_addresses.extend([(address, crypto) for address in addresses])

        return found_addresses

    except Exception as e:
        print(f"An error occurred while searching {url}: {e}")
        return None

# Function to read URLs from a text file
def read_urls_from_file(filename):
    try:
        with open(filename, 'r') as file:
            urls = file.readlines()
        return [url.strip() for url in urls]
    except Exception as e:
        print(f"An error occurred while reading URLs from {filename}: {e}")
        return None

# Function to write findings to a text file
def write_findings_to_file(filename, findings):
    try:
        with open(filename, 'w') as file:
            for url, addresses in findings.items():
                if addresses:
                    file.write(f"URL: {url}\n")
                    file.write("Cryptocurrency addresses found:\n")
                    unique_addresses = set(addresses)  # Remove duplicates
                    for address, crypto in unique_addresses:
                        file.write(f"Address: {address} (Type: {crypto})\n")
                    file.write("\n")
        print(f"Findings saved to {filename}")
    except Exception as e:
        print(f"An error occurred while writing findings to {filename}: {e}")

# Main function
def main():
    urls_filename = "urls.txt"  # Name of the file containing URLs
    findings = {}

    # Read URLs from file
    urls = read_urls_from_file(urls_filename)

    if urls:
        for url in urls:
            print(f"Searching {url} for cryptocurrency addresses...")
            found_crypto_addresses = search_crypto_addresses(url)
            if found_crypto_addresses:
                findings[url] = found_crypto_addresses
        write_findings_to_file("findings.txt", findings)
    else:
        print(f"No URLs found in {urls_filename}.")

if __name__ == "__main__":
    main()
