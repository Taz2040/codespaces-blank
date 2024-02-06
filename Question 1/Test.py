''''
megastring = "This is a large string containing various words and phrases."
substrings_to_check = ["various", "phrases", "banana"]

if any(substring in megastring for substring in substrings_to_check):
    print("At least one substring found in the megastring.")
else:
    print("None of the substrings were found in the megastring.")
'''
import dict_api 
words=dict_api.fetchwords()  
key = "Text123"
for f in (e for e in words if e in key):
    print(f)  # Output: Text
    break  # stop the loop when a match is found



print()
