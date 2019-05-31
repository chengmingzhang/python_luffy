# coding=utf-8
# time:2019-05-31

old_str = 'girl'
new_str = '女孩'
f = open(file='staff_table', mode='r+', encoding='utf-8')
data = f.readlines()
print(data)
f.truncate(0)
for line in data:
    if old_str in line:
        new_line = line.replace(old_str, new_str)
        print(new_line)
        f.write(new_line)
    else:
        f.write(line)
f.close()
