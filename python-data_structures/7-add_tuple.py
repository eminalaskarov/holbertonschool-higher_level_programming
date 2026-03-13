#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """İki korteji toplayır və nəticədə 2 elementli kortej qaytarır."""
    # Hər iki korteji 2 elementli formaya gətiririk
    # Çatışmayan yerlərə 0 əlavə edirik
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0
    
    return (a1 + b1, a2 + b2)
