#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   save_coupon.py
@Time    :   2023/05/29 21:24:10
@Author  :   XuDong
@Description: 保存0001中生成的优惠券  
'''
import random
import string
from typing import List

import MySQLdb


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


def save_coupon_in_db(coupons:List):
    '''将生成的优惠券存储到mysql数据库中
    '''
    db = MySQLdb.connect(
        host='localhost',
        user='root',
        password='123456',
        database='mycode'
    )
    
    try:
        cursor = db.cursor()
        cursor.executemany('INSERT INTO coupon(code) values(%s) ', coupons)
        db.commit()
        print("插入完成")
    except Exception as e:
        db.rollback()
        print('插入失败')
    finally:
        db.close()

if __name__ == "__main__":
    codes = gen_random_code(20, 200)
    for code in codes:
        print(code)
    save_coupon_in_db(codes)
