import re
rule="[a-z0-9_]+[@][a-z]+.[a-z]*"
var_name=input("ENTER MAIL ADDRESS")
match=re.fullmatch(rule,var_name)
if match == None:
    print("INVALID EMAIL ACCOUNT")
else:
    print("VALID EMAIL")

