#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    # Burada print funksiyası ilə formatlı şəkildə nəticəni yazmalısan
    print("{} + {} = {}".format(a, b, add(a, b)))
