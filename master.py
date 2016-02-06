# _*_ coding: utf-8 _*_

from init import init
from worker import work
from multiprocessing import Pool

p = Pool()
d = init()
n = 0
mx = len(d.keys())

for i in d:
    p.apply_async(work, args=(i, d[i]))
    print '*_*_*' + str(n) + '/' + str(mx) + '任务已添加进程'
    n += 1

print '!!!!!所有任务已添加进程!!!!!\n'
p.close()
p.join()

print  '完成'