import re

# Sample multiline text for demonstration and testing
sample_text = """
Contact us at user@example.com or firstname.lastname@company.co.uk.
Visit https://www.example.com or https://subdomain.example.org/page.
Call us at (123) 456-7890, 123-456-7890, or 123.456.7890.
Meeting times: 14:30, 2:30 PM, and 09:15 am.
Some HTML: <p>, <div class="example">, <img src="image.jpg" alt="description">
Prices: $19.99, $1,234.56, and $1000000.00.
"""

# Dictionary of regex patterns
regex_patterns = {
    "Email Addresses": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "URLs": r"https?://[^\s]+",
    "Phone Numbers": r"(?:\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}",
    "Time Formats (12/24h)": r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[AaPp][Mm])?\b",
    "HTML Tags": r"<[^>]+?>",
    "Currency Amounts": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\$\d+(?:\.\d{2})?"
}

def extract_data(text, patterns):
    """
    Extracts matching data from the input text based on the provided regex patterns.

    Args:
        text (str): The input text to search.
        patterns (dict): A dictionary of {pattern_name: regex}.

    Returns:
        dict: Extracted matches grouped by pattern name.
    """
    results = {}
    for name, pattern in patterns.items():
        matches = re.findall(pattern, text)
        results[name] = matches
    return results

def display_results(results):
    """
    Nicely formats and displays the extracted data.

    Args:
        results (dict): A dictionary of {pattern_name: [matches]}.
    """
    for category, items in results.items():
        print(f"\n{category}:")
        if items:
            for item in items:
                print(f"  - {item}")
        else:
            print("  (No matches found)")

if __name__ == "__main__":
    print("=== Regex Data Extractor ===")
    extracted = extract_data(sample_text, regex_patterns)
    display_results(extracted)

