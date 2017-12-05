import random

file = open("random_values","w")

for i in range(0,1000):
    file.write(str(random.randint(0,100))+"\n");

file = open("sorted_values","w")

for i in range(0,1000):
    file.write(str(i)+"\n");