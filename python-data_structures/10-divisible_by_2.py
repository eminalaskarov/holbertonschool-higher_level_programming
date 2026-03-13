#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Siyahıdakı ədədlərin 2-yə bölünüb-bölünmədiyini yoxlayır."""
    result_list = []
    for i in my_list:
        if i % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)
    return result_list
