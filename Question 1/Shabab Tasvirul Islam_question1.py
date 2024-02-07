def validate_wifi_password(key):
    if not isinstance( key , str) or (len(key)<12) :
        print("Invalid,The password is not a string of atleast 12 characters.")
        return False
    
    def symbol_check(char):
        symbols=' !"#$%&()*+, -./:;<=>?@[\]^_`{|}~'
        if (char in symbols) or char=="'":
            return True        
        else:
            return False

    Ucase_bool=0
    Lcase_bool=0
    sym_bool=0
    num_bool=0
    for index,char in enumerate(key):
        val= ord(char)
        if char>='a' and char<='z':
            Lcase_bool=1
        elif char>='A' and char<='Z':
            Ucase_bool=1
        elif char>='0'and char<='9':
            num_bool=1
        elif symbol_check(char):
            sym_bool=1
        if index<(len(key)-2) and not symbol_check(char):
            if not symbol_check(key[index+2]) and (char+chr(val+1)+chr(val+2))==key[index:(index+3)] :
                print("Invalid,password contains sequential letters/numbers:",key[index:(index+3)])
                return False
        
    total_bool= Lcase_bool+Ucase_bool+num_bool+sym_bool
    if total_bool<3:
        print("Invalid,Password didnt meet enough of the requirements:")
        bool_list=[Lcase_bool,Ucase_bool,num_bool,sym_bool]
        warning_list=["Lowercase Letters.","Uppercase Letters.","Numbers.","Symbols or Spaces."]
        print_list=[print("It Doesn't have any " + warning_list[index]) for index,e in enumerate(bool_list) if e==0]       
        return False
    

    import dict_api 
    words=dict_api.fetchwords() 
    upperkey=key.upper() 
    for e in (e for e in words if e.upper() in upperkey):
        print("Invalid,Password contains Common Word: "+e.upper())
        return False
    print("Valid Password.")
    return True 


passlist=[ "SomeHowValid CuzSpaceASymbol","Small_len","Enough_lengt","Over_LengthLim","onlylowercase",
          "ONLYUPPERCASE","UPPERandlower","Upper,Lower,Symbol","UPPERlower9Num",
          "FakeCommonword_Text","Sequential_letters_mno",
          "Sequential_ascii-values,but_one_char_a_symbol_@AB","Sequential_ascii-values,but_one_char_a_symbol_YZ[" ]
for x in passlist:
    print("Password:",x)
    check=validate_wifi_password(x)
    print(check)
    print()


            
        


        