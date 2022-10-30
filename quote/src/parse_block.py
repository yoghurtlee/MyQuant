#!/usr/bin/env python3
# encoding: utf-8

from struct import *
import os
import sys

PATH = './tdxzs3.cfg'

BK_MAP = {'hy': '2', 'dq': '3', 'gn': '4', 'fg': '5', 'yjhy': '12', 'zs': '6'}
EX_MAP = {'0': 'sz.', '1': 'sh.', '2': 'bj.'}

def read_file_loc(file_name, splits):
    with open(file_name, 'r') as f:
        buf_list = f.read().split('\n')
    return [x.split(splits) for x in buf_list[:-1]]






