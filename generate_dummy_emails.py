"""
generate_dummy_emails.py

This script generates a specified number of unique dummy email addresses using the Faker library.
The generated email addresses are then logged to a file with a timestamped filename.

Dependencies:
    - Faker: Library for generating fake data (install with 'pip install faker')

Usage:
    Run the script, and it will prompt you to enter the number of dummy email addresses to generate.
    The generated email addresses will be saved to a text file with a timestamped filename.

Example:
    $ python generate_dummy_emails.py
"""

import random
from faker import Faker
from datetime import datetime

def generate_dummy_emails(num_emails):
    """
    Generate unique dummy email addresses.

    Args:
        num_emails (int): Number of email addresses to generate.

    Returns:
        list: List of generated dummy email addresses.
    """
    fake = Faker()
    domain = "@gmail.com"
    dummy_emails_set = set()

    while len(dummy_emails_set) < num_emails:
        first_name = fake.first_name().lower()
        last_name = fake.last_name().lower()
        email = f"{first_name}.{last_name}{domain}"
        dummy_emails_set.add(email)

    return list(dummy_emails_set)

def log_emails_to_file(emails, filename):
    """
    Log a list of email addresses to a file.

    Args:
        emails (list): List of email addresses to log.
        filename (str): Name of the file to which the emails will be logged.
    """
    with open(filename, "w") as file:
        for email in emails:
            file.write(f"{email}\n")

def main():
    """
    Main function to execute the script.
    """
    num_emails = int(input("How many emails to generate? "))
    dummy_emails = generate_dummy_emails(num_emails)

    now = datetime.now()
    timestamp = now.strftime('%Y%m%d_%H%M%S')
    filename = f"dummy_emails_{timestamp}.txt"

    log_emails_to_file(dummy_emails, filename)

    print(f"Generated {len(dummy_emails)} dummy emails and logged to {filename}")

if __name__ == "__main__":
    main()