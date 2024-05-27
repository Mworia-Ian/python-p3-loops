#!/usr/bin/env python3
num = 10

def happy_new_year():
    # code goes here!
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -=1
    print("Happy New Year!")
happy_new_year()

pass


def square_integers(int_list):
    squared_list = []
    # code goes here!
    for integer in int_list:
        squared_integers = integer**2
        squared_list.append(squared_integers)
    return squared_list

ints = square_integers([2,3,4])
print(ints) 
pass

def fizzbuzz():
    # code goes here!
    num = 1
    while num < 101:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz") 
        elif num % 5 == 0:
            print("Buzz") 
        elif  num % 3 == 0:
            print("Fizz") 
        else:
            print(num) 
        num += 1
fizzbuzz()



pass
