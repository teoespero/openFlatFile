# Teo Espero
# BS Cloud and Systems Administration
# Western Governors University


import time
import datetime
import os.path

# begin

theFile = input('Enter file to open: ')
try:
    myFile = open(theFile)
except:
    print('File cannot be opened.')
    quit()

line = []
for lines in myFile:
    lines = lines.rstrip()
    line.append(lines.upper())
myFile.close()

theNewFile = theFile.replace('.txt', '-uppercase-' + time.strftime('%m-%d-%Y') + '.txt')

if not os.path.exists(theNewFile):
    newFile = open(theNewFile,'w')
    newFile.close()
else:
    print(theNewFile + ' already exist.')
    theNewFile = theFile.replace('.txt', '-uppercase-' + time.strftime('%m-%d-%Y-%I%M%p') + '.txt')
    newFile = open(theNewFile, 'w')

for rows in line:
    newFile.write(rows)
newFile.close()
# end