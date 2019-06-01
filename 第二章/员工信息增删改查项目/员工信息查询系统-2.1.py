# coding=utf-8

import numpy as np

columns = ['id', 'name', 'age', 'phone', 'dept', 'enroll_date']  # 文件的列名称
symbol = ['>', '<', '=', 'like', '<=', '>=']  # 运算符号


def read_file():  # 读取文件，将文件内容处理，生成一个用户信息字典user_dic
    f = open(file='staff_table', mode='r+', encoding='utf-8')
    user_dic = {'id': [], 'name': [], 'age': [], 'phone': [], 'dept': [], 'enroll_date': []}
    table = [i.strip() for i in f.readlines()]
    for i in table:
        user_dic['id'].append(i.split(',')[0])
        user_dic['name'].append(i.split(',')[1])
        user_dic['age'].append(i.split(',')[2])
        user_dic['phone'].append(i.split(',')[3])
        user_dic['dept'].append(i.split(',')[4])
        user_dic['enroll_date'].append(i.split(',')[5])
    f.close()
    return user_dic


def read_input():  # 将输入信息进行分析，保证输入的字符串符合查询语法，得到正确的查询语列表s
    while True:
        condition = input('查询语句:>>>').strip()
        s = condition.split(' ')
        if len(s) != 8 or s[0] != 'find' or s[2] != 'from' or s[3] != 'staff_table' or s[4] != 'where':
            print('语法错误1')
        elif set(s[1].split(',')) & set(columns) != set(s[1].split(',')) and s[1] != '*':
            print('语法错误2')
        elif s[5] not in columns or s[6] not in symbol:
            print('语法错误3')
        else:
            return s  # s = ['find', 'name,age', 'from', 'staff_table', 'where', 'age', '>', '22']


def find():  #
    s = read_input()
    condition_left = s[1].split(',')  # name,age得到列表[name, age]
    result_index = []  # 如年龄大于22的索引值
    new_s = s
    if new_s[6] == '=':
        new_s[6] = '=='
    elif new_s[6] == 'like':
        new_s[6] = 'in'
    print(new_s)
    new_list = read_input()
    for i, j in enumerate(new_list[new_s[5]]):
        if new_s[6] == 'in':
            condition_right = '''%s %s '%s' ''' % (new_s[7], new_s[6], j)  # 如"2013" in '2013-04-01'
        elif new_s[7].isdigit():
            condition_right = j + new_s[6] + new_s[7]  # 只有数字才能比较大小，将字符串起来如'23>22'
        else:
            condition_right = ''' '%s' %s %s''' % (j, new_s[6], new_s[7])  # 如果是字符串，就串起来如'IT' == "IT"
        print(condition_right)

        if eval(condition_right):  # 如'age' + '>' + '22'
            result_index.append(i)  # 得到满足条件的索引值，如满足大于22的年纪索引
        else:
            continue
    result = []  # 将得到的索引值的结果存入列表
    if condition_left == ['*']:
        condition_left = columns
    for k in condition_left:
        arr = []
        for l in result_index:
            arr.append(new_list[k][l])
        result.append(arr)  # result的结果是这样的[list1,list2...]

    result = np.array(result).transpose()  # 得到结果[[name,name,name]，[age,age,age]]将结果列表进行转置，得到我们最终需要的结果need
    print('您查询的结果为:')
    for need in result:
        print(','.join(need))


def add():
    while True:
        add_input = input('创建员工记录语句:')
        if add_input.startswith('add staff_table'):
            if len(add_input.split('staff_table')[1].strip().split(',')) != 5:
                print('语法错误')
            else:
                id_list = [int(i) for i in read_file()['id']]  # id列表
                phone_list = [i for i in read_file()['phone']]  # 电话号码列表
                right = add_input.split('staff_table')[1].strip()  # Alex Li,25,134435344,IT,2015-10-29
                phone_right = right.split(',')[2]  # 获取输入的电话号码
                if phone_right in phone_list:
                    print('phone number %s is exits' % phone_right)
                else:
                    r = open(file='staff_table', mode='r+', encoding='utf-8')
                    r.read()
                    r.write('\n%s,%s' % (str(max(id_list) + 1), right))
                    r.close()
        elif add_input == 'q':
            print('推出')
        else:
            print('语法错误')


find()
