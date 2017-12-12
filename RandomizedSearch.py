import random
import os
import sys

with open(os.path.join(os.path.dirname(__file__), 'random_values')) as f:
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

def main():
    global opCount
    global opCount1
    num = int(sys.argv[1]);
    times = int(sys.argv[2]);
    print("Executed " + str(times)+" times")
    linear = 0 
    randomized = 0

    for i in range(0,times):
        linear_seach(values,num)
        linear += opCount
        randomized_search(values,num)
        randomized+=opCount1
        opCount = 0
        opCount1 = 0
    print("--------------------------------------------------------------------")
    print("             Repeated values - 1000 elements")
    print("--------------------------------------------------------------------")
    print("Average of Linear Search " +str(int(linear/times))+ " operations!" )
    print("Average of Random Search " +str(int(randomized/times))+ " operations!" )
    print("--------------------------------------------------------------------")

    linear = 0
    randomized = 0

    with open(os.path.join(os.path.dirname(__file__), 'sorted_values')) as f:
        values1 = f.readlines();

    values1 =[int(x.strip()) for x in values1]

    for i in range(0,times):
        linear_seach(values1,num)
        linear += opCount
        randomized_search(values1,num)
        randomized+=opCount1
        opCount = 0
        opCount1 = 0

    print("             Non-repeated sorted values - 100 elements")
    print("--------------------------------------------------------------------")
    print("Average of Linear Search " +str(int(linear/times))+ " operations!" )
    print("Average of Random Search " +str(int(randomized/times))+ " operations!" )
    print("--------------------------------------------------------------------")

    linear = 0
    randomized = 0

    with open(os.path.join(os.path.dirname(__file__), 'non_repeated_values')) as f:
        values2 = f.readlines();

    values2 =[int(x.strip()) for x in values2]

    for i in range(0,times):
        linear_seach(values2,num)
        linear += opCount
        randomized_search(values2,num)
        randomized+=opCount1
        opCount = 0
        opCount1 = 0

    print("             Non repeated non sorted values - 100 elements")
    print("--------------------------------------------------------------------")
    print("Average of Linear Search " +str(int(linear/times))+ " operations!" )
    print("Average of Random Search " +str(int(randomized/times))+ " operations!" )
    print("--------------------------------------------------------------------")

if __name__ == "__main__":
    main()