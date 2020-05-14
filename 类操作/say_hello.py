#!usr/bin/env python3
# -*-conding:UTF-8-*-

"""模块demo"""
__author__ = 'agassiz'

import sys


def test():
    print(__name__)
    args = sys.argv
    if len(args) == 1:
        print('hello,world!')
    elif len(args) == 2:
        print('hello {0}'.format(args[1]))
    else:
        print('Too many argments:!{0}'.format(args))


if __name__ == '__main__':
    test()
