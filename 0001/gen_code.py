#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   gen_code.py
@Time    :   2023/05/29 20:37:16
@Author  :   XuDong
@Description:  生成随机的优惠券
'''
import random
import string
from typing import List


def gen_random_code(length:int, num:int)->List:
    '''生成num个长度为lenght的随机优惠券
    
    '''
    if length < 20:
        print('建议长度大于20个字符')
        return None
    
    if num < 1:
        print('至少生成1个优惠券')
        return None
    
    code_list = set()
    
    while (len(code_list) < num):
        ran_str = ''.join(random.sample(string.ascii_letters+string.digits, length))
        code_list.add(ran_str)
        
    return list(code_list)


if __name__ == "__main__":
    codes = gen_random_code(20, 200)
    for code in codes:
        print(code)
    

