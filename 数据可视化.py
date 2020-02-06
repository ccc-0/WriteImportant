'''
第一行，一个整数 N（1<=n<=20），表示这组数据的条目数。
第二行，两个字符串，用于表示数据展示在柱状图上的排序方式。第一个字符串是“Name” 或者 “Value”，表示排序的依据是数据条目的名称亦或数值；第二个字符串是 “ASC” 或者 “DESC”，表示升序或降序。
随后的 N 行，每行包含一个字符串 S 和一个数字 V，以空格分隔，表示一条数据。S 即数据条目的名称，仅包含小写字母，V 即对应的数值，是一个整数，(0<=V<=1,000,000)
'''


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def y_input():
    '''
    输入
    :returns order1, order2, entry
    '''
    print('''输入规则：
第一行，一个整数 N（1<=n<=20），表示这组数据的条目数。
第二行，两个字符串，用于表示数据展示在柱状图上的排序方式。
      第一个字符串是“Name” 或者 “Value”，表示排序的依据是数据条目的名称亦或数值；
      第二个字符串是 “ASC” 或者 “DESC”，表示升序或降序。
随后的 N 行，每行包含一个字符串S和一个数字V，以空格分隔，表示一条数据。
    S 即数据条目的名称，仅包含小写字母，V 即对应的数值，是一个整数，(0<=V<=1,000,000)
请输入：''')
    try:
        all_num = input()
        all_num = int(all_num)
        if all_num > 20 or all_num < 1:   # 整数 （1<=n<=20）
            raise NameError
        # print(all_num)
        order1, order2 = input().split()
        if order1 != 'Name' and order1 != 'Value':  # 字符串只能是“Name” 或者 “Value”
            raise NameError
        if order2 != 'ASC' and order2 != 'DESC':   # 字符串只能是 “ASC” 或者 “DESC”
            raise NameError
        # print(order1,order2)
        entry = {}   # 字典存放所有的数据
        for i in range(all_num):
            entry_name, entry_num = input('').split(' ')
            entry_num = int(entry_num)
            entry[entry_name] = entry_num
            i += 1
        # print(entry)
        return order1, order2, entry  # 以后要用
    except:
        print("格式错误，请按正确输入规则输入")


def y_output(entry_names, entry_nums):
    '''输出'''
    num_max = max(entry_nums)   # 绘制所用的数值
    name_num_list = [len(one) for one in entry_names]
    name_max_len = max(name_num_list)
    print('\u250c' + '\u2500' * name_max_len + '\u252c' + '\u2500' * 20 + '\u2510')
    i = 0
    for entry_name in entry_names:
        the_len=math.floor(entry_nums[i]/num_max*20)  #柱子的长度
        print('\u2502' + '\u0020'*(name_max_len-name_num_list[i]) + entry_name + '\u2502'
              + '\u2588'*the_len + '\u0020'*(20-the_len) + '\u2502')
        if i == len(entry_names)-1:           #最后一行例外
            print('\u2514' + '\u2500' * name_max_len + '\u2534' + '\u2500' * 20 + '\u2518')
        else:
            print('\u251c' + '\u2500'*name_max_len + '\u253c' + '\u2500'*20 + '\u2524')
        i += 1


def main():
    try:
        order1, order2, entry = y_input()
        if order1 == 'Name':   # 判断
            the_pp = 0
        else:
            the_pp = 1
        if order2 == 'ASC':
            the_flag = False
        else:
            the_flag = True
        new_entry_list = sorted(entry.items(), key=lambda d: d[the_pp], reverse=the_flag) # 排序，字典排序
        # print(new_entry_list)
        entry_names=[]  # 构建两个空列表，y_output用
        entry_nums=[]
        for name, num in new_entry_list:
            entry_names.append(name)
            entry_nums.append(num)
        # print(entry_names,entry_nums)
        y_output(entry_names, entry_nums)  # 输出
    except:
        pass


if __name__ == "__main__":
    while True:
        main()
