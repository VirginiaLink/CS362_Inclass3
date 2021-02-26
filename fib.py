# VIrginia Link
# 02/21/2021
# Inclass Activity 3

def fib(num):
    if num < 0:
        print("Oops! the fibonacci sequence only covers positive numbers")
        return 0
    elif num == 0:
        return 0
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fib(num-1) + fib(num-2)

def fact(num):
    res = 1 
    if num < 0:
        print("Oops! the factorial can only be calculated for positive numbers")
        return 0
    elif num == 0:
        return 0
    else:
        for i in range(1, num+1):
            res = res*i
        return res


#print("Testing 5: ", fact(5))
