# _*_ coding: utf-8 _*_

import os
import csv

def work(x, y):
    print x + ' work已调用'
    os.mkdir('../done/' + x)
    mx = len(y)
    n = 1
    temp = ['']
    city = []

    for addr in y:
        with open(addr, 'rb') as fi:
            content = csv.reader(fi)
            for row in content:
                if len(row) < 5:
                    continue
                elif content.line_num == 1:
                    if temp[0] != '':
                        continue
                    else:
                        temp = row[:3] + row[4:]
                # 排除第一行 ,顺带将fields添加进temp

                elif '2015' in row[0] and row[3] == '':
                    with open('../done/' + x + '/' + row[2] + '.csv', 'ab') as fo:
                        writer = csv.writer(fo)
                        if row[2] not in city:
                            writer.writerow(temp)
                            city.append(row[2])
                        writer.writerow(row[:3] + row[4:])

        print x + '已完成' + str(n) + '/' + str(mx)
        n += 1

    print x + '全部完成'

if __name__ == '__main__':
    t = os.listdir('./eg')[1]
    x = t[:t.index('_')]
    y = []
    y.append('./eg/' + t)
    work(x ,y)
