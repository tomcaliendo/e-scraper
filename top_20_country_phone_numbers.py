import re

# Define the criteria for the top 20 countries
country_criteria = {
    "China": r'\b(?:\+?86\s*[-.\s]?)?(?:\(?[0-9]{2,3}\)?[-.\s]?){3,}\b',  # China phone number pattern
    "India": r'\b(?:\+?91\s*[-.\s]?)?(?:\(?[0-9]{2}\)?[-.\s]?){3,}\b',  # India phone number pattern
    "United States": r'\b(?:\+?1\s*[-.\s]?)?(?:\(?[0-9]{3}\)?[-.\s]?){2}[0-9]{4}\b',  # USA phone number pattern
    "Indonesia": r'\b(?:\+?62\s*[-.\s]?)?(?:\(?[0-9]{2,4}\)?[-.\s]?){2,6}\b',  # Indonesia phone number pattern
    "Pakistan": r'\b(?:\+?92\s*[-.\s]?)?(?:\(?[0-9]{2,3}\)?[-.\s]?){2,6}\b',  # Pakistan phone number pattern
    "Brazil": r'\b(?:\+?55\s*[-.\s]?)?(?:\(?[0-9]{2}\)?[-.\s]?){2,6}\b',  # Brazil phone number pattern
    "Nigeria": r'\b(?:\+?234\s*[-.\s]?)?(?:\(?[0-9]{2}\)?[-.\s]?){3,6}\b',  # Nigeria phone number pattern
    "Bangladesh": r'\b(?:\+?880\s*[-.\s]?)?(?:\(?[0-9]{2,3}\)?[-.\s]?){3,6}\b',  # Bangladesh phone number pattern
    "Russia": r'\b(?:\+?7\s*[-.\s]?)?(?:\(?[0-9]{3}\)?[-.\s]?){1,5}[0-9]{2}[-.\s]?[0-9]{2}[-.\s]?[0-9]{2}\b',  # Russia phone number pattern
    "Mexico": r'\b(?:\+?52\s*[-.\s]?)?(?:\(?[0-9]{2}\)?[-.\s]?){2,6}\b',  # Mexico phone number pattern
    "Japan": r'\b(?:\+?81\s*[-.\s]?)?(?:\(?[0-9]{2,4}\)?[-.\s]?){2,6}\b',  # Japan phone number pattern
    "Ethiopia": r'\b(?:\+?251\s*[-.\s]?)?(?:\(?[0-9]{2}\)?[-.\s]?){3,6}\b',  # Ethiopia phone number pattern
    "Philippines": r'\b(?:\+?63\s*[-.\s]?)?(?:\(?[0-9]{2}\)?[-.\s]?){2,6}\b',  # Philippines phone number pattern
    "Vietnam": r'\b(?:\+?84\s*[-.\s]?)?(?:\(?[0-9]{2,3}\)?[-.\s]?){3,6}\b',  # Vietnam phone number pattern
    "Egypt": r'\b(?:\+?20\s*[-.\s]?)?(?:\(?[0-9]{2,4}\)?[-.\s]?){3,6}\b',  # Egypt phone number pattern
    "DR Congo": r'\b(?:\+?243\s*[-.\s]?)?(?:\(?[0-9]{2}\)?[-.\s]?){3,6}\b',  # DR Congo phone number pattern
    "Turkey": r'\b(?:\+?90\s*[-.\s]?)?(?:\(?[0-9]{2}\)?[-.\s]?){2,6}\b',  # Turkey phone number pattern
    "Iran": r'\b(?:\+?98\s*[-.\s]?)?(?:\(?[0-9]{2}\)?[-.\s]?){2,6}\b',  # Iran phone number pattern
    "Germany": r'\b(?:\+?49\s*[-.\s]?)?(?:\(?[0-9]{2,4}\)?[-.\s]?){2,6}\b',  # Germany phone number pattern
}

def check_phone_numbers(text):
    # Dictionary to store findings for each country
    findings = {country: set(re.findall(pattern, text)) for country, pattern in country_criteria.items()}
    return findings

def main():
    # Read the input text from a file or scrape from the web
    # Here, for demonstration purposes, we're using a simple example text
    text = """
    Here are some example phone numbers:
    China: +86 10 12345678, 86-10-1234567
    India: 91-80-12345678, +91 (80) 1234-5678
    United States: +1 (123) 456-7890
    """
    
    # Check phone numbers against the defined criteria
    results = check_phone_numbers(text)

    # Write the findings to the output file
    with open("world_top_20_phone_numbers.txt", "w") as output_file:
        for country, numbers in results.items():
            output_file.write(f"{country} phone numbers:\n")
            if numbers:
                for number in numbers:
                    output_file.write(f"- {number}\n")
            else:
                output_file.write("No numbers found.\n")

if __name__ == "__main__":
    main()
