#!/usr/bin/env python3
# encoding: utf-8


from struct import *
import os
import sys


'''
filename    : 通达信K线数据文件名
output      : 存放输出数据文件名
'''
def parse_dayline(filename, output):
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
        fileline = str(int(buf[0]/10000))+'/'+str(int(buf[0]%10000/100)).zfill(2)+'/'+str(int(buf[0]%100)).zfill(2)\
                 +','+str(buf[1]/100.0)+','+str(buf[2]/100.0)\
                 +','+str(buf[3]/100.0)+','+str(buf[4]/100.0)\
                 +','+str(buf[5])+','+str(buf[6])+','+str(buf[7])+'\n'
        print(fileline)
        ofile.write(fileline)
    ofile.close()

def parse_minline(filename, output):
    SIZE = 32   # 通达信分K数据长度

    data = None
    with open(filename, 'rb') as fp:
        data = fp.read()

    ofile = open(output, 'w')

    headline = 'date,time,open,high,low,close,amount,volume,reserve\n'
    ofile.write(headline)

    length = len(data)
    for i in range(int(length/SIZE)):
        buf = unpack('HHfffffII', data[i*SIZE:(i+1)*SIZE])
        fileline = str(int(buf[0]/2048)+2004)+'/'+str(int(buf[0]%2048/100)).zfill(2)+'/'+str(buf[0]%2048%100).zfill(2)\
                 + ','+str(int(buf[1]/60)).zfill(2)+':'+str(buf[1]%60).zfill(2)+':00'\
                 + ','+str(buf[2])+','+str(buf[3])+','+str(buf[4])+','+str(buf[5])\
                 +','+str(buf[6])+','+str(buf[7])+','+str(buf[8])+'\n'
        print(fileline)
        ofile.write(fileline)
    ofile.close()

if __name__ == '__main__':
    parse_dayline('./sh000001.day', './sh000001_day.csv')
    parse_minline('./sh000001.lc1', './sh000001_min.csv')
    pass


