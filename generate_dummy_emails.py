
"""
generate_dummy_emails.py

This script generates unique dummy email addresses with random first and last names.
These emails are for work purposes, and no privacy is harmed.

Usage:
    python generate_dummy_emails.py
"""
from faker import Faker
import datetime

fake = Faker()

num_emails = int(input("How many emails to generate? "))

def generate_dummy_emails(num_emails):
    """
    Generate unique dummy email addresses with random first and last names.

    Args:
        num_emails (int): Number of email addresses to generate.

    Returns:
        list: List of generated dummy email addresses.
    """
    
    email_list = set()

    while len(email_list) < num_emails:
        first_name = fake.first_name()
        last_name = fake.last_name() 
        email = f"{first_name.lower()}.{last_name.lower()}@gmail.com"
        email_list.add(email)

    return list(email_list)

if __name__ == "__main__":
    
    # Generate dummy emails
    dummy_emails = generate_dummy_emails(num_emails)

    # Log the generated emails to a file with timestamp
    now = datetime.datetime.now()
    filename = f"dummy_emails_{now.strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(filename, "w") as f:
        for email in dummy_emails:
            f.write(f"{email}\n")
            
    print(f"Generated {len(dummy_emails)} dummy emails and logged to {filename}")
