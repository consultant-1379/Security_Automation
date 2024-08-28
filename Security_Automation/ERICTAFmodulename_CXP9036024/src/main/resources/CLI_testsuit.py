#!/usr/bin/python
#############################################################################################
#  *********************************************************************
#  *COPYRIGHT:
#  *
#  *********************************************************************
#	This is the testsuit file to trigger the CLI testsuit.
#
#	Author: Manu Prasad(xmanupr)
#############################################################################################

import utility
import SSLciphers
import MULTIRAT
import AXE
import CRLTesting
import MSRBSV2
#import NegetiveTesting
import Telstra
import CIPHER
import RTSEL
#Create test result file from the test data file^M
utility.create_result_file('test_data.xml')


##############################################################################################

print("Hi... The testing is started.. It will take 1 and half hour to end ")


print ("")
print("")

##########Start: MSRBSV2######################################################################
MSRBSV2.TC01()
MSRBSV2.TC02()
MSRBSV2.TC03()
MSRBSV2.TC04()
MSRBSV2.TC05()
MSRBSV2.TC06() 
MSRBSV2.TC07()
MSRBSV2.TC08()
MSRBSV2.TC09() 
MSRBSV2.TC10()
MSRBSV2.TC11()
MSRBSV2.TC12()
MSRBSV2.TC13()
MSRBSV2.TC14()
MSRBSV2.TC15()
MSRBSV2.TC16() 
MSRBSV2.TC17()
MSRBSV2.TC18()
MSRBSV2.TC19() 
MSRBSV2.TC20()
MSRBSV2.TC21()
MSRBSV2.TC22()
MSRBSV2.TC23()
MSRBSV2.TC24()
MSRBSV2.TC25()
MSRBSV2.TC26() 
MSRBSV2.TC27()
MSRBSV2.TC28()
MSRBSV2.TC29() 
MSRBSV2.TC30()
MSRBSV2.TC31()
MSRBSV2.TC32()
MSRBSV2.TC33()
MSRBSV2.TC34()
MSRBSV2.TC35()
MSRBSV2.TC36() 
MSRBSV2.TC37()
MSRBSV2.TC38()
MSRBSV2.TC39() 
MSRBSV2.TC40()
MSRBSV2.TC41()
MSRBSV2.TC42()
MSRBSV2.TC43()
MSRBSV2.TC44()
MSRBSV2.TC45()
MSRBSV2.TC46() 
MSRBSV2.TC47()
MSRBSV2.TC48()
MSRBSV2.TC49() 
MSRBSV2.TC50()
MSRBSV2.TC51()
MSRBSV2.TC52()
MSRBSV2.TC53()
MSRBSV2.TC54()
MSRBSV2.TC55()
MSRBSV2.TC56() 
MSRBSV2.TC57()
MSRBSV2.TC58()
MSRBSV2.TC59() 
MSRBSV2.TC60()


##########Start: SSL -CIPHER##################################################################
SSLciphers.TC06()

##########Start: MULTI RAT##################################################################^M
MULTIRAT.TC01()
MULTIRAT.TC02()
MULTIRAT.TC03()
MULTIRAT.TC04()
MULTIRAT.TC05()
MULTIRAT.TC06()
MULTIRAT.TC07()
MULTIRAT.TC08()

##########Start: AXE##################################################################
AXE.TC01()
AXE.TC02()

##########Start: CRLTesting##################################################################
CRLTesting.TC01()
CRLTesting.TC02()
CRLTesting.TC03()
CRLTesting.TC04()
CRLTesting.TC05()
CRLTesting.TC06()



#############Start: Telstra###################################################################
Telstra.TC01()
Telstra.TC02()
Telstra.TC03()
Telstra.TC04()
Telstra.TC05()
Telstra.TC06()
Telstra.TC07()
Telstra.TC08()
Telstra.TC09()
Telstra.TC10()
Telstra.TC11()
Telstra.TC12()
Telstra.TC13()
Telstra.TC14()
Telstra.TC15()
Telstra.TC16()
Telstra.TC17()
Telstra.TC18()
Telstra.TC19()
Telstra.TC20()
Telstra.TC21()
Telstra.TC22()
Telstra.TC23()
Telstra.TC24()
Telstra.TC25()
Telstra.TC26()
Telstra.TC27()
Telstra.TC28()
Telstra.TC29()
Telstra.TC30()
Telstra.TC31()
Telstra.TC32()
Telstra.TC33()
Telstra.TC34()
Telstra.TC35()

#################CIPHER#####################################################################
CIPHER.TC01()
CIPHER.TC02()
CIPHER.TC03()
CIPHER.TC04()
CIPHER.TC05()
CIPHER.TC06()
CIPHER.TC07()
CIPHER.TC08()
CIPHER.TC09()
CIPHER.TC10()

#####Start: RTSEL##################################################################  
RTSEL.TC01()
RTSEL.TC02()
RTSEL.TC03() 
RTSEL.TC04() 
RTSEL.TC05() 
RTSEL.TC06()
RTSEL.TC07()
RTSEL.TC08() 
RTSEL.TC09() 
RTSEL.TC10() 
RTSEL.TC11() 
RTSEL.TC12() 
RTSEL.TC13() 
RTSEL.TC14() 
RTSEL.TC15() 
RTSEL.TC16() 
RTSEL.TC17() 
RTSEL.TC18()
RTSEL.TC19()
RTSEL.TC20()
RTSEL.TC21()
RTSEL.TC22()
RTSEL.TC23()
RTSEL.TC24()
RTSEL.TC25()
RTSEL.TC26()
RTSEL.TC27()
RTSEL.TC28()
RTSEL.TC29()
RTSEL.TC30()
RTSEL.TC31()
RTSEL.TC32()
RTSEL.TC33()
RTSEL.TC34()

#################################RESULT DISPLAY###############################################

utility.print_result()

print "*************************** RUN COMPLETED ***************************"
