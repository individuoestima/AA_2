import random

file = open("valores.txt","w")

for i in range(0,1000):
    file.write(str(random.randint(0,100))+"\n");