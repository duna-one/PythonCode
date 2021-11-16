import math #��� ������ � ���������
import random #��� �������� ������ �� ���������� ����������
import pickle #��� ������ � ����

#�������
def TaskFunction(list1, list2):
    dictionary = dict() #�������� �������
    for i in range(len(list1)):
        absItem = math.fabs(list2[i]) #������ (���������� ��������) �������� �� ������� ������
        dictionary[list1[i]] = math.log(absItem) #���������� ���� ����-��������
    return dictionary

#�������� ����� �������
print("Enter length:") 
listlen = int(input()) 

#�������� 2� ������� ��������� ����� �� ���������� ���������� �� -100 �� 100
list1 = [random.randint(-100,100) for _ in range(listlen)]
list2 = [random.randint(-100,100) for _ in range(listlen)]

#������ ������ ��� ����������� �� �����
print(list1)
print(list2)

#��������������� ��������
dictionary = TaskFunction(list1, list2)

#������ � �������� ����
binFile = open("Slovar.bin", "wb") #������� ����
pickle.dump(dictionary, binFile) #�������� ������� � ����
binFile.close #������� ����

#������ ��������� �����
newDictionary = dict()
binFile = open("Slovar.bin", "rb") #������� ����
newDictionary = pickle.load(binFile) #��������� ������� �� �����
binFile.close #������� ����

#������ ���������� ����� �� �����
for couple in newDictionary.items():
    print(couple)