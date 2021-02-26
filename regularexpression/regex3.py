import re
rule="[kK][lL][0-9][0-9][a-zA-z]{2}[0-9]{1,4}"
var_name=input("ENTER REGISTRATION NUMBER")
match=re.fullmatch(rule,var_name)
if match == None:
    print("VEHICLE IS NOT UNDER KERALA REGISTRATION")
else:
    print("VALID REGISTRATION")
