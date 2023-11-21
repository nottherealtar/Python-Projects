import random
from faker import Faker
import datetime

def generate_dummy_first_names(num_to_generate):
    """
    Generate a list of random first names.

    Args:
        num_to_generate (int): Number of first names to generate.

    Returns:
        list: List of randomly generated first names.
    """
    fake = Faker()
    first_names = [fake.first_name() for _ in range(num_to_generate)]
    return first_names

def write_first_names_to_file(first_names, filename):
    """
    Write a list of first names to a file.

    Args:
        first_names (list): List of first names to write.
        filename (str): Name of the file to which the first names will be written.
    """
    with open(filename, 'w') as file:
        file.writelines('\n'.join(first_names))

def main():
    """
    Main function to execute the script.
    """
    # Get user input for the number of first names to generate
    num_to_generate = int(input("How many first names would you like to generate? "))

    # Generate random first names
    first_names = generate_dummy_first_names(num_to_generate)

    # Create filename with timestamp
    now = datetime.datetime.now()
    filename = now.strftime("%Y%m%d-%H%M%S") + "_random_first_names.txt"

    # Write first names to file
    write_first_names_to_file(first_names, filename)

    print(f"Random first names written to {filename}")

if __name__ == "__main__":
    main()
