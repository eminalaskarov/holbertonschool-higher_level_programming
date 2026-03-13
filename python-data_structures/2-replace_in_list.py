#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Siyahıdakı elementi verilmiş indeksdə yeni elementlə əvəz edir."""
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list
