#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import re

top_level=77
lnk_temp='%s- [%s](#%s)'

def load_md_file(fname):
    """load md content"""
    lines = []
    with open(fname, 'r') as file:
        lines = file.readlines()
    return lines

def generate_toc(lines):
    global top_level
    headers = [e.strip() for e in lines if re.match(r'#+', e)]
    #find top_level
    for i,h in enumerate(headers):
        ln = len(re.search(r'^#+',h).group(0))
        top_level = ln if ln < top_level else top_level
        headers[i] = re.sub(r'^#+\s*', str(ln)+' ', h)
    headers = [tr_header(h) for h in headers]
    print '\n'.join(headers)

def tr_header(header):
    global lnk_temp
    lvl, txt = re.findall(r'^(\d+) (.*)', header)[0]
    return lnk_temp%((int(lvl)-top_level)*'    ', txt, re.sub(' ','-',re.sub('[^-a-z0-9 ]','',txt.lower())))

if __name__ == '__main__':
    generate_toc(load_md_file('test/test.md'))
