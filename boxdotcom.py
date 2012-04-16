# -*- coding: utf-8 -*-
'''
Created on Apr 4, 2012

@author: geraldo
'''
from parser_xml import MyParser
import requests

class BoxDotCom:
    service_url = 'https://www.box.net/api/1.0/rest?%s'
    ticket = None

    def __init__(self, api_key):
        self.api_key = api_key
    
    '''
    Esse método pega a ticket e o usa para fazer todos os serviços.
    Após possuir o ticket é necessário validá-lo
    '''
    def getTicket(self):
        parser = MyParser()
        complement = 'action=get_ticket&api_key=%s' % self.api_key
        request_url = self.service_url % complement
        result = requests.get(request_url)
        self.ticket = parser.getTicket(result.text)
        print 'ticket: %s' % self.ticket
        return self.ticket
    
    # Deve ser usado o serviço: http://developers.box.net/w/page/12923930/ApiFunction_get_auth_token#REST
    def login(self):
        parser = MyParser()
        if self.ticket == None:
            self.getTicket()
            # fazer um método para abrir um browser e validar a senha.
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
#test.getTicket()
print test.login()
