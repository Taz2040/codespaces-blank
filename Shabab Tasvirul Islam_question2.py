
def main():
    import pandas as pd
    print("Initializing...")
    print("Looking for inventory file(inventory.txt)....")
    try:
        # Open the file in read mode
        with open("inventory.txt", 'r') as file:
            print("File Found!")
            print("Reading files...")

            # Define the column names (header)
            column_names = ['ISBN','Title','Author','Quantity','Price'] 
            dtypes = {'ISBN': int, 'Title': float, 'Author': str,'Quantity':int,'Price':float}
            # Read the CSV file into a DataFrame and specify the column names
            db = pd.read_csv('inventory.txt', names=column_names,dtype=dtypes)


            # Display the DataFrame
            print("File successfully read:")

    except FileNotFoundError:
        print("Error: File not found.")
    except pd.errors.EmptyDataError:
        print("Error: file is empty.")
    except pd.errors.ParserError as e:
        print("Error reading file:", e)
        
    print("Validating Inventory file format")
    

main()
