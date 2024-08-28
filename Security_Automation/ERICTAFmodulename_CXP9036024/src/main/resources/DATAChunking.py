#!/usr/bin/python
import logging
from utility import *

#Global data sepcific for the testsuit
TEST_DATA_FILE = "test_data.xml"
DICT_ROOT = "Test_data"
PASSED = "testcase passed"
FAILED = "testcase failed"
LOGFILE = "CLI_testSuit.log"

TEST_SUIT = "DATAChunking"

TEST_DATA = parseXML_to_dict(TEST_DATA_FILE)[DICT_ROOT][TEST_SUIT]

##############################################################################
#Test case 1
#Description "Fingerprint Verification for NECertCA.pem"
##############################################################################

