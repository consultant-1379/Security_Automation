#!/usr/bin/python
import logging
from utility import *
import re
import user_input
import os
import time

#Global data sepcific for the testsuit
TEST_DATA_FILE = "test_data.xml"
DICT_ROOT = "Test_data"
PASSED = "testcase passed"
FAILED = "testcase failed"
LOGFILE = "CLI_testSuit.log"

TEST_SUIT = "Telstra"

TEST_DATA = parseXML_to_dict(TEST_DATA_FILE)[DICT_ROOT][TEST_SUIT]

##############################################################################
#Test case 01
#Description: Verification of the new commands in caasAdmin CLI
##############################################################################
def TC01(): 
 testCase = "TC01"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] 
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 pattern = " caasAdmin sacpp -action <action type>  {-to <target1 target2...targetn> | -file <file path>}  [ -ossUser <user> ] [-out <out file>]"

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
	
##############################################################################
#Test case 02
#Description:  Activate sftp and ssh on single ERBS node when node is in SL1
##############################################################################
def TC02(): 
 testCase = "TC02"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==1:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
 

##############################################################################
#Test case 03
#Description: Activate sftp and ssh on Multiple ERBS nodes when node is in SL1
##############################################################################
def TC03(): 
 testCase = "TC03"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node + user_input.erbs_node1
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==1:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
 

##############################################################################
#Test case 04
#Description: Activate sftp and ssh on Multiple Mixed nodes when node is in SL1
##############################################################################
def TC04(): 
 testCase = "TC04"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node + user_input.rnc_node + user_input.rbs_node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==1:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
 

##############################################################################
#Test case 05
#Description: Dectivate sftp and ssh on single ERBS node when node is in SL1
##############################################################################
def TC05(): 
 testCase = "TC05"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 str = testData["cmd1"] + user_input.erbs_node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==1:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)

##############################################################################
#Test case 06
#Description: Deactivate sftp and ssh on Multiple ERBS nodes when node is in SL1
##############################################################################
def TC06(): 
 testCase = "TC06"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node + user_input.erbs_node1
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==1:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
 
 
##############################################################################
#Test case 07
#Description: Deactivate sftp and ssh on Multiple Mixed nodes when node is in SL1
##############################################################################
def TC07(): 
 testCase = "TC07"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node + user_input.rnc_node + user_input.rbs_node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==1:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)


##############################################################################
#Test case 08
#Description: Activating SL2 for Single ERBS Node
##############################################################################
def TC08(): 
 testCase = "TC08"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==1:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
        

##############################################################################
#Test case 09
#Description: Activating SL2 for Multiple ERBS Nodes
##############################################################################
def TC09(): 
 testCase = "TC09"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 str = testData["cmd1"] + user_input.erbs_node + user_input.erbs_node1
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==1:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
 

##############################################################################
#Test case 10
#Description: Activating SL2 for Multiple Mixed Nodes
##############################################################################
def TC10(): 
 testCase = "TC10"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node + user_input.rnc_node + user_input.rbs_node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==1:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
	
##############################################################################
#Test case 11
#Description: Activating SL2 for Single ERBS Node which is already in SL2
##############################################################################
def TC11(): 
 testCase = "TC11"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str1 = testData["cmd1"] + user_input.erbs_node
 output1 = run_command1(str1, user_input.caas_user)
 logging.debug(str1)
 logging.debug(output1)
 pattern = " Operational Security Level                        : 2"
 if (re.search(pattern,output1)):
 	str2 = testData["cmd2"] + user_input.erbs_node
 	output2 = run_command1(str2, user_input.caas_user)
 	logging.debug(str2)
 	logging.debug(output2)
 	output2_list = output2.split()
 	job_id = output2_list[-1]
 	k = 0
 	while(k == 0):
 		time.sleep(60)
 		k = job_status(job_id)
 		logging.debug(k)

 	if k==1:
        	logging.debug(PASSED)
        	update_result_file(TEST_SUIT, testCase, 'pass')
 	else:
		logging.debug(FAILED)
 else:
	logging.debug("The pre-requesite of the node is not met, the node should be in SL2")
	logging.debug(FAILED)

##############################################################################
#Test case 12
#Description: Verification of security level status of the single ERBS Node 
##############################################################################
def TC12(): 
 testCase = "TC12"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 str = testData["cmd1"] + user_input.erbs_node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 pattern = " Result: Succesful "

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)

##############################################################################
#Test case 13
#Description: Verification of security level status of the Multiple ERBS Nodes 
##############################################################################
def TC13(): 
 testCase = "TC13"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 str = testData["cmd1"] + user_input.erbs_node + user_input.erbs_node1
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 pattern = " Result: Succesful "
 k=output1.count(pattern)
 logging.debug(k)

 if k==2:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)

##############################################################################
#Test case 14
#Description: Verification of security level status of Multiple Mixed Nodes
##############################################################################
def TC14(): 
 testCase = "TC14"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node + user_input.rnc_node + user_input.rbs_node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 pattern = " Result: Succesful "
 k=output1.count(pattern)
 logging.debug(k)

 if k==3:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
 

##############################################################################
#Test case 15
#Description: Verification of security level status in OSS Database for the single ERBS node
##############################################################################
def TC15(): 
 testCase = "TC15"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 str = testData["cmd1"] + user_input.erbs_node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 pattern = " Result: Succesful  "

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)

##############################################################################
#Test case 16
#Description: Verification of security level status in OSS Database for Multiple ERBS Nodes
##############################################################################
def TC16(): 
 testCase = "TC16"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node + user_input.erbs_node1
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 pattern = " Result: Succesful  "
 k=output1.count(pattern)
 logging.debug(k)

 if k==2:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
 

##############################################################################
#Test case 17
#Description: Verification of security level status in OSS Database for Multiple Mixed Nodes
##############################################################################
def TC17(): 
 testCase = "TC17"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node + user_input.rnc_node + user_input.rbs_node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 pattern = " Result: Succesful  "
 k=output1.count(pattern)
 logging.debug(k)

 if k==3:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
 
##############################################################################
#Test case 18
#Description: Verification of Node configuration sync for the single ERBS node 
##############################################################################
def TC18(): 
 testCase = "TC18"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 pattern = " Result: Succesful "

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
 

##############################################################################
#Test case 19
#Description: Verification of Node configuration sync for Multiple ERBS nodes 
##############################################################################
def TC19(): 
 testCase = "TC19"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node + user_input.erbs_node1
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 pattern = " Result: Succesful "
 k=output1.count(pattern)
 logging.debug(k)

 if k==2:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
 

##############################################################################
#Test case 20
#Description: Verification of Node configuration sync for Multiple Mixed Nodes 
##############################################################################
def TC20(): 
 testCase = "TC20"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node + user_input.rnc_node + user_input.rbs_node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 pattern = " Result: Succesful "
 k=output1.count(pattern)
 logging.debug(k)

 if k==3:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)


##############################################################################
#Test case 21
#Description: Activate sftp and ssh single ERBS node which is already activated
##############################################################################
def TC21(): 
 testCase = "TC21"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==1:
	str1 = testData["cmd1"] + user_input.erbs_node 
 	output2 = run_command1(str1, user_input.caas_user)
 	logging.debug(str1)
 	logging.debug(output2)
 	output2_list = output2.split()
 	job_id = output2_list[-1]
 	k = 0
 	while(k == 0):
 		time.sleep(60)
 		k = job_status(job_id)
 		logging.debug(k)

 	if k==1:
        	logging.debug(PASSED)
        	update_result_file(TEST_SUIT, testCase, 'pass')
 	else:
		logging.debug(FAILED)
 else:
	logging.debug("The pre-requesite of the node is not met, sftp should be activated")
	logging.debug(FAILED)
 
##############################################################################
#Test case 22
#Description: Deactivate sftp and ssh single ERBS node when node is in SL2
##############################################################################
def TC22(): 
 testCase = "TC22"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str1 = testData["cmd1"] + user_input.erbs_node
 output1 = run_command1(str1, user_input.caas_user)
 logging.debug(str1)
 logging.debug(output1)
 pattern = " Operational Security Level                        : 2"
 if (re.search(pattern,output1)):
 	str2 = testData["cmd2"] + user_input.erbs_node
 	output2 = run_command1(str2, user_input.caas_user)
 	logging.debug(str2)
 	logging.debug(output2)
 	output2_list = output2.split()
 	job_id = output2_list[-1]
 	k = 0
 	while(k == 0):
 		time.sleep(60)
 		k = job_status(job_id)
 		logging.debug(k)

 	if k==1:
        	logging.debug(PASSED)
        	update_result_file(TEST_SUIT, testCase, 'pass')
 	else:
		logging.debug(FAILED)
 else:
	logging.debug("The pre-requesite of the node is not met, the node should be in SL2")
	logging.debug(FAILED)
 
##############################################################################
#Test case 23
#Description: Deactivating from SL2 to SL1 for Single ERBS Node
##############################################################################
def TC23(): 
 testCase = "TC23"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node 
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==1:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
 

##############################################################################
#Test case 24
#Description: Deactivating from SL2 to SL1 for Multiple ERBS Nodes
##############################################################################
def TC24(): 
 testCase = "TC24"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node + user_input.erbs_node1
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==1:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
 

##############################################################################
#Test case 25
#Description: Deactivating from SL2 to SL1 for Multiple Mixed Nodes
##############################################################################
def TC25(): 
 testCase = "TC25"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node + user_input.rnc_node + user_input.rbs_node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==1:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
 
##############################################################################
#Test case 26
#Description: SL2 activation for ERBS Node which is already Initial Enrolled
##############################################################################
def TC26(): 
 testCase = "TC26"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 node =user_input.erbs_node_init_enroll
 str = testData["cmd1"] + node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 job = "The job is now queued"
 if re.search(job,output1):
 	output1_list = output1.split()
 	job_id = output1_list[-1]
 	k = 0
 	while(k == 0):
 		time.sleep(60)
 		k = job_status(job_id)
 	logging.debug(k)

 	if k==1:
		str1 = testData["cmd2"] + node 
 		output2 = run_command1(str1, user_input.caas_user)
 		logging.debug(str1)
 		logging.debug(output2)
 		output2_list = output2.split()
 		job_id = output2_list[-1]
 		k = 0
 		while(k == 0):
 			time.sleep(60)
 			k = job_status(job_id)
 			logging.debug(k)

 		if k==1:
        		logging.debug(PASSED)
        		update_result_file(TEST_SUIT, testCase, 'pass')
 		else:
			logging.debug(FAILED)
 	else:
		logging.debug("The pre-requesite of the node is not met, the initial enrollment is failed")
		logging.debug(FAILED)
 else:
	logging.debug("The pre-requesite of the node is not met, the initial enrollment is failed")
	logging.debug(FAILED)


##############################################################################
#Test case 27
#Description: SL2 activation for ERBS Node which is already Initial Enrolled and trust distribution(corba) completed on node
##############################################################################
def TC27(): 
 testCase = "TC27"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 node = user_input.erbs_node_corba_peer
 str = testData["cmd1"] + node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 job = "The job is now queued"
 if re.search(job,output1):
 	output1_list = output1.split()
 	job_id = output1_list[-1]
 	k = 0
 	while(k == 0):
 		time.sleep(60)
 		k = job_status(job_id)
 	logging.debug(k)

 	if k==1:
		str1 = testData["cmd2"] + node 
 		output2 = run_command1(str1, user_input.caas_user)
 		logging.debug(str1)
 		logging.debug(output2)
 		output2_list = output2.split()
 		job_id = output2_list[-1]
		job_id.replace("obtained:", " ")
 		k = 0
 		while(k == 0):
 			time.sleep(60)
 			k = job_status(job_id)
 		logging.debug(k)

 		if k==1:
			str2 = testData["cmd3"] + node 
 			output3 = run_command1(str2, user_input.caas_user)
 			logging.debug(str2)
 			logging.debug(output3)
 			output3_list = output2.split()
 			job_id = output3_list[-1]
			job_id.replace("obtained:", " ")
 			k = 0
 			while(k == 0):
 				time.sleep(60)
 				k = job_status(job_id)
 			logging.debug(k)
        		if k==1:
        			logging.debug(PASSED)
        			update_result_file(TEST_SUIT, testCase, 'pass')
 			else:
				logging.debug(FAILED)
 		else:
			logging.debug("The pre-requesite of the node is not met, the corba peer distribution is failed")
			logging.debug(FAILED)
 	else:
		logging.debug("The pre-requesite of the node is not met, the initial enrollment is failed")
		logging.debug(FAILED)
 else:
	logging.debug("The pre-requesite of the node is not met, the initial enrollment is failed")
	logging.debug(FAILED) 



##############################################################################
#Test case 28
#Description: Activate sftp and ssh single ERBS node when node is not reachable
##############################################################################
def TC28(): 
 testCase = "TC28"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node_stopped
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==-1:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
 
##############################################################################
#Test case 29
#Description: Deactivate sftp and ssh single ERBS node when node is not reachable
##############################################################################
def TC29(): 
 testCase = "TC29"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 str = testData["cmd1"] + user_input.erbs_node_stopped
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==-1:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)

##############################################################################
#Test case 30
#Description: SL2 activation for single ERBS Node when the node is not reachable
##############################################################################
def TC30(): 
 testCase = "TC30"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node_stopped
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==-1:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
 
##############################################################################
#Test case 31
#Description: SL2 Deactivation for single ERBS Node when the node is not reachable
##############################################################################
def TC31(): 
 testCase = "TC31"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 str = testData["cmd1"] + user_input.erbs_node_stopped
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==-1:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
 
##############################################################################
#Test case 32
#Description: SL2 activation for Multiple mixed nodes in that one node should be in not reachable
##############################################################################
def TC32(): 
 testCase = "TC32"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node_stopped + user_input.rnc_node + user_input.rbs_node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==-1:
	str1 = testData["cmd2"] + user_input.rnc_node + user_input.rbs_node 
 	output2 = run_command1(str1, user_input.caas_user)
 	logging.debug(str1)
 	logging.debug(output2)
 	pattern = "Operational Security Level                        : 2 "
 	k=output2.count(pattern)
 	logging.debug(k)

 	if k==2:
        	logging.debug(PASSED)
        	update_result_file(TEST_SUIT, testCase, 'pass')
 	else:
		logging.debug(FAILED)
 else:
	logging.debug(FAILED)
 

##############################################################################
#Test case 33
#Description: SL2 deactivation for Multiple mixed nodes in that one node should be in not reachable
##############################################################################
def TC33(): 
 testCase = "TC33"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node_stopped + user_input.rnc_node + user_input.rbs_node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 output1_list = output1.split()
 job_id = output1_list[-1]
 k = 0
 while(k == 0):
 	time.sleep(60)
 	k = job_status(job_id)
 logging.debug(k)

 if k==-1:
	str1 = testData["cmd2"] + user_input.rnc_node + user_input.rbs_node 
 	output2 = run_command1(str1, user_input.caas_user)
 	logging.debug(str1)
 	logging.debug(output2)
 	pattern = "Operational Security Level                        : 1"
 	k=output2.count(pattern)
 	logging.debug(k)

 	if k==2:
        	logging.debug(PASSED)
        	update_result_file(TEST_SUIT, testCase, 'pass')
 	else:
		logging.debug(FAILED)
 else:
	logging.debug(FAILED)
 
##############################################################################
#Test case 34
#Description: Verification of Node configuration sync for single ERBS Node when node is not reachable
##############################################################################
def TC34(): 
 testCase = "TC34"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.erbs_node_stopped
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 pattern = " Result: Succesful"

 if re.search(pattern,output1):
	logging.debug(FAILED)
 else:
	logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 

##############################################################################
#Test case 35
#Description: Verification of Node configuration sync for the Multiple  mixed nodes file as input where some nodes are in not reachable
##############################################################################
def TC35(): 
 testCase = "TC35"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 str = testData["cmd1"] + user_input.erbs_node_stopped + user_input.rbs_node + user_input.rnc_node
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 pattern = " Result: Succesful "
 k=output1.count(pattern)
 logging.debug(k)

 if k==2:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
	logging.debug(FAILED)
 

##############################################################################
#Test case 36
#Description "Fingerprint Verification for NECertCA.pem"
##############################################################################
def TC36(): 
 testCase = "TC36"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 37
#Description:
##############################################################################
def TC37(): 
 testCase = "TC37"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 38
#Description:
##############################################################################
def TC38(): 
 testCase = "TC38"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 39
#Description:
##############################################################################
def TC39(): 
 testCase = "TC39"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 40
#Description:
##############################################################################
def TC40(): 
 testCase = "TC40"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 41
#Description:
##############################################################################
def TC41(): 
 testCase = "TC41"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 42
#Description "Fingerprint Verification for NECertCA.pem"
##############################################################################
def TC42(): 
 testCase = "TC42"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 43
#Description:
##############################################################################
def TC43(): 
 testCase = "TC43"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 44
#Description:
##############################################################################
def TC44(): 
 testCase = "TC44"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 

##############################################################################
#Test case 45
#Description:
##############################################################################
def TC45(): 
 testCase = "TC45"	
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)


##############################################################################
#Test case 
#Description:
##############################################################################
def job_status(job_id):
 testCase = "TC_job_status"	
 #testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 str1= "caasAdmin l j | grep " + job_id
 output = run_command1(str1, user_input.caas_user)
 pattern = "completed"
 pattern1 = "processing"
 pattern2 = "failed"
 logging.debug(str1)
 logging.debug(output)
 k=-1
 
 if re.search(pattern1,output):
	k=0
 else:
 	if re.search(pattern, output):
		k=1	
	else:
		k=-1
 return k	

#######################################################################################

TC24();
TC25();	
TC26();
TC27();	

