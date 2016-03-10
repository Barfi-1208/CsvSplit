# -*- coding: utf-8 -*-
import os

'''
将目标文件用dict来省份分类,dict['省份'] = [省份_xxx.csv, etc...],dict用于master进程分配任务
'''
def init():
    ans = {}
    name = ''
    target = os.listdir('../work')
    for i in target:
        name = i[:i.index('_')]
        if name not in ans:
            ans[name] = [('../work/' + i)]
        else:
            ans[name].append('../work/' + i)

    ans.pop('.DS')
    return ans

if __name__ == '__main__':
    temp = init()
    for i in temp:
        for j in temp[i]:
            print j
