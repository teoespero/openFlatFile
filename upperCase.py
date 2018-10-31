# Teo Espero
# BS Cloud and Systems Administration
# Western Governors University


import time
# begin

theFile = input('Enter file to open: ')
try:
    myFile = open(theFile)
except:
    print('File cannot be opened.')
    quit()

line = []
nCtr = 0
for lines in myFile:
    lines = lines.rstrip()
    line.append(lines.upper())
myFile.close()

theNewFile = theFile.replace('.txt', '-uppercase-' + time.strftime('%m-%d-%Y') + '.txt')
newFile = open(theNewFile,'w')
for rows in line:
    newFile.write(rows)

newFile.close()

# end