from faker import Faker
import datetime

def generate_dummy_last_names(num_to_generate):
    """
    Generate a list of random last names.

    Args:
        num_to_generate (int): Number of last names to generate.

    Returns:
        list: List of randomly generated last names.
    """
    fake = Faker()
    last_names = [fake.last_name() for _ in range(num_to_generate)]
    return last_names

def write_last_names_to_file(last_names, filename):
    """
    Write a list of last names to a file.

    Args:
        last_names (list): List of last names to write.
        filename (str): Name of the file to which the last names will be written.
    """
    with open(filename, 'w') as file:
        file.writelines('\n'.join(last_names))

def main():
    """
    Main function to execute the script.
    """
    # Get user input for the number of last names to generate
    num_to_generate = int(input("How many last names would you like to generate? "))

    # Generate random last names
    last_names = generate_dummy_last_names(num_to_generate)

    # Create filename with timestamp
    now = datetime.datetime.now()
    filename = now.strftime("%Y%m%d-%H%M%S") + "_random_last_names.txt"

    # Write last names to file
    write_last_names_to_file(last_names, filename)

    print(f"Random last names written to {filename}")

if __name__ == "__main__":
    main()
