# -*- coding: utf-8 -*-
'''
Created on Apr 4, 2012

@author: geraldo
'''
from parser_xml import MyParser
import requests

class BoxDotCom:
    url = 'https://www.box.net/api/1.0/rest?%s'

    def __init__(self, api_key):
        self.api_key = api_key
        
    def getTicket(self):
        complement = 'action=get_ticket&api_key=%s' % self.api_key
        getTicket = self.url % complement
        result = requests.get(getTicket)
        a = MyParser()
        a.parse(result.text)
        return result.text
    
    def login(self):
        pass
    
    def logout(self):
        pass
    
    def get_account_info(self):
        pass
    
    
api_key = '20c7b3zjjt5g66ermxiarf35lcs24pcz'
test = BoxDotCom(api_key)
test.getTicket()