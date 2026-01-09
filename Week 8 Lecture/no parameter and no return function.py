import time


def print_count_down():
        print ("Session will start in : ")
        for i in range (10, 0, -1):
            time.sleep(i)
            print(i)

print_count_down()


#function with no parameters and no return
import time

def print_count_down():
    for i in range(100, 0, -1):
        time.sleep(0.5)
        print(i)

print_count_down()


import time
import os




