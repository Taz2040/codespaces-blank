def validate_wifi_password(key):
    if not isinstance( key , str) or (len(key)<12) :
        return False
    def symbol_check(chr):
        val=ord(chr)
        if (val>=32 and val<=47) or (val>=58 and val<=64) or (val>=91 and val<=96) or (val>=123 and val<=126):
            return True
        else:
            return False
    Ucase_bool=0
    Lcase_bool=0
    sym_bool=0
    num_bool=0
    for index,char in key:
        val= ord(char)
        if char>='a' and char<='z':
            Lcase_bool=1
        elif char>='A' and char<='Z':
            Ucase_bool=1
        elif char>='0'and char<='9':
            num_bool=1
        elif symbol_check(char):
            sym_bool=1
        if index<(len(key)-2) and symbol_check(char) and symbol_check(key[index+2]) and chr(val+1)==key[index+1] and chr(val+2)==key[index+2]:
            return False

            
    total_bool= Lcase_bool+Ucase_bool+num_bool+sym_bool
    if total_bool<3:
        return False
            
        


        