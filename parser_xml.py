# -*- coding: utf-8 -*-
'''
Created on Apr 4, 2012

@author: geraldo
'''
from xml.dom.minidom import parseString


class MyParser:
    
    def parse(self, result):
        dom1 = parseString(result)
        return dom1
