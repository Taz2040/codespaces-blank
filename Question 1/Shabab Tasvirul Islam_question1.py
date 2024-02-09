def validate_wifi_password(key):
    """
    This function validates a wifi password based on four requirements:
    1. It must have a length of 12 or more characters.
    2. It must include a combination of characters from at least
       three of the following sets:
       Uppercase letters (A-Z)
       Lowercase letters (a-z)
       Digits (0-9)
       Special characters (e.g., @, #, $, %, ^, &, *)
    3. It cannot contain a sequence of three or more
       sequential characters (e.g., "abc," "123," "XYZ").
    4. It should not contain common dictionary
       words, to prevent dictionary attacks.

    Parameters:
    key (str): The wifi password to be validated.

    Returns:
    bool: True if the password is valid, False otherwise.
    """

    # Check if the password is a string of at least 12 characters
    if not isinstance( key , str) or (len(key)<12) :
        print("Invalid,The password is not a string of at least 12 characters.")
        return False
    
    # Define a helper function to check if a character is a symbol
    def symbol_check(char):
        symbols=' !"#$%&()*+, -./:;<=>?@[\]^_`{|}~'
        if (char in symbols) or char=="'":
            return True        
        else:
            return False

    # Initialize four boolean variables to keep track of the character sets
    Ucase_bool=0
    Lcase_bool=0
    sym_bool=0
    num_bool=0

    # Loop through each character in the password
    for index,char in enumerate(key):
        val= ord(char) # Get the ASCII value of the character
        if char>='a' and char<='z': # Check if the character is lowercase
            Lcase_bool=1
        elif char>='A' and char<='Z': # Check if the character is uppercase
            Ucase_bool=1
        elif char>='0'and char<='9': # Check if the character is a digit
            num_bool=1
        elif symbol_check(char): # Check if the character is a symbol
            sym_bool=1

        # Check if the character is part of a sequential pattern
        # This is done by comparing the current character and the next two characters
        # with their ASCII values incremented by one
        # For example, 'abc' has ASCII values 97, 98, 99
        # This check is only done if the character is not a symbol
        # and if there are at least two more characters after it
        if index<(len(key)-2) and not symbol_check(char):
            if not symbol_check(key[index+2]) and (char+chr(val+1)+chr(val+2))==key[index:(index+3)] :
                print("Invalid,password contains sequential letters/numbers:",key[index:(index+3)])
                return False
        
    # Sum up the boolean variables to get the total number of character sets
    total_bool= Lcase_bool+Ucase_bool+num_bool+sym_bool

    # Check if the password has at least three character sets
    if total_bool<3:
        print("Invalid,Password didn't meet enough of the requirements:")
        bool_list=[Lcase_bool,Ucase_bool,num_bool,sym_bool]
        warning_list=["Lowercase Letters.","Uppercase Letters.","Numbers.","Symbols or Spaces."]
        # Print a warning message for each missing character set
        print_list=[print("It Doesn't have any " + warning_list[index]) for index,e in enumerate(bool_list) if e==0]       
        return False
    
    # Import the dictionary API module
    import dict_api 
    # Fetch a list of common words from the API
    words=dict_api.fetchwords() 
    # Convert the password to uppercase for comparison
    upperkey=key.upper() 
    # Loop through each word in the list
    for e in (e for e in words if e.upper() in upperkey):
        # Check if the word is a substring of the password
        print("Invalid,Password contains Common Word: "+e.upper())
        return False
    # If all the checks are passed, the password is valid
    print("Valid Password.")
    return True 

            
        


        
