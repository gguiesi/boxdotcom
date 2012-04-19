'''
Created on Apr 19, 2012

@author: geraldo
'''
import unittest
import boxdotcom

class Test(unittest.TestCase):


    def setUp(self):
        self.box = boxdotcom.BoxDotCom()
        self.box.get_ticket()
        pass


    def tearDown(self):
        self.box.logout()
        pass


    def testName(self):
        print 'passou'
        pass
    
    def test_validate_ticket(self):
        self.box.validateTicket()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()