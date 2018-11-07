#-*- coding:utf-8 -*-
#########################################################################
# File Name: 04_pythonic_frame_style.py
# Author: Shen Bo
# mail: Bo.A.Shen@alcatel-sbell.com.cn
# Created Time: Tue Nov  6 10:36:35 2018
#########################################################################
#!usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/index.html')

def hello():
    return "Hello world"

if __name__ == "__main__":
    app.run()
