#!/usr/bin/python3
def uniq_add(my_list=[]):
    return list(map(lambda add : list(map(lambda x: x + x, add)), my_list))
    print("Result: {:d}".format(result))
