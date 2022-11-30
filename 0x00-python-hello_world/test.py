#!/usr/bin/python3
for i in range(2, 10, 8):
    print(i, end=" ")

#!/usr/bin/python3
not_print = (10, 20, 30, 40, 50, 60, 70, 80)
for num in range(0, 90):
    if num in not_print:
        continue
    else:
        if num != 89:
            print("{:02d}, ".format(num), end='')
        else:
            print("{:02d}\n".format(num))