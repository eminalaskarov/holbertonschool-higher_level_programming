#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Siyahıdakı tam ədədləri tərsinə, hər sətirdə bir ədəd olmaqla çap edir."""
    if my_list:
        for i in my_list[::-1]:
            print("{:d}".format(i))
