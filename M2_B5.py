import random;
import pickle;

"""Create"""
elements = set(random.sample(range(147,264), 15))
print("Elements:", elements)

"""Get file name"""
print("Please enter file name:")
fileName = input()
fileName = fileName + '.bin' #Add file extension

"""Write binary file"""
binFile = open(fileName, 'wb') #Open file to write
pickle.dump(elements, binFile)
binFile.close() #Close file

"""Delete elements from memory"""
elements.clear()

"""Read binary file"""
binFile = open(fileName, "rb") #Open file to read
newElements = pickle.load(binFile) #New set
binFile.close() #Close file

"""Create elementsList"""
elementsList = list(newElements) #Convert set to list
elementsList.sort() #Sort

"""Print"""
for i in range(0, len(elementsList)):
    print('Element #:', i, '=', elementsList[i])