import random
import datetime

def generate_dummy_phones(num_to_generate):
    """
    Generate a list of random South African phone numbers.

    Args:
        num_to_generate (int): Number of phone numbers to generate.

    Returns:
        list: List of randomly generated phone numbers.
    """
    return ['+27' + str(random.randint(7600000000, 7699999999)) for _ in range(num_to_generate)]

def write_phone_numbers_to_file(phone_numbers, filename):
    """
    Write a list of phone numbers to a file.

    Args:
        phone_numbers (list): List of phone numbers to write.
        filename (str): Name of the file to which the phone numbers will be written.
    """
    with open(filename, 'w') as file:
        file.writelines('\n'.join(phone_numbers))

def main():
    """
    Main function to execute the script.
    """
    # Get user input for the number of phone numbers to generate
    num_to_generate = int(input("How many phone numbers would you like to generate? "))

    # Generate phone numbers
    phone_numbers = generate_dummy_phones(num_to_generate)

    # Create filename with timestamp
    now = datetime.datetime.now()
    filename = now.strftime("%Y%m%d-%H%M%S") + "_phone_numbers.txt"

    # Write phone numbers to file
    write_phone_numbers_to_file(phone_numbers, filename)

    print(f"Phone numbers written to {filename}")

if __name__ == "__main__":
    main()