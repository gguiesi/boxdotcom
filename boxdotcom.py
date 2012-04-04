# -*- coding: utf-8 -*-
'''
Created on Apr 4, 2012

@author: geraldo
'''
from parser_xml import MyParser
import requests

class BoxDotCom:
    service_url = 'https://www.box.net/api/1.0/rest?%s'

    def __init__(self, api_key):
        self.api_key = api_key
        
    def getTicket(self):
        parser = MyParser()
        complement = 'action=get_ticket&api_key=%s' % self.api_key
        request_url = self.service_url % complement
        result = requests.get(request_url)
        self.ticket = parser.getTicket(result.text)
        return self.ticket
    
    def login(self):
        self.getTicket()
        parser = MyParser()
        complement = 'action=get_auth_token&api_key=%s&ticket=%s' % (self.api_key, self.ticket)
        request_url = self.service_url % complement
        result = requests.get(request_url)
        self.auth_token = parser.getAuthToken(result.text)
    
    def logout(self):
        self.ticket = None
    
    def get_account_info(self):
        pass
    
    
api_key = '20c7b3zjjt5g66ermxiarf35lcs24pcz'
test = BoxDotCom(api_key)
print test.login()
