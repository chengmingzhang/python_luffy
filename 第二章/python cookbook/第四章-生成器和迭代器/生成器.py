# coding=utf-8
# time:2019/6/1

def frange(start, stop, step):
    x = start
    while start < stop:
        yield x
        x += step

a = frange(1,4,0.5)
print(a)
print(next(a))
print(next(a))