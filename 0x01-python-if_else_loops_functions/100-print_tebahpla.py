#!/usr/bin/python3
i = 122
while i > 64 and not (i > 90 and i < 97):
    print(chr(i), end="")
    i -= 1
    print(chr(i - 32), end="")
    i -= 1
