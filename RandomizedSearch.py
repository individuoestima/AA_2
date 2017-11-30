import random

with open('/home/kanto/Documents/AA/SequenciasDeInteiros/aleatorios02500.txt') as f:
    values = f.readlines();

values =[int(x.strip()) for x in values]

opCount = 0
opCount1 = 0

def linear_seach(array,n):
    global opCount
    for i in range(0,len(array)-1):
        opCount+=1
        if array[i] == n:
            return True;
    return False;

def randomized_search(array,n):
    global opCount1
    l = [];
    for i in range(0,len(array)-1):
        test = random.randint(0,len(array)-1)
        while test in l:
            test = random.randint(0,len(array)-1)
        l.append(test)
        opCount1+=1
        if(array[test] == n):
            return True;
    return False;

num = 14564097

if(linear_seach(values,num)):
    print(opCount)
else:
    print("Número não encontrado")

if(randomized_search(values,num)):
    print(opCount1)
else:
    print("Número não encontrado")