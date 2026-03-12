#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # sys.argv[0] skriptin adıdır, ona görə arqument sayını tapmaq üçün 1 çıxırıq
    count = len(sys.argv) - 1

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Hər bir arqumenti dövr (loop) vasitəsilə çap edirik
    for i in range(1, count + 1):
        print("{}: {}".format(i, sys.argv[i]))
