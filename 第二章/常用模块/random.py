# coding=utf-8
# time:2019/5/31

import random

character = [chr(i) for i in range(97, 123)]
character_str = ''.join(character)
number = [str(i) for i in range(10)]
number_str = ''.join(number)

verification_code = random.sample(character_str + number_str, 4)
print(''.join(verification_code))
