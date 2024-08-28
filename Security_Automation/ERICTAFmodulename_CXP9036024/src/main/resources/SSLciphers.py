#!/usr/bin/python

###################################################################################
#  *********************************************************************
#  *COPYRIGHT:
#  *Author: Manu Prasad(xmanupr)
#  *********************************************************************
#	SSL-ciphers test suit.
#	
###################################################################################

from utility import *
import logging

TEST_DATA_FILE = "test_data.xml"
DICT_ROOT = "Test_data"
PASSED = "testcase passed"
FAILED = "testcase failed"
LOGFILE = "CLI_testSuit.log"

TEST_SUIT = "SSL-ciphers"

TEST_DATA = parseXML_to_dict(TEST_DATA_FILE)[DICT_ROOT][TEST_SUIT]

##############################################################################
#Test case 01
#Description:
##############################################################################
def TC01(): 
 testCase = "TC01"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 02
#Description:
##############################################################################
def TC02(): 
 testCase = "TC02"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

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
	
	output = run_command(testData["cmd"])
	logging.debug(testData["cmd"])
	logging.debug(output)

	if output == testData["compareString"]:
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
 

##############################################################################
#Test case 09
#Description:
##############################################################################
def TC09(): 
 testCase = "TC09"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

