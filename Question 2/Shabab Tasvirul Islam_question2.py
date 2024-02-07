def main():
    print("Initializing...")
    print("Looking for inventory file(inventory.txt)....")
    #Looking for and openning inventory file
    try:
        # Open the file in read mode
        with open('inventory.txt', 'r') as file:
            print("File Found!")
            print("Reading files...")
            # Read all lines and store them in a list using list comprehension
            lines = [line.strip() for line in file]
    except FileNotFoundError:
        print("File not found.")
    except IOError as e:
        print("An error occurred while reading the file:", e)
    else:
        print(lines)

main()