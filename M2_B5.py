import random;

"""Create"""
elements = set(random.sample(range(147,264), 15))
print("Elements:", elements)

"""Get file name"""
print("Please enter file name:")
fileName = input()
fileName = fileName + '.bin' #Add file extension

"""Write binary file"""
binFile = open(fileName, 'wb') #Open file to write
for item in elements:
    itemStr = str(item) + '\n' #Convert to string
    byte = itemStr.encode() #Convert to byte
    binFile.write(byte)
binFile.close() #Close file

"""Delete elements from memory"""
elements.clear()

"""Read binary file"""
binFile = open(fileName, "rb") #Open file to read
newElements = set() #New set
for line in binFile:
    item = int(line) #Convert bytes to int
    newElements.add(item) #Add element to new set
binFile.close() #Close file

"""Create elementsList"""
elementsList = list(newElements) #Convert set to list
elementsList.sort() #Sort

"""Print"""
for i in range(0, len(elementsList)):
    print('Element #:', i, '=', elementsList[i])