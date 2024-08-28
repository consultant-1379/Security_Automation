#!/usr/bin/python
import logging
from utility import *
import re
import user_input
import os
import pdb
import time

#Global data sepcific for the testsuit
TEST_DATA_FILE = "test_data.xml"
DICT_ROOT = "Test_data"
PASSED = "testcase passed"
FAILED = "testcase failed"
LOGFILE = "CLI_testSuit.log"

TEST_SUIT = "MSRBSV2"

TEST_DATA = parseXML_to_dict(TEST_DATA_FILE)[DICT_ROOT][TEST_SUIT]

##############################################################################
#Test case 01
#Description: config_renew for single radio node (mode automatic)
##############################################################################
def TC01(): 
 testCase = "TC01"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd"] + user_input.msrbs_node
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
        

##############################################################################
#Test case 02
#Description: config_renew for single radio node (mode manual)
##############################################################################
def TC02(): 
 testCase = "TC02"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 3
#Description: config_renew for multiple radio nodes (mode automatic)
##############################################################################
def TC03(): 
 testCase = "TC03"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node + user_input.msrbs_node1
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 04
#Description: config_renew for multiple radio nodes (mode manual)
##############################################################################
def TC04(): 
 testCase = "TC04"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node + user_input.msrbs_node1
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 05
#Description: Config_trust for multiple radio nodes (invalidate the trusted certs)
##############################################################################
def TC05(): 
 testCase = "TC05"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.wrong_subjectDN + testData["cmd2"] + user_input.wrong_serial + testData["cmd3"] + user_input.msrbs_node + user_input.msrbs_node1
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 06
#Description: Config_trust for radio nodes file as input (invalidate the trusted certs)
##############################################################################
def TC06(): 
 testCase = "TC06"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 f= open("/var/tmp/node_file.txt","w+")
 f.write(user_input.msrbs_node +'\n')
 f.write(user_input.msrbs_node1 +'\n')
 os.system('chmod 777 /var/tmp/node_file.txt')
 f.close()
 file_name= "/var/tmp/node_file.txt"
 str = testData["cmd1"] + user_input.wrong_subjectDN + testData["cmd2"] + user_input.wrong_serial + testData["cmd3"] + file_name
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 07
#Description:Config_trust for single radio node (enable the trusted certs)
##############################################################################
def TC07(): 
 testCase = "TC07"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.correct_subjectDN + testData["cmd2"] + user_input.correct_serial + testData["cmd3"] + user_input.msrbs_node 
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 08
#Description:Config_trust for multiple radio nodes (enable the trusted certs)
##############################################################################
def TC08(): 
 testCase = "TC08"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.correct_subjectDN + testData["cmd2"] + user_input.correct_serial + testData["cmd3"] + user_input.msrbs_node + user_input.msrbs_node1
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 09
#Description:Config_trust for radio node file as input (enable the trusted certs)
##############################################################################
def TC09(): 
 testCase = "TC09"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 f= open("/var/tmp/node_file.txt","w+")
 f.write(user_input.msrbs_node +'\n')
 f.write(user_input.msrbs_node1 +'\n')
 os.system('chmod 777 /var/tmp/node_file.txt')
 f.close()
 file_name= "/var/tmp/node_file.txt"
 str = testData["cmd1"] + user_input.correct_subjectDN + testData["cmd2"] + user_input.correct_serial + testData["cmd3"] + file_name
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 10
#Description: Config_trust for single radio node (invalidate the trusted certs)
##############################################################################
def TC10(): 
 testCase = "TC10"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.wrong_subjectDN + testData["cmd2"] + user_input.wrong_serial + testData["cmd3"] + user_input.msrbs_node 
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 11
#Description: Listing the RADIO_NODE genarated certificates
##############################################################################
def TC11(): 
 testCase = "TC11"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] 
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 12
#Description: config_renew for radio node file as input (mode automatic)
##############################################################################
def TC12(): 
 testCase = "TC12"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 f= open("/var/tmp/node_file.txt","w+")
 f.write(user_input.msrbs_node +'\n')
 f.write(user_input.msrbs_node1 +'\n')
 os.system('chmod 777 /var/tmp/node_file.txt')
 f.close()
 file_name= "/var/tmp/node_file.txt"
 str = testData["cmd1"] + file_name
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 13
#Description: config_renew for radio node file as input (mode manual)
##############################################################################
def TC13(): 
 testCase = "TC13"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 f= open("/var/tmp/node_file.txt","w+")
 f.write(user_input.msrbs_node +'\n')
 f.write(user_input.msrbs_node1 +'\n')
 os.system('chmod 777 /var/tmp/node_file.txt')
 f.close()
 file_name= "/var/tmp/node_file.txt"
 str = testData["cmd1"] + file_name
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 14
#Description: SYSLOG Trust Distribution for Radio_Node
##############################################################################
def TC14(): 
 testCase = "TC14"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 15
#Description:  NETCONF Trust Distribution to Radio Node 
##############################################################################
def TC15(): 
 testCase = "TC15"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 str = testData["cmd1"] + user_input.msrbs_node
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 16
#Description:  LDAP Trust Distribution for Radio_Node
##############################################################################
def TC16(): 
 testCase = "TC16"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node 
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 17
#Description:  ALL Trust Certificates Distribution to Radio_Node
##############################################################################
def TC17(): 
 testCase = "TC17"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 18
#Description:  NETCONF Trust Distribution for Multiple Radio_Nodes
##############################################################################
def TC18(): 
 testCase = "TC18"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node + user_input.msrbs_node1
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 19
#Description: LDAP Trust Distribution for Multiple Radio_Nodes
##############################################################################
def TC19(): 
 testCase = "TC19"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node + user_input.msrbs_node1
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 20
#Description:  SYSLOG Trust Distribution for Multiple Radio_Nodes
##############################################################################
def TC20(): 
 testCase = "TC20"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node + user_input.msrbs_node1
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 21
#Description:  LDAP and SYSLOG Trust Distribution for Radio_Node
##############################################################################
def TC21(): 
 testCase = "TC21"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 22
#Description: NETCONF and SYSLOG Trust Distribution for Radio_Node
##############################################################################
def TC22(): 
 testCase = "TC22"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
 

##############################################################################
#Test case 23
#Description: NETCONF and LDAP Trust Distribution for Radio_Node
##############################################################################
def TC23(): 
 testCase = "TC23"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)


##############################################################################
#Test case 24
#Description: ALL Trust Certificates Distribution to Multiple Radio_Nodes
##############################################################################
def TC24(): 
 testCase = "TC24"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node + user_input.msrbs_node1
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 25
#Description:  List of syslog state on multiple Radio_Nodes when one node name is not valid
##############################################################################
def TC25(): 
 testCase = "TC25"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node + " ossmaster:xxxx"
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 pattern1 = testData ["pattern1"]
 pattern2 = testData ["pattern2"]
 logging.debug(str)
 logging.debug(output1)

 if (re.search(pattern,output1) or re.search(pattern1,output1)) and re.search(pattern2,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 26
#Description: List of syslog state on CPP, Radio_T_node and Radio_node for type Radio_node 
##############################################################################
def TC26(): 
 testCase = "TC26"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node + user_input.erbs_node + user_input.tcu_node
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 pattern1 = testData["pattern1"]
 pattern2 = testData["pattern2"]
 logging.debug(str)
 logging.debug(output1)
 k=output1.count(pattern2)
 logging.debug(k)

 if (k==2 and (re.search(pattern,output1) or re.search(pattern1,output1))):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)


##############################################################################
#Test case 27
#Description: List of syslog state on CPP, Radio_T_node and Radio_node for type Radio_t_node
##############################################################################
def TC27(): 
 testCase = "TC27"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node + user_input.tcu_node + user_input.erbs_node 
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 pattern1 = testData["pattern1"]
 pattern2 = testData["pattern2"]
 logging.debug(str)
 logging.debug(output1)
 k=output1.count(pattern2)
 logging.debug(k)

 if (k==2 and (re.search(pattern,output1) or re.search(pattern1,output1))):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 28
#Description: Listing external syslog server to Radio_T_node 
##############################################################################
def TC28(): 
 testCase = "TC28"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData["cmd"]+" "+user_input.tcu_node, user_input.caas_user)
 output1=run_command1(testData["cmd1"]+" "+user_input.tcu_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.tcu_node)
 logging.debug(testData["cmd1"]+" "+user_input.tcu_node)
 logging.debug(output)
 logging.debug(output1)
 pattern = testData["pattern"]
 pattern1 = testData["pattern1"]
# logging.debug(output)
# logging.debug(output1)

 if (re.search(pattern1,output1)):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 elif (re.search(pattern, output1)):
        logging.debug("The pre-requisite of the node is not meet, distribute the syslog server to the node")
        logging.debug(FAILED)
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 29
#Description:  Listing external syslog server to Multiple Radio_T_nodes
##############################################################################
def TC29(): 
 testCase = "TC29"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData["cmd"]+" "+user_input.tcu_node+" "+user_input.tcu_node1, user_input.caas_user)
 output1=run_command1(testData["cmd1"]+" "+user_input.tcu_node+" "+user_input.tcu_node1, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.tcu_node)
 logging.debug(testData["cmd1"]+" "+user_input.tcu_node1)
 pattern = testData["pattern"]
 pattern1 = testData["pattern1"]
 logging.debug(output)
 logging.debug(output1)
 k=output1.count(pattern1)
 logging.debug(k)

 if (k==2):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 elif (re.search(pattern, output1)):
        logging.debug("The pre-requisite of the node is not meet, distribute the syslog server to the node")
        logging.debug(FAILED)
 else:
        logging.debug(FAILED)


##############################################################################
#Test case 30
#Description: Listing external syslog server to Radio_node
##############################################################################
def TC30(): 
 testCase = "TC30"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData["cmd"]+" "+user_input.msrbs_node, user_input.caas_user)
 output1=run_command1(testData["cmd1"]+" "+user_input.msrbs_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.msrbs_node)
 logging.debug(testData["cmd1"]+" "+user_input.msrbs_node)
 pattern = testData["pattern"]
 pattern1 = testData["pattern1"]
 logging.debug(output)
 logging.debug(output1)

 if (re.search(pattern1,output1)):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 elif (re.search(pattern, output1)):
        logging.debug("The pre-requisite of the node is not meet, distribute the syslog server to the node")
        logging.debug(FAILED)
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 31
#Description:  Listing external syslog server to Multiple Radio_nodes
##############################################################################
def TC31(): 
 testCase = "TC31"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData["cmd"]+" "+user_input.msrbs_node+" "+user_input.msrbs_node1, user_input.caas_user)
 output1=run_command1(testData["cmd1"]+" "+user_input.msrbs_node+" "+user_input.msrbs_node1, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.msrbs_node)
 logging.debug(testData["cmd1"]+" "+user_input.msrbs_node1)
 pattern = testData["pattern"]
 pattern1 = testData["pattern1"]
 logging.debug(output)
 logging.debug(output1)
 k=output1.count(pattern1)
 logging.debug(k)

 if (k==2):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 elif (re.search(pattern, output1)):
        logging.debug("The pre-requisite of the node is not meet, distribute the syslog server to the node")
        logging.debug(FAILED)
 else:
        logging.debug(FAILED)


##############################################################################
#Test case 32
#Description: Listing external syslog server to unreachable Radio_node
##############################################################################
def TC32(): 
 testCase = "TC32"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd"] + user_input.msrbs_node_stopped
 output1 = run_command1(str, user_input.caas_user)
 logging.debug(str)
 logging.debug(output1)
 newoutput = re.split("\n", output1)
 pattern = "Not Configured"

 if re.search(pattern,output1) :
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED)

##############################################################################
#Test case 33
#Description:  CLI command available for LDAP configuration
##############################################################################
def TC33(): 
 testCase = "TC33"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] 
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if (re.search(pattern,output1)):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED) 

 
##############################################################################
#Test case 34
#Description:  LDAP configuration for single Radio_t_node
##############################################################################
def TC34(): 
 testCase = "TC34"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.tcu_node
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if (re.search(pattern,output1)):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED) 
##############################################################################
#Test case 35
#Description: LDAP configuration for multiple Radio_t_nodes
##############################################################################
def TC35(): 
 testCase = "TC35"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.tcu_node + user_input.tcu_node1
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED) 
##############################################################################
#Test case 36
#Description:  Listing LDAP attributes for single Radio_t_node
##############################################################################
def TC36(): 
 testCase = "TC36"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.tcu_node
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if (re.search(pattern,output1)):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED) 

##############################################################################
#Test case 37
#Description:  Listing LDAP attributes for Multiple Radio_t_nodes
##############################################################################
def TC37(): 
 testCase = "TC37"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 str = testData["cmd1"] + user_input.tcu_node + user_input.tcu_node1
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)
 k=output1.count(pattern)
 logging.debug(k)
 
 if (k==2):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED) 

##############################################################################
#Test case 38
#Description: LDAP configuration for multiple mixed (Radio & Radio_t_nodes)
##############################################################################
def TC38(): 
 testCase = "TC38"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.tcu_node + user_input.msrbs_node
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 pattern1 = testData["pattern1"]
 logging.debug(str)
 logging.debug(output1)

 
 if (re.search(pattern1,output1) and re.search(pattern,output1)):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED) 
##############################################################################
#Test case 39
#Description: LDAP configuration for single Radio_t_node when Node is in offline
##############################################################################
def TC39(): 
 testCase = "TC39"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.tcu_node_stopped
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if (re.search(pattern,output1)):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED) 


##############################################################################
#Test case 40
#Description:  LDAP configuration for multiple Radio_t_nodes where one Node is in not reachable  and remaining are in reachable
##############################################################################
def TC40(): 
 testCase = "TC40"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 str = testData["cmd1"] + user_input.tcu_node +" "+ user_input.tcu_node_stopped
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 pattern1 = testData["pattern1"]
 logging.debug(str)
 logging.debug(output1)
 
 if (re.search(pattern1,output1) and re.search(pattern,output1)):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED) 

##############################################################################
#Test case 41
#Description:  Listing LDAP attributes for single Radio_t_node when Node is offline
##############################################################################
def TC41(): 
 testCase = "TC41"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.tcu_node_stopped
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if (re.search(pattern,output1)):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 42
#Description:  Listing LDAP attributes for Multiple Radio_t_nodes  where one Node is in not reachable and remaining are in reachable
##############################################################################
def TC42(): 
 testCase = "TC42"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.tcu_node + " " +user_input.tcu_node_stopped
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 pattern1 = testData["pattern1"]
 logging.debug(str)
 logging.debug(output1)
 k=output1.count(pattern1)
 logging.debug(k)

 if (re.search(pattern,output1) and k==1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 43
#Description: LDAP configuration for single Radio node
##############################################################################
def TC43(): 
 testCase = "TC43"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if (re.search(pattern,output1)):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED) 

 
##############################################################################
#Test case 44
#Description:   LDAP configuration for multiple Radio nodes
##############################################################################
def TC44(): 
 testCase = "TC44"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node + user_input.msrbs_node1
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)
 
 if (re.search(pattern,output1)):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED) 

##############################################################################
#Test case 45
#Description:  Listing LDAP attributes for single Radio node
##############################################################################
def TC45(): 
 testCase = "TC45"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if (re.search(pattern,output1)):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 46
#Description:  Listing LDAP attributes for Multiple Radio nodes
##############################################################################
def TC46(): 
 testCase = "TC46"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 str = testData["cmd1"] + user_input.msrbs_node + user_input.msrbs_node1
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)
 k=output1.count(pattern)
 logging.debug(k)

 if (k==2):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 47
#Description: LDAP configuration for single Radio node when Node is in offline
##############################################################################
def TC47(): 
 testCase = "TC47"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node_stopped
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if (re.search(pattern,output1)):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED) 


##############################################################################
#Test case 48
#Description:  LDAP configuration for multiple Radio nodes where one Node is in not reachable  and remaining are in reachable
##############################################################################
def TC48(): 
 testCase = "TC48"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node + user_input.msrbs_node_stopped
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)
 
 if (re.search(pattern,output1)):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED) 

##############################################################################
#Test case 49
#Description:  Listing LDAP attributes for single Radio node when Node is offline
##############################################################################
def TC49(): 
 testCase = "TC49"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 str = testData["cmd1"] + user_input.msrbs_node_stopped
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if (re.search(pattern,output1)):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 50
#Description:  Listing LDAP attributes for Multiple Radio nodes  where one Node is in not reachable and remaining are in reachable
##############################################################################
def TC50(): 
 testCase = "TC50"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData["cmd1"] + user_input.msrbs_node + user_input.msrbs_node_stopped
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 pattern1 = testData["pattern1"]
 logging.debug(str)
 logging.debug(output1)
 k=output1.count(pattern1)
 logging.debug(k)

 if (re.search(pattern,output1) and k==1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

###################################################################################################
#Test case 51
#Description:Verification of set_renewal_mode: automatic for multiple Radio_Nodes with file as input
###################################################################################################
def TC51(): 
 testCase = "TC51"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 f= open("/var/tmp/node_file.txt","w+")
 f.write(user_input.radio_node +'\n')
 f.write(user_input.radio_node1 +'\n')
 os.system('chmod 777 /var/tmp/node_file.txt')
 f.close()
 file_name= "/var/tmp/node_file.txt"
 str = testData["cmd"] + file_name
 time.sleep(20)
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)
##################################################################################################
#Test case 52
#Description:Verification of set_renewal_mode: Manual for multiple Radio_Nodes with file as input
##################################################################################################
def TC52(): 
 testCase = "TC52"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 f= open("/var/tmp/node_file.txt","w+")
 f.write(user_input.radio_node +'\n')
 f.write(user_input.radio_node1 +'\n')
 os.system('chmod 777 /var/tmp/node_file.txt')
 f.close()
 file_name= "/var/tmp/node_file.txt"
 str = testData["cmd"] + file_name
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##################################################################################
#Test case 53
#Description:Verification of set_renewal_mode: automatic for multiple mixed nodes 
##################################################################################
def TC53(): 
 testCase = "TC53"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 f= open("/var/tmp/node_file.txt","w+")
 f.write(user_input.radio_node +'\n')
 f.write(user_input.radio_node1 +'\n')
 os.system('chmod 777 /var/tmp/node_file.txt')
 f.close()
 file_name= "/var/tmp/node_file.txt"
 str = testData["cmd"] + file_name
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 54
#Description:Verification of set the expiryAlarmThreshold  for Radio_Node
##############################################################################
def TC54(): 
 testCase = "TC54"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.radio_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.radio_node)
 logging.debug(output)
 pattern = "Failed :"
 newoutput = re.split(pattern, output)
 newoutput = re.split("\n", newoutput[1])
 if (int(newoutput[0].strip()) != 0):
        logging.debug(FAILED)
 else:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT,testCase,'pass')
###################################################################################
#Test case 55
#Description:Verification of set the expiryAlarmThreshold  for multiple Radio_Nodes
###################################################################################
def TC55(): 
 testCase = "TC55"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.mul_radio_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.mul_radio_node)
 logging.debug(output)
 pattern = "Failed :"
 newoutput = re.split(pattern, output)
 newoutput = re.split("\n", newoutput[1])
 if (int(newoutput[0].strip()) != 0):
        logging.debug(FAILED)
 else:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT,testCase,'pass')
######################################################################################################
#Test case 56
#Description:Verification of set the expiryAlarmThreshold  for multiple Radio_Nodes with file as input
######################################################################################################
def TC56(): 
 testCase = "TC56"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 
 f= open("/var/tmp/node_file.txt","w+")
 f.write(user_input.radio_node +'\n')
 f.write(user_input.radio_node1 +'\n')
 os.system('chmod 777 /var/tmp/node_file.txt')
 f.close()
 file_name= "/var/tmp/node_file.txt"
 str = testData["cmd"] + file_name
 output1 = run_command1(str, user_input.caas_user)
 pattern = testData["pattern"]
 logging.debug(str)
 logging.debug(output1)

 if re.search(pattern,output1):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)



############################################################################################
#Test case 57
#Description:Verification of ALL Trust Certificates Distribution to  Radio_Nodes through CLI
############################################################################################
def TC57(): 
 testCase = "TC57"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)


 output=run_command1(testData['cmd']+" "+user_input.radio_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.radio_node)
 logging.debug(output)
 pattern = "Failed :"
 newoutput = re.split(pattern, output)
 newoutput = re.split("\n", newoutput[1])
 if (int(newoutput[0].strip()) != 0):
        logging.debug(FAILED)
 else: 
        logging.debug(PASSED)
        update_result_file(TEST_SUIT,testCase,'pass')

##############################################################################
#Test case 58
#Description:Verification of listing Trust Certificates to Radio_Node
##############################################################################
def TC58(): 
 testCase = "TC58"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 output = run_command1(testData["cmd"]+" "+user_input.radio_node, user_input.caas_user)
 pattern = "NE Name" 
 logging.debug(testData["cmd"]+" "+user_input.radio_node)
 logging.debug(output)

 if re.search(pattern,output):
        logging.debug(PASSED)
        update_result_file(TEST_SUIT, testCase, 'pass')
 else:
        logging.debug(FAILED)

##############################################################################
#Test case 59
#Description:Verification of listing Trust Certificates to multiple Radio_Nodes
##############################################################################
def TC59(): 
 testCase = "TC59"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 output = run_command1(testData['cmd']+" "+user_input.mul_radio_node , user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.mul_radio_node)
 logging.debug(output)
 word_list=user_input.mul_radio_node.split("ossmaster:")
 pattern = user_input.radio_node


 if re.search(word_list[2],output) and re.search(word_list[1],output):
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED)
##################################################################################################
#Test case 60
#Description:Verification of listing Trust Certificates to multiple Radio_Nodes using file as input
##################################################################################################
def TC60(): 
 testCase = "TC60"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)


 f= open("/var/tmp/node_file.txt","w+")
 f.write(user_input.radio_node +'\n')
 f.write(user_input.radio_node1 +'\n')
 os.system('chmod 777 /var/tmp/node_file.txt')
 f.close()
 f1 = open("/var/tmp/node_file.txt","r")
 output1 = f1.readlines()
 file_name= "/var/tmp/node_file.txt" 
 str = testData["cmd"] + file_name
 output=run_command1(str, user_input.caas_user)
 logging.debug(output)
 pattern = user_input.radio_node 
 pattern1 = user_input.radio_node1 

 if re.search(pattern,output) and re.search(pattern1,output):
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED)


##############################################################################
#Test case 61
#Description:
##############################################################################
def TC61(): 
 testCase = "TC61"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 