#!/usr/bin/python
#############################################################################################
#  *********************************************************************
#  *COPYRIGHT:
#  *Author: Manu Prasad(xmanupr)
#  *********************************************************************
#	This file provides the utility functions for the CLI automation.
#	
#############################################################################################
import shutil
import subprocess
import xml.etree.ElementTree as ET


#############################################################################################
#Function: runCommand
#		Run any shell style command using the following functions
#param:
#	cmd = command to runCommand
#return:
#	output returned by the command execution
#############################################################################################
def run_command(cmd):
	
	output = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True).communicate()[0].strip()
	return output
	

#############################################################################################
#Function: runCommand
#		Run any shell style command using the following functions
#param:
#	cmd = command to runCommand
#	user = user environment to be used
#return:
#	output returned by the command execution
#############################################################################################
def run_command1(cmd, user):
	user_cmd = "su - "+user+" -c "+'"'+cmd+'"'
	output = subprocess.Popen(user_cmd,stdout=subprocess.PIPE, shell=True).communicate()[0].strip()
	return output
	

#############################################################################################
#Function: parseXML_to_dict
#		Parse an XML file and return dict
#param:
#	XML file
#return:
#	dict
#############################################################################################	
def parseXML_to_dict(file):
	tree = ET.parse(file)
	root = tree.getroot()
	xmldict = make_dict_from_tree(root)
	return xmldict


#############################################################################################
#Function: make_dict_from_tree
#		Parse an XML root object to a dict
#param:
#	element_tree_root: XML root object
#return:
#	dict
#############################################################################################	
def make_dict_from_tree(element_tree_root):
	def internal_iter(tree, accum):
		if tree is None:
			return accum
		else:
			if len(tree) == 0:
				accum[tree.get('param')] = tree.text
			else:
				accum[tree.get('param')] = {}
				
			for child in tree:
				result = internal_iter(child, {})
				accum[tree.get('param')].update(result)		
		return accum
		
	return internal_iter(element_tree_root, {})

	
#############################################################################################
#Function: createResultFile
#		Create result XML file from the data input file.
#param:
#	test_data_file: test data file in XML format
#return:
#	0 = Done
#	1 = Failed
#############################################################################################	
def create_result_file(test_data_file):
	resultFile = 'test_result.xml'
	shutil.copy(test_data_file,resultFile)
	
	tree = ET.parse(resultFile)
	root = tree.getroot()
	
	for testsuit in root:
		for testcase in testsuit:
			testcase.text = 'fail'
			for item in testcase.findall('item'):
				testcase.remove(item)
	tree.write(resultFile)


#############################################################################################
#Function: printResult
#		prints the test execution result.
#param:
#	None
#return:
#	None
#############################################################################################	
def print_result():
	resultFile = 'test_result.xml'
	tree = ET.parse(resultFile)
	root = tree.getroot()
	
	for testSuit in root:
		print testSuit.get('param'),':'
		passed_tc = 0
		failed_tc = 0
		for testcase in testSuit:
			if testcase.text == 'pass':
				passed_tc += 1
			elif testcase.text == 'fail':
				failed_tc += 1
				
		print "Passed test cases:",passed_tc
		print "Failed test cases",failed_tc

		
#############################################################################################
#Function: update_result_file
#		updates the result file with the testcase result.
#param:
#	testsuit: test suit name
#	testcase: test case name
#	result : test result (pass/fail)
#return:
#	None
#############################################################################################
def update_result_file(testsuit, testcase, result):
	result_file = 'test_result.xml'
	tree = ET.parse(result_file)
	root = tree.getroot()
	
	for element in root.findall('testsuit'):
		if element.get('param') == testsuit:
			for tc_element in element:
				if tc_element.get('param') == testcase:
					tc_element.text = result
					tree.write(result_file)
					break
	