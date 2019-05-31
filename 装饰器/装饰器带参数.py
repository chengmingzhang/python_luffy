# coding=utf-8
# time:2019-05-31

# 1.创建装饰器函数，参数为被装饰函数
# 2.创建包装函数
# 3.包装函数中执行被装饰函数
# 4.返回包装函数
import time

username = 'zhang'
password = '123'


def decorate(func):  # 装饰器不带参数
    def inner():
        start = time.time()
        time.sleep(1)
        print('Starting...')
        func()
        print('Ending...')
        end = time.time()
        print('耗时%f秒' % (end - start))
    return inner


def decorate1(auth):  # 装饰器带参数
    def outter(func1):
        def inner():
            count = 0
            while True:
                _username = input('username:').strip()
                _password = input('password:').strip()
                if _username == username and _password == password:
                    print('Login Success, Welcome %s user' % auth)
                    func1()
                    break
                else:
                    print('username or password error')
                    count += 1
                    if count == 3:
                        print('三次错误，退出')
                        break
        return inner
    return outter


@decorate
def gen():
    arr = [i for i in range(10000) if i % 2 == 0 and i % 3 == 0]
    print(arr)


@decorate1(auth='qq')
def china():
    print('国人专区'.center(30, '-'))

china()
