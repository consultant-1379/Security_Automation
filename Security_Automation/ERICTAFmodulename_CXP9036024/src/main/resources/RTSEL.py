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

TEST_SUIT = "RTSEL"

TEST_DATA = parseXML_to_dict(TEST_DATA_FILE)[DICT_ROOT][TEST_SUIT]

############################################################################## 
#Test case 01 
#Description: Check RTSEL Deactivate is done on single Radio_Node
############################################################################## 
def TC01(): 
 testCase = "TC01"      
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 str = testData['cmd']+user_input.AI_radio_node
 output=run_command1(str, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.AI_radio_node)
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
#Test case 02 
#Description: Check RTSEL Deactivate is done on single Radio_T_Node
############################################################################## 
def TC02():
 testCase = "TC02"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.radio_t_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.radio_t_node)
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
#Test case 03 
#Description: Check RTSEL Deactivate is done on multiple Radio_Node
############################################################################## 
def TC03():
 testCase = "TC03"
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

##############################################################################
#Test case 04
#Description:Check RTSEL Deactivate is done on multiple Radio_T_nodes from GUI.
#When one of the node is CPP node name.
##############################################################################
def TC04():
 testCase = "TC04"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.mul_radio_t_node+" "+user_input.cpp_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.mul_radio_t_node+" "+user_input.cpp_node)
 logging.debug(output)
 newoutput = re.split("\n", output)
 pattern = "does not exist"
 pattern1 = "Successful :                   2"

 if re.search(pattern,output) and re.search(pattern1,output):
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED)
##############################################################################################################
#Test case 05
#Description:Check RTSEL Deactivate is done on both Radio_T_node and Radio_node.Give the type as RADIO_T_NODE
##############################################################################################################
def TC05():
 testCase = "TC05"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.mix_radio_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.mix_radio_node)
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
#Test case 06
#Description:
############################################################################## 
def TC06():
 testCase = "TC06"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.radio_t_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.radio_t_node)
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
#Test case 07
#Description:
############################################################################## 
def TC07():
 testCase = "TC07"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.radio_t_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.radio_t_node)
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
#Test case 08
#Description:
############################################################################## 
def TC08():
 testCase = "TC08"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.radio_t_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.radio_t_node)
 logging.debug(output)
 newoutput = re.split("\n", output)
 pattern = "Activated"

 if re.search(pattern,output) :
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED)

############################################################################## 
#Test case 09
#Description:
############################################################################## 
def TC09():
 testCase = "TC09"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.mul_radio_t_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.mul_radio_t_node)
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
#Test case 10 
#Description:
############################################################################## 
def TC10():
 testCase = "TC10"
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
#Test case 11 
#Description:
############################################################################## 
def TC11():
 testCase = "TC11"
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
#Test case 12
#Description:Check RTSEL Deactivate is done on multiple Radio_T_node from CLI.
#When one of the node is invalid node name.
##############################################################################
def TC12():
 testCase = "TC12"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.invalid_radio_t_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.invalid_radio_t_node)
 logging.debug(output)
 pattern = "does not exist"

 if re.search(pattern,output) :
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED)


##############################################################################
#Test case 13
#Description:
##############################################################################
def TC13():
 testCase = "TC13"
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


##############################################################################
#Test case 14
#Description:Verification of adding external syslog server to multiple Radio Nodes
##############################################################################
def TC14():
 testCase = "TC14"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.mul_radio_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.mul_radio_node)
 time.sleep(20)
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
#Test case 15
#Description:Verification of adding external syslog server to multiple Radio T Nodes
##############################################################################
def TC15():
 testCase = "TC15"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.mul_radio_t_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.mul_radio_t_node)
 logging.debug(output)
 pattern = "Failed :"
 newoutput = re.split(pattern, output)
 newoutput = re.split("\n", newoutput[1])
 if (int(newoutput[0].strip()) != 0):
        logging.debug(FAILED)
 else:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT,testCase,'pass')


#####################################################################################################
#Test case 16
#Description:Verification of adding external syslog server to multiple Radio Nodes and one CPP Node
#####################################################################################################
def TC16():
 testCase = "TC16"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.mul_radio_node+" "+user_input.cpp_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.mul_radio_node+" "+user_input.cpp_node)
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
#Test case 17 
#Description:Check the installed syslog certificate on multiple Radio_T_Node
##############################################################################
def TC17():
 testCase = "TC17"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)
 
 output1=run_command1(testData['cmd1']+" "+user_input.mul_radio_t_node, user_input.caas_user)
 output=run_command1(testData['cmd']+" "+user_input.mul_radio_t_node, user_input.caas_user)
 logging.debug(testData["cmd1"]+" "+user_input.mul_radio_t_node)
 logging.debug(testData["cmd"]+" "+user_input.mul_radio_t_node)
 logging.debug(output1)
 logging.debug(output)
 newoutput = re.split("\n", output)
 pattern = "Failed"
 pattern1 = "Not Installed"

 if re.search(pattern,output) or re.search(pattern1,output) :
        logging.debug(FAILED)
 else:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT,testCase,'pass')

##############################################################################
#Test case 18
#Description:Check the installed syslog certificate on single Radio_T_Node
##############################################################################
def TC18():
 testCase = "TC18"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.radio_t_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.radio_t_node)
 logging.debug(output)
 newoutput = re.split("\n", output)
 pattern = "Failed"
 pattern1 = "Not Installed"

 if re.search(pattern,output) or re.search(pattern1,output) :
        logging.debug(FAILED)
 else:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT,testCase,'pass')


##############################################################################
#Test case 19
#Description:Check list of syslog state  on multiple Radio_Node
##############################################################################
def TC19():
 testCase = "TC19"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.mul_radio_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.mul_radio_node)
 logging.debug(output)
 newoutput = re.split("\n", output)
 pattern = "Activated"

 if re.search(pattern,output) :
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED) 


###############################################################################################
#Test case 20
#Description:Check list of syslog state  on multiple Radio_T_Node where one node is unreachable
###############################################################################################
def TC20():
 testCase = "TC20"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.unreach_radio_t_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.unreach_radio_t_node)
 logging.debug(output)
 pattern = "Failed :"
 newoutput = re.split(pattern, output)
 newoutput = re.split("\n", newoutput[1])
 if (int(newoutput[0].strip()) != 0):
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED)

###############################################################################################
#Test case 21
#Description:Check RTSEL Activation is done on multiple Radio_Node from CLI.
#When one of the node is invalid node name.
###############################################################################################
def TC21():
 testCase = "TC21"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.invalid_radio_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.invalid_radio_node)
 logging.debug(output)
 pattern = "does not exist"

 if re.search(pattern,output) :
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED)


###############################################################################################
#Test case 22
#Description:Check RTSEL Activation is done on multiple Radio_Node from CLI.
#When one of the node is CPP node name.
###############################################################################################
def TC22():
 testCase = "TC22"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.mul_radio_node+" "+user_input.cpp_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.mul_radio_node+" "+user_input.cpp_node)
 logging.debug(output)
 newoutput = re.split("\n", output)
 pattern = "does not exist"
 pattern1 = "Successful :                   2"

 if re.search(pattern,output) and re.search(pattern1,output):
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED)

###############################################################################################
#Test case 23
#Description:Check RTSEL Activation is done on CPP, Radio_T_Node and Radio_Node from CLI.Give type as RADIO_NODE
###############################################################################################
def TC23():
 testCase = "TC23"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.radio_node+" "+user_input.cpp_node+" "+user_input.radio_t_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.radio_node+" "+user_input.cpp_node+" "+user_input.radio_t_node)
 logging.debug(output)
 newoutput = re.split("\n", output)
 pattern = "does not exist"
 pattern1 = "Successful :                   1"

 if re.search(pattern,output) and re.search(pattern1,output):
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED)

###############################################################################################
#Test case 24
#Description:Check RTSEL Activation is done on  Radio_T_Node and Radio_Node from CLI.Give type as RADIO_NODE
###############################################################################################
def TC24():
 testCase = "TC24"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.radio_node+" "+user_input.radio_t_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.radio_node+" "+user_input.radio_t_node)
 logging.debug(output)
 newoutput = re.split("\n", output)
 pattern = "does not exist"
 pattern1 = "Successful :                   1"

 if re.search(pattern,output) and re.search(pattern1,output):
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED)

###############################################################################################
#Test case 25
#Description:Check RTSEL Activation is done on  Radio_T_Node and Radio_Node from CLI.Give type as RADIO_T_NODE
###############################################################################################
def TC25():
 testCase = "TC25"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.radio_node+" "+user_input.radio_t_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.radio_node+" "+user_input.radio_t_node)
 logging.debug(output)
 newoutput = re.split("\n", output)
 pattern = "does not exist"
 pattern1 = "Successful :                   1"

 if re.search(pattern,output) and re.search(pattern1,output):
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED)

##########################################################################################################
#Test case 26
#Description:Check RTSEL Activation is done on multiple Radio_T_Node.When one of the node is CPP node name. 
##########################################################################################################
def TC26():
 testCase = "TC26"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.cpp_node+" "+user_input.mul_radio_t_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.cpp_node+" "+user_input.mul_radio_t_node)
 logging.debug(output)
 newoutput = re.split("\n", output)
 pattern = "does not exist"
 pattern1 = "Successful :                   2"

 if re.search(pattern,output) and re.search(pattern1,output):
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED)


##########################################################################################################
#Test case 27
#Description:Check RTSEL Deactivation is done on multiple Radio_Node.When one of the node is CPP node name.
##########################################################################################################
def TC27():
 testCase = "TC27"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.mul_radio_node+" "+user_input.cpp_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.mul_radio_node+" "+user_input.cpp_node)
 logging.debug(output)
 newoutput = re.split("\n", output)
 pattern = "does not exist"
 pattern1 = "Successful :                   2"

 if re.search(pattern,output) and re.search(pattern1,output):
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED)

###########################################################################################################
#Test case 28
#Description:Check RTSEL Deactivate is done on both Radio_T_node and Radio_node.Give the type as RADIO_NODE
###########################################################################################################
def TC28():
 testCase = "TC28"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.mix_radio_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.mix_radio_node)
 logging.debug(output)
 pattern = "Failed :"
 newoutput = re.split(pattern, output)
 newoutput = re.split("\n", newoutput[1])
 if (int(newoutput[0].strip()) != 0):
        logging.debug(FAILED)
 else:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT,testCase,'pass')

###########################################################################################################
#Test case 29
#Description:Check RTSEL Deactivate is done on CPP, Radio_T_node and Radio_node.Give the type as RADIO_NODE
###########################################################################################################
def TC29():
 testCase = "TC29"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.radio_node+" "+user_input.cpp_node+" "+user_input.radio_t_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.radio_node+" "+user_input.cpp_node+" "+user_input.radio_t_node)
 logging.debug(output)
 newoutput = re.split("\n", output)
 pattern = "does not exist"
 pattern1 = "Successful :                   1"

 if re.search(pattern,output) and re.search(pattern1,output):
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED)

###########################################################################################################
#Test case 30
#Description:Check RTSEL Deactivate is done on multiple Radio_node .Give the type as RADIO_NODE.
#When one of the node is invalid node name.
###########################################################################################################
def TC30():
 testCase = "TC30"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.invalid_radio_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.invalid_radio_node)
 logging.debug(output)
 newoutput = re.split("\n", output)
 pattern = "does not exist"
 pattern1 = "Successful :                   2"

 if re.search(pattern,output) and re.search(pattern1,output):
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED)

##############################################################################################################
#Test case 31
#Description:Check RTSEL Deactivate is done on both Radio_T_node and Radio_node.Give the type as RADIO_NODE
##############################################################################################################
def TC31():
 testCase = "TC31"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.mix_radio_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.mix_radio_node)
 logging.debug(output)
 pattern = "Failed :"
 newoutput = re.split(pattern, output)
 newoutput = re.split("\n", newoutput[1])
 if (int(newoutput[0].strip()) != 0):
        logging.debug(FAILED)
 else:
        logging.debug(PASSED)
        update_result_file(TEST_SUIT,testCase,'pass')

###########################################################################################################
#Test case 32
#Description:Check RTSEL Deactivate is done on CPP, Radio_T_node and Radio_node.Give the type as RADIO_T_NODE
###########################################################################################################
def TC32():
 testCase = "TC32"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.radio_node+" "+user_input.cpp_node+" "+user_input.radio_t_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.radio_node+" "+user_input.cpp_node+" "+user_input.radio_t_node)
 logging.debug(output)
 newoutput = re.split("\n", output)
 pattern = "does not exist"
 pattern1 = "Successful :                   1"

 if re.search(pattern,output) and re.search(pattern1,output):
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED)

####################################################################################
#Test case 33
#Description:Verification of adding external syslog server to multiple Radio_T_Nodes
####################################################################################
def TC33():
 testCase = "TC33"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output1=run_command1(testData['cmd1']+" "+user_input.mul_radio_t_node, user_input.caas_user)
 output=run_command1(testData['cmd']+" "+user_input.mul_radio_t_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.mul_radio_t_node)
 time.sleep(20)
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
#Test case 34
#Description:Check list of syslog state  on multiple Radio_T_Node
##############################################################################
def TC34():
 testCase = "TC34"
 testData = TEST_DATA[testCase]
 logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
 logging.info(TEST_SUIT+':'+testCase)

 output=run_command1(testData['cmd']+" "+user_input.mul_radio_t_node, user_input.caas_user)
 logging.debug(testData["cmd"]+" "+user_input.mul_radio_t_node)
 logging.debug(output)
 newoutput = re.split("\n", output)
 pattern = "Activated"

 if re.search(pattern,output) :
  logging.debug(PASSED)
  update_result_file(TEST_SUIT,testCase,'pass')
 else:
  logging.debug(FAILED)


