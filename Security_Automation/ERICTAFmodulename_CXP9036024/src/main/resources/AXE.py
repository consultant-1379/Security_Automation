#!/usr/bin/python
import logging
from utility import *
import user_input
import re


#comment rajesh is good fellow

#Global data sepcific for the testsuit
TEST_DATA_FILE = "test_data.xml"
DICT_ROOT = "Test_data"
PASSED = "testcase passed"
FAILED = "testcase failed"
LOGFILE = "CLI_testSuit.log"

TEST_SUIT = "AXE"

TEST_DATA = parseXML_to_dict(TEST_DATA_FILE)[DICT_ROOT][TEST_SUIT]

##############################################################################
#Test case 01
#Description "Fingerprint Verification for NECertCA.pem"
##############################################################################
def TC01(): 
 testCase = "TC01"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output1 = run_command1(testData["cmd1"], user_input.caas_user)
 pattern = user_input.msc_node_default
 logging.debug(testData["cmd1"])
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED) 

##############################################################################
#Test case 02
#Description:
##############################################################################
def TC02(): 
 testCase = "TC02"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output1 = run_command1(testData["cmd2"], user_input.caas_user)
 pattern = user_input.bsc_node_default
 logging.debug(testData["cmd2"])
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED) 
 

##############################################################################
#Test case 3
#Description: 
##############################################################################
def TC03(): 
 testCase = "TC03"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 04
#Description:
##############################################################################
def TC04(): 
 testCase = "TC04"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 05
#Description:
##############################################################################
def TC05(): 
 testCase = "TC05"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 06
#Description:
##############################################################################
def TC06(): 
 testCase = "TC06"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 07
#Description:
##############################################################################
def TC07(): 
 testCase = "TC07"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 08
#Description:
##############################################################################
def TC08(): 
 testCase = "TC08"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 09
#Description:
##############################################################################
def TC09(): 
 testCase = "TC09"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 10
#Description:
##############################################################################
def TC10(): 
 testCase = "TC10"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 11
#Description:
##############################################################################
def TC11(): 
 testCase = "TC11"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 12
#Description:
##############################################################################
def TC12(): 
 testCase = "TC12"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 13
#Description "Fingerprint Verification for NECertCA.pem"
##############################################################################
def TC13(): 
 testCase = "TC13"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 14
#Description:
##############################################################################
def TC14(): 
 testCase = "TC14"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 15
#Description:
##############################################################################
def TC15(): 
 testCase = "TC15"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 16
#Description:
##############################################################################
def TC16(): 
 testCase = "TC16"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 17
#Description:
##############################################################################
def TC17(): 
 testCase = "TC17"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 


 
