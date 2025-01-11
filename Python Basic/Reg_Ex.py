import re

def extract_emails_and_phones(file_path):
    # Define regex patterns for emails and phone numbers
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\b\d{10}\b|\b(?:\d{3}-){2}\d{4}\b|\b(?:\+\d{1,3} )?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}\b'

    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Find all matches for emails and phone numbers
    emails = re.findall(email_pattern, content)
    phones = re.findall(phone_pattern, content)

    # Print results in a formatted way
    print("\nExtracted Email Addresses:")
    for email in emails:
        print(f"- {email}")

    print("\nExtracted Phone Numbers:")
    for phone in phones:
        print(f"- {phone}")

# Example Usage
if __name__ == "__main__":
    # Specify the text file to analyze
    file_path = "sample_text.txt"
    extract_emails_and_phones(file_path)
