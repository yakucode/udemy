# open('/root//coding//udemy//automateTheBoringStuff//11 - Files//hello.txt')

# open() returns a file object
import os
helloFile = open(
    '/root//coding//udemy//automateTheBoringStuff//11 - Files//hello.txt')
helloContent = helloFile.read()  # read() returns the file's contents as a string
print(helloContent)  # print() displays the string in the terminal
helloFile.close()  # close() closes the file object

helloFile = open(
    '/root//coding//udemy//automateTheBoringStuff//11 - Files//hello.txt')
# readlines() returns a list of strings, each string is a line of the file
print(helloFile.readlines())
helloFile.close()

helloFile = open(
    '/root//coding//udemy//automateTheBoringStuff//11 - Files//hello2.txt', 'w')
helloFile.write('Hello!!!!\n')
helloFile.write('Hello!!!!\n')
helloFile.write('Hello!!!!\n')

helloFile.close()

helloFile = open(
    '/root//coding//udemy//automateTheBoringStuff//11 - Files//hello2.txt')
print(helloFile.read())
helloFile.close()


baconFile = open('bacon.txt', 'w')
os.getcwd()
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('\n\nBacon is delicious.')
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)
