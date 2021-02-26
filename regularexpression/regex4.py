import re
rule="[0-9]{10}"
var_name=input("ENTER PHONE NUMBER")
match=re.fullmatch(rule,var_name)
if match == None:
    print("INVALID PHONE NUMBER")
else:
    print("VALID PHONE NUMBER")

