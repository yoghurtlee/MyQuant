#!/usr/bin/env python3
# encoding: utf-8


from struct import *
import os
import sys


'''
filename    : 通达信K线数据文件名
output      : 存放输出数据文件名
'''
def parse_kline(filename, output):
    SIZE = 32   # 通达信日K数据长度

    data = None
    with open(filename, 'rb') as fp:
        data = fp.read()

    ofile = open(output, 'w')

    headline = 'date,open,high,low,close,amount,volume,reserve\n'
    ofile.write(headline)

    length = len(data)
    for i in range(int(length/SIZE)):
        buf = unpack('IIIIIfII', data[i*SIZE:(i+1)*SIZE])
        fileline = str(buf[0])+','+str(buf[1]/100.0)+','+str(buf[2]/100.0)\
                 +','+str(buf[3]/100.0)+','+str(buf[4]/100.0)+','+str(buf[5])\
                 +','+str(buf[6])+','+str(buf[7])+'\n'
        print(fileline)
        ofile.write(fileline)
    ofile.close()


if __name__ == '__main__':
    filename = './sh000001.day'
    output = './sh000001.csv'
    parse_kline(filename, output)
    pass


