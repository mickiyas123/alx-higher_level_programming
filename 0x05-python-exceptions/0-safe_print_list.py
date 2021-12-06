#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for c in my_list:
        count = count + 1

    try:
        if (x <= count):
            for i in range(x):
                print("{}".format(my_list[i]), end='')
            print('')
            return (my_list[x-1])
        else:
            for j in range(count):
                print("{}".format(my_list[j]), end='')
            print('')
            return (my_list[count-1])
    except TypeError:
        print("Error")
