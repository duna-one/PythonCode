import math #Для модуля и логорифма
import random #Для создания списка со случайными значениями
import pickle #Для записи в файл

#Функция
def TaskFunction(list1, list2):
    dictionary = dict() #Создание словаря
    for i in range(len(list1)):
        absItem = math.fabs(list2[i]) #Модуль (абсолютное значнеие) значения из второго списка
        dictionary[list1[i]] = math.log(absItem) #Добавление пары ключ-значение
    return dictionary

#Получили длину списков
print("Enter length:") 
listlen = int(input()) 

#Создание 2х списков указанной длины со случайными значениями от -100 до 100
list1 = [random.randint(-100,100) for _ in range(listlen)]
list2 = [random.randint(-100,100) for _ in range(listlen)]

#Вывели списки для наглядности на экран
print(list1)
print(list2)

#Воспользовались функцией
dictionary = TaskFunction(list1, list2)

#Запись в бинарный файл
binFile = open("Slovar.bin", "wb") #Открыли файл
pickle.dump(dictionary, binFile) #Записали словарь в файл
binFile.close #Закрыли файл

#Чтение бинарного файла
newDictionary = dict()
binFile = open("Slovar.bin", "rb") #Открыли файл
newDictionary = pickle.load(binFile) #Прочитали словарь из файла
binFile.close #Закрыли файл

#Вывели содержимое файла на экран
for couple in newDictionary.items():
    print(couple)