#!/usr/bin/python
import logging
from utility import *
import re
import user_input

#Global data sepcific for the testsuit
TEST_DATA_FILE = "test_data.xml"
DICT_ROOT = "Test_data"
PASSED = "testcase passed"
FAILED = "testcase failed"
LOGFILE = "CLI_testSuit.log"

TEST_SUIT = "CIPHER"

TEST_DATA = parseXML_to_dict(TEST_DATA_FILE)[DICT_ROOT][TEST_SUIT]

##############################################################################
#Test case 1
#Description "Checking for manual sync in omsas from admin"
##############################################################################
def TC01():
 testCase = "TC01"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output1 = run_command1(testData["cmd1"], user_input.caas_user)
 pattern = "Failed to synchronize OSS users"
 logging.debug(testData["cmd1"])
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(FAILED)
 else:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')

##############################################################################
#Test case 2 
#Description "Verification of Auto Sync for CPP Nodes"
##############################################################################
def TC02():
 testCase = "TC02"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output1 = run_command1(testData["cmd1"], user_input.caas_user)
 pattern = user_input.cpp_node_default
 logging.debug(testData["cmd1"])
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 3 
#Description "Verification of Auto Sync for Radio Nodes"
##############################################################################
def TC03():
 testCase = "TC03"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output1 = run_command1(testData["cmd1"], user_input.caas_user)
 pattern = user_input.radio_node_default
 logging.debug(testData["cmd1"])
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 4 
#Description "Verification of Auto Sync for radio_t_node"
##############################################################################
def TC04():
 testCase = "TC04"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output1 = run_command1(testData["cmd1"], user_input.caas_user)
 pattern = user_input.radio_t_node_default
 logging.debug(testData["cmd1"])
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 5 
#Description "Verification of Auto Sync for STN Nodes"
##############################################################################
def TC05():
 testCase = "TC05"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output1 = run_command1(testData["cmd1"], user_input.caas_user)
 pattern = user_input.stn_node_default
 logging.debug(testData["cmd1"])
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 6 
#Description "Verification of Auto Sync for Pico Nodes"
##############################################################################
def TC06():
 testCase = "TC06"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output1 = run_command1(testData["cmd1"], user_input.caas_user)
 pattern = user_input.pico_node_default
 logging.debug(testData["cmd1"])
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
##############################################################################
#Test case 07
#Description:326))Verification of help command for cipher per node feature(set command)
##############################################################################
def TC07(): 
 testCase = "TC07"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 output = run_command(testData["cmd"])
 logging.debug(testData["cmd"])
 logging.debug(output)
 pattern = "pkiAdmin ciphers cred list           - List cipher information for End Entity certificates."

 if re.search(pattern,output):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
##############################################################################
#Test case 08
#Description:259))Verification to list the credentials for com_ecim
##############################################################################
def TC08(): 
 testCase = "TC08"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 output = run_command1(testData["cmd"],user_input.caas_user)
 logging.debug(testData["cmd"])
 logging.debug(output)
 pattern = "valid"

 if re.search(pattern,output):
        logging.debug(PASSED) 
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
##############################################################################
#Test case 9
#Description:298))Verification for list the TLS node credentials for single ERBS Node
##############################################################################
def TC09(): 
 testCase = "TC09"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 output = run_command1(testData["cmd"] + user_input.cpp_node,user_input.caas_user)
 logging.debug(testData["cmd"] + user_input.cpp_node)
 logging.debug(output)
 pattern = "CN=LTEIPSecNEcusRootCA,O=Ericsson"

 if re.search(pattern,output):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
##############################################################################
#Test case 10
#Description:298))Verification for list the TLS node credentials for single ERBS Node
##############################################################################
def TC10(): 
 testCase = "TC10"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 output = run_command1(testData["cmd"] + user_input.cpp_node,user_input.caas_user)
 logging.debug(testData["cmd"] + user_input.cpp_node)
 logging.debug(output)
 pattern = "CN=ossmasterNECertCA"

 if re.search(pattern,output):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)




