#!/usr/bin/python
import logging
from utility import *

#Global data sepcific for the testsuit
TEST_DATA_FILE = "test_data.xml"
DICT_ROOT = "Test_data"
PASSED = "testcase passed"
FAILED = "testcase failed"
LOGFILE = "CLI_testSuit.log"

TEST_SUIT = "MULTIRAT"

TEST_DATA = parseXML_to_dict(TEST_DATA_FILE)[DICT_ROOT][TEST_SUIT]

##############################################################################
#Test case 1
#Description "Fingerprint Verification for NECertCA.pem"
##############################################################################
def TC01(): 
 testCase = "TC01"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 output1 = run_command(testData["cmd1"])
 output2 = run_command(testData["cmd2"])
 
 logging.debug(testData["cmd1"])
 logging.debug(output1)
 logging.debug(testData["cmd2"])
 logging.debug(output2)
 
 if output1 == output2:
	logging.debug(PASSED)
	update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
 
##############################################################################
#Test case 2
#Description "Fingerprint Verification for COMInfRootCA.pem"
##############################################################################
def TC02():
 testCase = "TC02"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output1 = run_command(testData["cmd1"])
 output2 = run_command(testData["cmd2"])

 logging.debug(testData["cmd1"])
 logging.debug(output1)
 logging.debug(testData["cmd2"])
 logging.debug(output2)

 if output1 == output2:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 3
#Description "Fingerprint Verification for DSCertCA.pem"
##############################################################################
def TC03():
 testCase = "TC03"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output1 = run_command(testData["cmd1"])
 output2 = run_command(testData["cmd2"])

 logging.debug(testData["cmd1"])
 logging.debug(output1)
 logging.debug(testData["cmd2"])
 logging.debug(output2)

 if output1 == output2:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 4
#Description "Fingerprint Verification for RACSACertCA.pem"
##############################################################################
def TC04():
 testCase = "TC04"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output1 = run_command(testData["cmd1"])
 output2 = run_command(testData["cmd2"])

 logging.debug(testData["cmd1"])
 logging.debug(output1)
 logging.debug(testData["cmd2"])
 logging.debug(output2)

 if output1 == output2:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 5
#Description "Fingerprint Verification for MSCertCA.pem"
##############################################################################
def TC05():
 testCase = "TC05"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output1 = run_command(testData["cmd1"])
 output2 = run_command(testData["cmd2"])

 logging.debug(testData["cmd1"])
 logging.debug(output1)
 logging.debug(testData["cmd2"])
 logging.debug(output2)

 if output1 == output2:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 6
#Description "Fingerprint Verification for RootCA.pem"
##############################################################################
def TC06():
 testCase = "TC06"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output1 = run_command(testData["cmd1"])
 output2 = run_command(testData["cmd2"])

 logging.debug(testData["cmd1"])
 logging.debug(output1)
 logging.debug(testData["cmd2"])
 logging.debug(output2)

 if output1 == output2:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 7
#Description "Fingerprint Verification for LTEIPSecSEGRootCA.pem"
##############################################################################
def TC07():
 testCase = "TC07"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output1 = run_command(testData["cmd1"])
 output2 = run_command(testData["cmd2"])

 logging.debug(testData["cmd1"])
 logging.debug(output1)
 logging.debug(testData["cmd2"])
 logging.debug(output2)

 if output1 == output2:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 8
#Description "Fingerprint Verification for LTEIPSecNEcusRootCA.pem"
##############################################################################
def TC08():
 testCase = "TC08"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output1 = run_command(testData["cmd1"])
 output2 = run_command(testData["cmd2"])

 logging.debug(testData["cmd1"])
 logging.debug(output1)
 logging.debug(testData["cmd2"])
 logging.debug(output2)

 if output1 == output2:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED) 
