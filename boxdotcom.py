# -*- coding: utf-8 -*-
'''
Created on Apr 4, 2012

@author: geraldo
'''
from parser_xml import MyParser
import os
import requests

class BoxDotCom:
    service_url = 'https://www.box.net/api/1.0/rest?%s'
    ticket = None
    api_key = '20c7b3zjjt5g66ermxiarf35lcs24pcz'
    auth_token = None
    
    def __init__(self, api_key=api_key):
        self.api_key = api_key
    
    '''
    Esse método pega a ticket e o usa para fazer todos os serviços.
    Após possuir o ticket é necessário validá-lo
    '''
    def get_ticket(self):
        parser = MyParser()
        complement = 'action=get_ticket&api_key=%s' % self.api_key
        request_url = self.service_url % complement
        result = requests.get(request_url)
        self.ticket = parser.getTicket(result.text)
        print 'ticket: %s' % self.ticket
        return self.ticket
    
    '''
    Recupera o auth_token do box
    '''
    def get_auth_token(self):
        parser = MyParser()
#        if self.ticket == None:
#            self.getTicket()
#            self.validateTicket()
            # fazer um método para abrir um browser e validar a senha.
        complement = 'action=get_auth_token&api_key=%s&ticket=%s' % (self.api_key, self.ticket)
        request_url = self.service_url % complement
        result = requests.get(request_url)
        self.auth_token = parser.getAuthToken(result.text)
        return self.auth_token
    
    '''
    Efetua o logout da aplicação
    '''
    def logout(self):
        self.ticket = None
    
    '''
    Recupera a árvore de arquivos do box
    '''
    def get_account_tree(self, api_key=api_key, auth_token=auth_token, folder_id=0, params='onelevel'):
        url = '%saction=get_account_tree&api_key=%s&auth_token=%s&folder_id=%s&params=%s' % (self.service_url, api_key, auth_token, folder_id, params)
        result = requests.get(url)
        return result.text
    
    '''
    Abre o browser e valida o ticket
    '''
    def validateTicket(self):
        url = 'https://www.box.net/api/1.0/auth/%s' % self.ticket
        os.system('/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --args %s' % url)
    
    '''
    cria um pasta
    '''
    def create_folder(self, api_key=api_key, auth_token=auth_token, parent_id=0, name='new folder', share=0):
        url = '%saction=create_folder&api_key=%s&auth_token=%s&parent_id=%s&name=%s&share=%s' % (api_key, auth_token, parent_id, name, share)
        result = requests.get(url)
        return result.text
    
#api_key = '20c7b3zjjt5g66ermxiarf35lcs24pcz'
#test = BoxDotCom(api_key)
#print test.login()
