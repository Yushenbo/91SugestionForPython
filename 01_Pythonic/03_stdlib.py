#-*- coding:utf-8 -*-
#########################################################################
# File Name: 03_stdlib.py
# Author: Shen Bo
# mail: Bo.A.Shen@alcatel-sbell.com.cn
# Created Time: Tue Nov  6 09:15:33 2018
#########################################################################
#!usr/bin/env python3

value = {'greet': 'Hello world', 'language': 'Python'}
print('%(greet)s from %(language)s.' % value)

print('style2 ==> {greet} from {language}.'.format(greet = 'Hello world',
    language = 'Python'))

