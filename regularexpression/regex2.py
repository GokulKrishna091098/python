#start with a-k,second character should be a digit and it is divisible by 3,any number of characters
import re
rule="[a-k][369][a-zA-Z]*"
var_name=input("ENTER VARIABLE NAME")
match=re.fullmatch(rule,var_name)
if match == None:
    print("INVALID VARIABLE NAME")
else:
    print("VALID VARIABLE NAME")

