# Teo Espero
# BS Cloud and Systems Administration
# Western Governors University

# begin

theFile = input('Enter file to open: ')
try:
    myFile = open(theFile)
except:
    print('File cannot be opened.')
    quit()

lineNumber = 0
letters = 0
numbers  = 0
specialChar = 0
for lines in myFile:
    lineNumber = lineNumber + 1
    myString = lines.rstrip()
    for chars in myString:
        if chars.lower() in 'abcdefghijklmnoppqrstuwxyz':
            letters = letters + 1
        elif chars.lower() in '1234567890':
            numbers = numbers + 1
        else:
            specialChar = specialChar + 1

print('The file ' + theFile + ' has:')
print(str(lineNumber) + ' lines')
print(str(letters) + ' letters')
print(str(numbers) + ' numbers')
print(str(specialChar) + ' special characters')

# end