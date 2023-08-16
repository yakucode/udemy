#! python3

import re
import pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''        # 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345 
(
    ((\d\d\d) | (\(\d\d\d\)))?      # area code (optional)
    (\s | -)                        # first seperator
    \d\d\d                          # first 3 digits
    -                               # seperator
    \d\d\d\d                        # last 4 digits
    (((ext(\.)?\s)|x) |             # extension word part (optional)         
    (\d{2,5}))?                     # extension number-part(optional)           
)
''', re.VERBOSE)

# Create a regex for email addresses

emailRegex = re.compile(r'''    # some.+_thing@some.+_thing.com
\b[a-zA-Z0-9_.+]+               # name part
@                               # @ symbol
[a-zA-Z0-9_+]+                 # domain name part                        
.                               # dot part
[a-zA-Z0-9]+\b                  # domain extension part                        
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhoneNum = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

# Add the full phonen numbers found to the allPhoneNumbers array
allPhoneNumbers = []
for phoneNumer in extractedPhoneNum:
    allPhoneNumbers.append(phoneNumer[0])


print(allPhoneNumbers)
print(extractedEmail)

# Copy the extracted email/phone to the cipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
