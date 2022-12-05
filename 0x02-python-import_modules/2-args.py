#!/usr/bin/python3.4
if __name__ == '__main__':
    from sys import argv

    i = len(argv) - 1
    if i == 0:
        print('{} arguments.'.format(i))
    elif i == 1:
        print('{} argument:'.format(i))
    else:
        print('{} argument:'.format(i))

    if i >= 1:
        i = 0
        for j in argv:
            if i != 0:
                print('{}: {}'.format(i, j))
            i += 1
