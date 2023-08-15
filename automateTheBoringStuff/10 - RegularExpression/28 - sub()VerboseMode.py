import re

string = 'Agent Alice gave the docu to Agent Bob'
nameReg = re.compile(r'Agent \w+')
print(nameReg.findall(string))

print(nameReg.sub('REDACTED', string))

nameReg = re.compile(r'Agent (\w)\w*')
print(nameReg.findall(string))
print(nameReg.sub(r'Agent \1****', string))


# verbose regular expression strings
re.compile(r'''
           (\d\d\d-) |      # area code 
           (\(\d\d\d\) )    # -or- area code with parens and no dash
           \d\d\d           # first 3 digits
           -                # second dash
           \d\d\d\d         # last 4 digits''', re.VERBOSE | re.DOTALL | re.IGNORECASE)
