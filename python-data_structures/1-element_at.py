#!/usr/bin/python3

def element_at(my_list, idx):
    """Siyahıdan verilmiş indeksdəki elementi qaytarır."""
    # İndeks mənfidirsə və ya siyahının uzunluğundan böyükdürsə
    if idx < 0 or idx >= len(my_list):
        return None
    
    # Əks halda elementi qaytar
    return my_list[idx]
