import requests
from bs4 import BeautifulSoup

# List of popular social media platforms
social_media_list = [
    "facebook",
    "youtube",
    "instagram",
    "twitter",
    "linkedin",
    "whatsapp",
    "pinterest",
    "snapchat",
    "reddit",
    "tumblr",
    "tiktok",
    "skype",
    "telegram",
    "wechat",
    "discord"
]

# Function to search for social media accounts on a website
def search_social_media(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        found_accounts = []

        for social_media in social_media_list:
            # Check for presence of social media URLs in page content
            social_media_links = soup.find_all('a', href=lambda href: href and social_media in href.lower())
            if social_media_links:
                found_accounts.extend([link['href'] for link in social_media_links])

        return found_accounts

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
            for url, accounts in findings.items():
                if accounts:
                    file.write(f"URL: {url}\n")
                    file.write("Social media accounts found:\n")
                    for account in accounts:
                        file.write(f"{account}\n")
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
            print(f"Searching {url} for social media accounts...")
            found_social_media_accounts = search_social_media(url)
            if found_social_media_accounts:
                findings[url] = found_social_media_accounts
        write_findings_to_file("findings.txt", findings)
    else:
        print(f"No URLs found in {urls_filename}.")

if __name__ == "__main__":
    main()
