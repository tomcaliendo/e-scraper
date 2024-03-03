import re
import requests
from bs4 import BeautifulSoup

def extract_us_phone_numbers(text):
    # Regular expression to match US phone numbers
    us_phone_numbers = set(re.findall(r'\b(?:\+?1\s*[-.\s]?)?(?:\(?[0-9]{3}\)?[-.\s]?){2}[0-9]{4}\b', text))
    return us_phone_numbers

def scrape_and_extract_phone_numbers(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        # Extracting text from HTML
        text = soup.get_text()
        us_phone_numbers = extract_us_phone_numbers(text)
        return us_phone_numbers
    else:
        print(f"Failed to retrieve {url}")

def main():
    with open("urls.txt", "r") as file:
        urls = file.readlines()

    unique_phone_numbers = set()
    
    for url in urls:
        url = url.strip()  # Remove leading/trailing whitespace and newline characters
        us_phone_numbers = scrape_and_extract_phone_numbers(url)
        if us_phone_numbers:
            unique_phone_numbers.update(us_phone_numbers)

    if unique_phone_numbers:
        with open("phone_numbers.txt", "w") as output_file:
            output_file.write("US Phone Numbers:\n")
            for number in unique_phone_numbers:
                output_file.write(f"- {number}\n")
    else:
        print("No US phone numbers found.")

if __name__ == "__main__":
    main()
