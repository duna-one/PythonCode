import random;

"""Create"""
elements = set(random.sample(range(147,263), 15))
print("Elements:\n" + str(list(elements)))

"""Get file name"""
print("Please enter file name:")
fileName = input()
if not fileName.__contains__('.'): 
    fileName = fileName + '.binary' #Add your own file extension if there is none

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
    newElements = newElements.union({item}) #Add element to new set
binFile.close() #Close file

"""Create elementsList"""
elementsList = list(newElements) #Convert set to list
elementsList.sort() #Sort

"""Print"""
for i in range(0, len(elementsList)):
    print('Element #:{0} = {1}'.format(i, elementsList[i]))