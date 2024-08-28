#!/usr/bin/python
import logging
from utility import *
import re

#Global data sepcific for the testsuit
TEST_DATA_FILE = "test_data.xml"
DICT_ROOT = "Test_data"
PASSED = "testcase passed"
FAILED = "testcase failed"
LOGFILE = "CLI_testSuit.log"

TEST_SUIT = "CRLTesting"

TEST_DATA = parseXML_to_dict(TEST_DATA_FILE)[DICT_ROOT][TEST_SUIT]

##############################################################################
#Test case 01
#Description "Verification of help command for CRL expiry period"
##############################################################################
def TC01(): 
 testCase = "TC01"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 output1 = run_command(testData["cmd1"])
 pattern = "pkiAdmin crl expperiod          - Manage CRL expiration period"
 logging.debug(testData["cmd1"])
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 02
#Description:"Verification of command to get CRL expiry period"
##############################################################################
def TC02(): 
 testCase = "TC02"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 output1 = run_command(testData["cmd1"])
 pattern = "AdminCA1                       1d"
 logging.debug(testData["cmd1"])
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 3
#Description:"Verification of command to set CRL expiry period" 
##############################################################################
def TC03(): 
 testCase = "TC03"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 output1 = run_command(testData["cmd1"])
 output2 = run_command(testData["cmd2"])
 output3 = run_command(testData["cmd3"])
 pattern = "AdminCA1                       30d"
 logging.debug(testData["cmd1"])
 logging.debug(output1)
 logging.debug(testData["cmd2"])
 logging.debug(output2)

 if re.search(pattern,output2):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 04
#Description:"Verification of help command for CRL generation"
##############################################################################
def TC04(): 
 testCase = "TC04"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 output1 = run_command(testData["cmd1"])
 pattern = "pkiAdmin crl generate           - Trigger immediate CRL generation"
 logging.debug(testData["cmd1"])
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 05
#Description:"Verification of help command for CRL generateperiod"
##############################################################################
def TC05(): 
 testCase = "TC05"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 output1 = run_command(testData["cmd1"])
 pattern = "pkiAdmin crl generateperiod     - Manage CRL generation period"
 logging.debug(testData["cmd1"])
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 06
#Description:"Verification of command to get CRL generation period"
##############################################################################
def TC06(): 
 testCase = "TC06"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 output1 = run_command(testData["cmd1"])
 pattern = "CAname                         Generation Period"
 logging.debug(testData["cmd1"])
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

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
