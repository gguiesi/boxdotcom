# -*- coding: utf-8 -*-
'''
Created on Apr 4, 2012

@author: geraldo
'''
from xml.dom.minidom import parseString


class MyParser:
    
#    mudar o método para devolver um dicionário com as tags existentes
    def getText(self, nodelist):
        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return ''.join(rc)
        
    
    def getTicket(self, result):
        dom = parseString(result)
#        status = self.getText((dom.getElementsByTagName('status')[0]).childNodes)
        ticket = self.getText((dom.getElementsByTagName('ticket')[0]).childNodes)
        return ticket
    
    def getAuthToken(self, result):
        dom = parseString(result)
        auth_token = self.getText((dom.getElementsByTagName('auth_token')[0]).childNodes)
        return auth_token
