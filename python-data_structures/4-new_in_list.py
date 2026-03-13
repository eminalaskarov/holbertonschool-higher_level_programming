#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list without modifying the original."""
    # Orijinal siyahının nüsxəsini yaradırıq
    copy_list = my_list[:]

    # İndeksi yoxlayırıq
    if idx < 0 or idx >= len(my_list):
        return copy_list

    # Dəyişikliyi nüsxə üzərində edirik
    copy_list[idx] = element
    return copy_list
