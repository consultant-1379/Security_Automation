#!/usr/bin/expect -f
spawn ssh root@atvts1440.athtem.eei.ericsson.se
expect "root@atvts1440.athtem.eei.ericsson.se's password" { send "shroot\r"}
expect "atvts1440" { send -- "ssh ossmaster\r"}
#expect "Password" { send "shroot\r"}
expect "ossmaster{root} # " { send -- "/opt/ericsson/fwSysConf/bin/removeDb.sh\r"}
expect "ossmaster{root} # " { send -- "su - nmsadm -c /opt/ericsson/fwSysConf/bin/createDb.sh\r"}
expect "logout"
expect "ossmaster{root} # " { send -- "smtool -coldrestart ARNEServer -reason='other' -reasontext='roboPrequisite'\r"}
expect "ossmaster{root} # " { send -- "smtool -coldrestart MAF -reason='other' -reasontext='roboPrequisite'\r"}
expect "ossmaster{root} # " { send -- "smtool -coldrestart ONRM_CS -reason='other' -reasontext='roboPrequisite'\r"}
expect "ossmaster{root} # " { send -- "smtool -coldrestart PSS -reason='other' -reasontext='roboPrequisite'\r"}
expect "ossmaster{root} # " { send -- "smtool -coldrestart SCS -reason='other' -reasontext='roboPrequisite'\r"}
expect "ossmaster{root} # " { send -- "smtool -coldrestart NetworkExplorerServer -reason='other' -reasontext='roboPrequisite'\r"}
expect "ossmaster{root} # " { send -- "exit\r"}
expect "logout "
sleep 60
expect "# " {send -- "ssh -X caas007@omsas.vts.com\r"}
expect "Password" { send "caas@123\r"}
expect "> " { send -- "caasAdmin sync\r"}
expect "> " { send -- "caasAdmin list targets\r"}
expect "> " { send -- "pkiAdmin list nodes -type stn\r"}
expect "> " { send -- "exit\r"}
expect "# " {send -- "ssh -X root@ossmaster.vts.com\r"}
expect "ossmaster{root} # " { send -- "/opt/ericsson/arne/bin/import.sh  -import -i_nau -f  /var/tmp/stn_create.xml\r"}
sleep 60
expect "ossmaster{root} # " { send -- "/opt/ericsson/arne/bin/import.sh  -import -i_nau -f  /var/tmp/erbs_create.xml\r"}
expect "ossmaster{root} # " { send -- "exit\r"}
expect "logout "
expect "# " {send -- "ssh -X caas007@omsas.vts.com\r"}
expect "Password" { send "caas@123\r"}
expect "> " { send -- "caasAdmin sync\r"}
expect "> " { send -- "caasAdmin list targets\r"}
expect "ossmaster:ERBS05 "
expect "> " { send -- "pkiAdmin list nodes -type stn\r"}
expect "TCU_test03 "
expect "> " { send -- "exit\r"}
expect "# " {send -- "ssh netsim@netsim.vts.com\r"}
expect "Password" { send "netsim\r"}
expect "netsim@netsim:~> " { send -- "cd ./inst\r"}
expect "netsim@netsim:~/inst> " { send -- "sh ./ipsec_moconfiguration.sh default ERBS_04\r"}
expect "netsim@netsim:~/inst> " { send -- "sh ./ipsec_moconfiguration.sh default ERBS_05\r"}
expect "netsim@netsim:~/inst> " { send -- "exit\r"}
expect eof