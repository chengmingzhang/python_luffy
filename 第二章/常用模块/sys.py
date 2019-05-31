# coding=utf-8
# time:2019/5/31
# python filename argv1 argv2,sys.argv可以将输入屏幕的参数传递给代码，sys.argv[0]代表的是文件名称
import sys


def hello():
    print('hello,%s,%s' % (sys.argv[1], sys.argv[2]))


hello()
