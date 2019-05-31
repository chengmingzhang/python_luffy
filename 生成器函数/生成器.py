# coding=utf-8
# time:2019-05-31

# 生成器方式一
a = (i for i in range(100) if i % 3 == 0 and i % 4 == 0)
print(a)  # 结果：<generator object <genexpr> at 0x0000000001D62F48>，即这就是一个生成器，只需将列表生成式的[]修改为()

# 生成器函数，函数中带有关键字yield，函数即为一个生成器函数


def generator():
    n = 3
    while True:
        print('starting...')
        s = yield n
        if s == 'stop':
            print('程序停止')
            break
        else:
            n += 1
            print(s)


f = generator()  # 执行生成器函数，第一次得到的是一个生成器对象
print(next(f))
print(next(f))
print(f.send(8))
print(f.send('stop'))
