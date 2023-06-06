#!/usr/bin/python3
i = 122
while (i > 64 and not(i > 90 and i < 97)):
    print("{}".format(chr(i)), end="")
    i -= 1
    print("{}".format(chr(i - 32)), end="")
    i -= 1
