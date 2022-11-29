#!/usr/bin/python3
for ch in range(97, 123):
    if "{:c}".format(ch) == 'q' or "{:c}".format(ch) == 'e':
        continue
    else:
        print("{:c}".format(ch), end='')
