import re

beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search("Hello there"))

allDigitsReg = re.compile(r'^\d+$')
print(allDigitsReg.search("a1231541512312"))

atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall("the cat in the hat sat on the flat mat"))


nameReg = re.compile(r'First Name: (.*) Last Name: (.*)')
name = "First Name: Alex Last Name: Sweigart"
print(nameReg.findall(name))

serve = "<To serve humans> for dinner.>"
nongreedyReg = re.compile(r'<(.*?)>')
print(nongreedyReg.findall(serve))
greedyReg = re.compile(r'<(.*)>')
print(greedyReg.findall(serve))

prime = "Serve the public trust. \nProtect the innocent.\nUpload the law."
dotStar = re.compile(r'.*', re.DOTALL)

vowelReg = re.compile(r'[aeiou]', re.I)
print(vowelReg.findall("Al eE aAd Oo uuIIoi"))
