import math
import random

def randint(min=0,max=100):
    a = random.randint(min,max)
    return a

def mergesort(list1):
    if len(list1)==1:
        return list1
    list2=list1[:math.floor(len(list1)/2)]
    list3=list1[math.floor(len(list1)/2):]
    list2=mergesort(list2)
    list3=mergesort(list3)
    return merge(list2,list3)
    
def merge(list2, list3):
    list4 = []
    while(list2 and list3):
        if list2[0] > list3[0]:
            list4.append(list3[0])
            list3.remove(list3[0])
        else:
            list4.append(list2[0])
            list2.remove(list2[0])
    while list2:
        list4.append(list2[0])
        list2.remove(list2[0])
    while list3:
        list4.append(list3[0])
        list3.remove(list3[0])   
    return list4

list1 = []
for x in range(15):
    list1.append(randint())
mergesort(list1)
print(mergesort(list1))