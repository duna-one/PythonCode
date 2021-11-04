import random

kort = tuple([random.randint(0,100) for _ in range(125)])
lists_List = list()

for i in range(25):
    lists_List.append(list(kort[i:i+5]))

for i in range(len(lists_List)):
    print(lists_List[i])