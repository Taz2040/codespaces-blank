''''
megastring = "This is a large string containing various words and phrases."
substrings_to_check = ["various", "phrases", "banana"]

if any(substring in megastring for substring in substrings_to_check):
    print("At least one substring found in the megastring.")
else:
    print("None of the substrings were found in the megastring.")
'''
Ucase_bool=0
Lcase_bool=1
sym_bool=0
num_bool=1
print("Password didnt meet enough of the requirements:")
bool_list=[Lcase_bool,Ucase_bool,num_bool,sym_bool]
warning_list=["Lowercase Letters.","Uppercase Letters.","Numbers.","Symbols or Spaces."]
print_list=[print("It Doesn't contain any " + warning_list[index]) for index,e in enumerate(bool_list) if e==0]       


print()
