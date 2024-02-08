def main():
    print("Initializing...")
    print("Looking for inventory file(inventory.txt)....")

    try:
        inventory = []
        # Open the file in read mode
        with open("inventory.txt", 'r') as file:
            print("File Found!")
            print("Reading files...")
            lines = [line.strip() for line in file]
            fields= [line.split(',') for line in lines]
            inventory = []
    except FileNotFoundError:
        print("Error: File not found.")
        
        
        
        
        
    print("Validating inventory.txt....")
    print()
    def check_data_type(element, data_type):
        try:
            # Attempt to convert the element to the specified data type
            x=data_type(element)
            return True  # Return True if successful
        except ValueError:
            return False  # Return False if conversion fails
        
        

    print("Checking format of each entry in file...")
    def entry_format_check(index,line):
        if len(line)!=5:
            print(f"Row: {index} (first row is 0) has {len(line)} items.")
            print("Please keep in mind,the program cannot handle book titles with comma's(,) in them.")
            return False
        else:
            column_names = ['ISBN','Title','Author','Quantity','Price']
            column_types=[str,str,str,int,float]
            for x in range(5):
                if not check_data_type(line[x],column_types[x]) :
                    print("In line",index,column_names[x],":",line[x],"is not of type ",column_types[x])
                    return False
        return True
    for index,line in enumerate(fields):
        if not entry_format_check(index,line):
            return False
        else:
            isbn, title, author, quantity, price = line
            book = [
                isbn,
                title,
                author,
                int(quantity),
                float(price)
            ]
            inventory.append(book)
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
                    
        print("ISBN(s) have valid prefix group and valid check digit.")
        return True
    
    def ISBN_is_unique(list,new_item_bool):
        """Verifies that each ISBN in the list is unique and does not repeat.
    
        Args:
            list (list): A list of strings representing ISBN-13 numbers.
            new_item_bool (bool): A flag indicating whether the last item in the list is a new item to be added or not.
    
        Returns:
            bool: True if all ISBNs in the list are unique, False otherwise.
        """
        templist=[x.replace("-","") for x in list] # Remove the hyphens from the ISBNs
        blank=[] # Create an empty list to store the unique ISBNs
        for i,num in enumerate(templist):
            if num not in blank: # Check if the ISBN is already in the unique list
                blank.append(num) # If not, add it to the unique list
            else:
                index=[blank.index(num),i] # If yes, find the indices of the repeated ISBNs
                if new_item_bool and i==(len(templist-1)): # If the last item is a new item to be added, print a warning message
                    print("ISBN:",num,"already exists in list,index:",index[0])
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
        pass
    else:
        return false
    
main()