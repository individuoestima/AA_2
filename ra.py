import random

file = open("non_repeated_values","w")

my_list = list(range(0,101))
random.shuffle(my_list)
for i in my_list:
    file.write(str(i)+"\n")