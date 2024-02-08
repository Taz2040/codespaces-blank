def main():
    """The main function of the program that executes the validation process.

    It prints the status messages to the console and handles any exceptions.
    """
    print("Initializing...")
    print("Looking for inventory file(inventory.txt)....")

    try:
        inventory = [] # A list to store the valid books
        # Open the file in read mode
        with open("inventory.txt", 'r') as file:
            print("File Found!")
            print("Inventory database must in a valid format/file in order to proceed. ")  
            print("Reading file...")
            lines = [line.strip() for line in file] # A list of strings, each representing a line in the file
            fields= [line.split(',') for line in lines] # A list of lists, each representing a book with its fields
            inventory = [] # A list to store the valid books
            import pandas as pd
            column_names=['ISBN','Title','Author','Quantity','Price']
            df = pd.DataFrame(fields, columns=['ISBN','Title','Author','Quantity','Price'])
    except FileNotFoundError:
        print("Error: File not found.") # Handle the exception if the file is not found
        
      
    print("Validating inventory.txt....")
    print()
    def check_data_type(element, data_type):
        """Checks if an element can be converted to a specified data type.

        Args:
            element (str): The element to be checked.
            data_type (type): The data type to be converted to.

        Returns:
            bool: True if the element can be converted, False otherwise.
        """
        try:
            # Attempt to convert the element to the specified data type
            x=data_type(element)
            return True  # Return True if successful
        except ValueError:
            return False  # Return False if conversion fails
        
        

    print("Checking format of each entry in file...")
    def entry_format_check(index,line):
        """Checks if a line in the file has the correct format and data types.

        Args:
            index (int): The index of the line in the file (starting from 0).
            line (list): A list of strings representing the fields of a book.

        Returns:
            bool: True if the line has the correct format and data types, False otherwise.
        """
        if len(line)!=5: # Check if the line has 5 fields
            print(f"Row: {index} (first row is 0) has {len(line)} items.")
            print("Please keep in mind,the program cannot handle book titles with comma's(,) in them.")
            return False
        else:
            column_names = ['ISBN','Title','Author','Quantity','Price'] # A list of column names for reference
            column_types=[str,str,str,int,float] # A list of data types for each column
            for x in range(5): # Loop through each field
                if not check_data_type(line[x],column_types[x]) : # Check if the field can be converted to the corresponding data type
                    print("In line",index,column_names[x],":",line[x],"is not of type ",column_types[x])
                    return False
        return True # Return True if all fields are valid
    for index,line in enumerate(fields): # Loop through each line in the file
        if not entry_format_check(index,line): # Check if the line has the correct format and data types
            print("Please ammend the inventory file in order to proceed")
            return False # Return False if not
        else:
            isbn, title, author, quantity, price = line # Unpack the fields into variables
            book = [ # Create a list representing a book
                isbn,
                title,
                author,
                int(quantity), # Convert the quantity to an integer
                float(price) # Convert the price to a float
            ]
            inventory.append(book) # Add the book to the inventory list
    print("Each entry is of correct data type and format.")
    print()
    
    
    print("Validatinge each ISBN....") 
    isbn_list=[book[0] for book in inventory]
    def ISBN_char_and_charlen_verification(list):
        """Verifies that each ISBN in the list has the correct length, format, and characters.

        Args:
            list (list): A list of strings representing ISBN-13 numbers.

        Returns:
            bool: True if all ISBNs in the list are valid, False otherwise.
        """
        index=0     
        for index,num in enumerate(list):             
            if len(num)!=17: # Check if the ISBN has 17 characters (13 digits + 4 hyphens)
                print("ISBN:",num,"in line",index,"doesn't follow ISBN 13 format,it has",len(num),"characters.")
                print("It must only have 13 digits,seperated by 4 hyphens,a total of 17 characters.")
                return False

            hiphen_count=0          
            for char in num:
                if (not (char>='0' and char<='9')) and (char!="-"): # Check if the ISBN contains only digits and hyphens
                    print("ISBN:",num,"in line",index,"contains characters other than digits and hiphens. The character:"+char+" is invalid")
                    return False
                elif char=="-": # Count the number of hyphens in the ISBN
                    hiphen_count+=1
            if hiphen_count!=4: # Check if the ISBN has 4 hyphens
                print("ISBN:",num,"in line",index,"contains",hiphen_count,"hiphens ('-'),it should only have 4 hiphens.")
                return False 
        print("ISBN(s) are of right lenght, contain only valid characters and have 5 groups.")       
        return True

    def ISBN_group_and_checkdigit_validation(list):
        """Verifies that each ISBN in the list has a valid prefix, registrant, publication, and check digit.

        Args:
            list (list): A list of strings representing ISBN-13 numbers.

        Returns:
            bool: True if all ISBNs in the list are valid, False otherwise.
        """
        index=0
        for index,number in enumerate(list):
            num=number.split('-') # Split the ISBN by hyphens into a list of 5 elements
            if (num[0]!="978") and (num[0]!="979"): # Check if the prefix element is 978 or 979
                print("ISBN:",number,"in line",index,"is invalid as the prefix element(the first group)",num[0],",is invalid")
                print("As time of writing,ISBN 13 only supports the prefix elements 978 and 979.")
                return False
            if len(num[4])!=1: # Check if the check digit element is one digit
                print("ISBN:",number,"in line",index,"is invalid as the check digit(the last digit/group) can be of only one character")
                return False
            
            num2=''.join(num) # Join the list of elements into a single string without hyphens
            # Calculate the sum of even-positioned digits
            even_sum = sum(int(num2[i]) for i in range(1, 12, 2)) * 3

            # Calculate the sum of odd-positioned digits (except the last digit)
            odd_sum = sum(int(num2[i]) for i in range(0, 11, 2))

            # Combine the sums and compute the check digit
            total_sum = even_sum + odd_sum
            remainder = total_sum % 10
            if remainder != 0:
                check_digit = 10 - remainder 
            else:
                check_digit=0
            if check_digit!=int(num2[12]): # Check if the computed check digit matches the actual check digit
                print("ISBN:",number,"in line",index,"Invalid as the actual last digit is",num2[12])
                print("But the calculated check-digit is",check_digit )
                return False

        print("ISBN(s) have valid prefix group and valid check digit.")
        return True

    def ISBN_is_unique(lst,new_item_bool):
        """Verifies that each ISBN in the list is unique and does not repeat.

        Args:
            list (list): A list of strings representing ISBN-13 numbers.
            new_item_bool (bool): A flag indicating whether the last item in the list is a new item to be added or not.

        Returns:
            bool: True if all ISBNs in the list are unique, False otherwise.
        """
        templist=lst # Remove the hyphens from the ISBNs
        blank=[] # Create an empty list to store the unique ISBNs
        for i,num in enumerate(templist):
            if num not in blank: # Check if the ISBN is already in the unique list
                blank.append(num) # If not, add it to the unique list
            else:
                index=[blank.index(num),i]
                temporary=len(templist)-1# If yes, find the indices of the repeated ISBNs
                if new_item_bool and (i==temporary): # If the last item is a new item to be added, print a warning message
                    print("ISBN:",num,"exists in list,index:",index[0])
                else: # If not, print an error message
                    print(f"ISBN:{num} repeats atleast in {index[0]} and {i}")
                return False
        return True

    def ISBN_validation(isbn_list):
        """Validates a list of ISBN-13 numbers by calling the previous three functions.

        Args:
            isbn_list (list): A list of strings representing ISBN-13 numbers.

        Returns:
            bool: True if all ISBNs in the list are valid and unique, False otherwise.
        """
        validation1=ISBN_char_and_charlen_verification(isbn_list) # Call the first function to verify the length, format, and characters
        validation2=ISBN_group_and_checkdigit_validation(isbn_list) # Call the second function to verify the prefix, registrant, publication, and check digit
        validation3=ISBN_is_unique(isbn_list,False) # Call the third function to verify the uniqueness of the ISBNs
        print("ISBN(s) are unique")
        if validation1 and validation2 and validation3: # If all three functions return True, the ISBNs are valid
            return True
        else: # If any of the functions return False, the ISBNs are invalid
            return False
    if ISBN_validation(isbn_list):
        print("Inventory file validated.")
        print("You may proceed.")
        pass
    else:
        print("Please ammend the inventory file in order to proceed")
        return False
    print("------------------------------------------------------------------------------------------")  
    
    
    
    
    
    
    
    
    
    
    
    
    
      
    def display_inventory(inventory):
        print("Inventory:")
        print(df)
        
        
        
        
        
        
    def add_book(inventory):
        bool=True
        while bool:
            while True:
                isbn=input("Enter Uniqueq ISBN number with proper format:")
                if ISBN_char_and_charlen_verification([isbn]) and ISBN_group_and_checkdigit_validation([isbn]):
                    temp_list=isbn_list+[isbn]
                    if ISBN_is_unique(temp_list,True):
                        break
                else:
                    x=input("Try again?(press y for yes anything else to go back to menu):")
                    if x=="y":
                        print()
                        pass
                    else:
                        bool=False
                        break
            if not bool:
                break
            title=input("Title:")
            author=input("Author:")
            while True:
                quantity=input("Quantity:")
                if check_data_type(quantity,int):
                    break
                else:
                    x=input("Invalid,try again?(press y for yes anything else to go back to menu):")
                    if x=="y":
                        print()
                        pass
                    else:
                        bool=False
                        break
            if not bool:
                break
            while True:
                price=input("price:")
                if check_data_type(price,float):
                    break
                else:
                    x=("Invalid,try again?(press y for yes anything else to go back to menu):")
                    
                    if x=="y":
                        print()
                        pass
                    else:
                        bool=False
                        break
            if not bool:
                break
            
            record=[isbn,title,author,quantity,price]
            print()
            print("You have entered:")
            x=[print(column_names[i],":",item) for i,item in enumerate(record)]
            x=input("Are you sure?Press y to accept anything else try again:")
            if x=="y":
                book = [ # Create a list representing a book
                    isbn,
                    title,
                    author,
                    (quantity), # Convert the quantity to an integer
                    (price)] # Convert the price to a float
                line=','.join(book)
                line=line+"\n"
                with open("inventory.txt", "a") as file:
                # Write the line to the file
                    file.write(line)
                    fields.append(book)
                print("Book Added")
                bool=False
                break
    
    def update_stock(inventory):
        isbn=input("enter ISBN:")
        cont=True
        if ISBN_char_and_charlen_verification([isbn]) and ISBN_group_and_checkdigit_validation([isbn]):
            temp=isbn_list+[isbn]
            if not ISBN_is_unique(temp,True):
                for i,x in enumerate(isbn_list):
                    if x==isbn:
                        print("Current stock of book saved as:",fields[i][3])
                        stock=input("New stock of the book:")
                        x=input("Are you sure you want to update?(press y to continue,others to cancel):")
                        if x!='y':
                            cont=False
                            break    
                        fields[i][3]=stock
                        with open("inventory.txt", "w") as file:
                        # Write the line to the file
                            to_write=[]
                            for i,x in enumerate(fields):
                                x=','.join(x)
                                to_write.append(x)
                            file.writelines(s + "\n" for s in to_write)
                            print("Book updated.")
                        break
            elif cont:
                print("ISBN not in database.")
        else:
            print("ISBN invalid.")
                
                        

    def search_isbn(inventory):
        cont=True
        while cont:
            isbn=input("ISBN to lookup:")
            if ISBN_char_and_charlen_verification([isbn]) and ISBN_group_and_checkdigit_validation([isbn]):
                if not ISBN_is_unique(isbn_list+[isbn],True):
                    for i,x in enumerate(isbn_list):
                        if x==isbn:
                            print(df.iloc[i])
                            cont=False
                            break
                else:
                    print("Book not in inventory or database.")
            else:
                print("Invalid ISBN")
            if cont:
                x=input("Try again?(Press y to continue, anything else to go back to menue):")
                print()
                if x!="y":
                    cont=False
                    
        
    def inventory_value(inventory):
        sums=[(float(book[3])*float(book[4])) for book in fields]
        result=0
        for sum in sums:
            result=float(result+sum)

        result=round(result,2)
        print("Inventory value is:",result)    
        
        
    def sales_report(inventory):
        cont=True
        sum_list=[]
        sold_index_list=[]
        sold_quants=[]
        cont2=True
        while cont2:
            isbn=input("Enter ISBN for the book sold:")
            if not ISBN_is_unique(isbn_list+[isbn],True):
                for i,x in enumerate(isbn_list):
                    if x==isbn:
                        index=i
                        break
                price=float(fields[index][4])
                current_quant=int(fields[index][3])
                print("Quantity remaining:",current_quant)
                while True:
                    sold=input('Number of Books Sold:')
                    x=check_data_type(sold, int)
                    if not x or int(sold)<0:
                        print("Please enter a positive whole")
                    elif current_quant-int(sold)<0:
                        print("Invalid quantity sold as there was not enough stock to be sold that many")
                        print("Please check if you have entered the ISBN for the wrong,if you just press 0 for quantity sold.")
                    elif int(sold)!=0:
                        x=input("Book found,valid sold amount,confirm sales?(press y to continue,else to rentry):")
                        if x=="y":
                            already_in=False
                            fields[index][3]=current_quant-int(sold)
                            for i,val in enumerate(sold_index_list):
                                if val==index:
                                    sold_quants[i]=sold_quants[i]+int(sold)
                                    sum_list[i]=sum_list[i]+((price)*float(sold))
                                    already_in=True
                            if not already_in:
                                sold_quants.append(int(sold))
                                sold_index_list.append(index)
                                sum_list.append(roun((price)*float(sold),2))
                                print("Sales added")
                                print("")
                            x2=input("Generate report or continue?(press y to to generate,else to continue):")
                            if x2=='y':
                                cont2=False
                            break
                        else:
                            break
                    else:
                        break
                        
            else:
                print("ISBN not in database, please re-enter a ISBN with proper formating which is in inventory")
                
                        
                
        print("Generate")
        print(f"sold quants:{sold_quants}")
        print(f"sold index:{sold_index_list}")
        print(f"sold sums:{sum_list}")

                                
                    
            
        
                
            
                        
                    
                    
            
                
            
                    
                
                
                

    while True:
        import pandas as pd
        column_names=['ISBN','Title','Author','Quantity','Price']
        df = pd.DataFrame(fields, columns=['ISBN','Title','Author','Quantity','Price'])
        inventory=fields
        print()
        print()
        print("------------------------------------------------------------------------------------------")  
        messages=["1)Display Inventory","2)Add Book","3)Update Stock","4)Search For Book by ISBN","5)Calculate Inventory Value",
                  "6)Generate sales report","7)Exit Program"]
        x=[print(e) for e in messages]
        print()
        # Ask the user to enter a number from 1 to 6
        num = input("Enter a number from 1 to 7: ")
        # Use the match and case keywords to execute the functions based on the user input
        match num:
            case "1":
                print("Display Inventory:")
                print()
                display_inventory(inventory)
            case "2":
                print("Add Book:")
                print()
                add_book(inventory)
            case "3":
                print("Update Stock:")
                print()
                update_stock(inventory)
            case "4":
                print("Search For Book by ISBN:")
                print()
                search_isbn(inventory)
            case "5":
                print("Calculate Inventory Value:")
                inventory_value(inventory)
            case "6":
                print("Generate sales report:")
                print()
                sales_report(inventory)
            case "7":
                return True
            case _:
                print("Invalid input. Please enter a number between 1 and 7.")
    
    
main()
print()