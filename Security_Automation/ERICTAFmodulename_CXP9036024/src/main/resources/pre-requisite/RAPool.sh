#!/usr/bin/expect -f
spawn ssh -X root@atvts1440.athtem.eei.ericsson.se
expect "root@atvts1440.athtem.eei.ericsson.se's password" { send "shroot\r"}
expect "atvts1440" { send -- "ssh omsrvm\r"}
expect "root@omsrvm:~# " { send -- "/opt/ericsson/secinst/bin/config.sh -p ERICracrs:poll -f\r"}
expect "root@omsrvm:~# " { send -- "scp /var/tmp/ERICsinst/config/secinst_omsrvm_config.zip root@omsas:/tmp\r"}
expect "Pass" {send "shroot12\r"}
expect "root@omsrvm" { send -- "ssh omsas\r"}
expect "Pass" {send "shroot12\r"}
expect "root@omsas:~# " { send -- "/opt/ericsson/secinst/bin/config.sh -R /tmp/secinst_omsrvm_config.zip\r"}
sleep 60
expect "root@omsas:~# " { send -- "scp /var/tmp/ERICsinst/config/secinst_omsrvm_response.zip root@omsrvm:/tmp\r"}
expect "Pass" {send "shroot12\r"}
expect "root@omsas" { send -- "ssh omsrvm\r"}
expect "Pass" {send "shroot12\r"}
expect "root@omsrvm:~# " { send -- "/opt/ericsson/secinst/bin/config.sh -p ERICracrs:poll -r /tmp/secinst_omsrvm_response.zip\r"}
expect "root@omsrvm" { send -- "ssh omsrvs\r"}
expect "root@omsrvs:~# " { send -- "/opt/ericsson/secinst/bin/config.sh -p ERICracrs:poll -f\r"}
expect "root@omsrvs:~# " { send -- "scp /var/tmp/ERICsinst/config/secinst_omsrvs_config.zip root@omsas:/tmp\r"}
set timeout 60
expect "Pass" {send "shroot12\r"}
expect "root@omsrvs" { send -- "ssh omsas\r"}
expect "Pass" {send "shroot12\r"}
expect "root@omsas:~# " { send -- "/opt/ericsson/secinst/bin/config.sh -R /tmp/secinst_omsrvs_config.zip\r"}
sleep 60
expect "root@omsas:~# " { send -- "scp /var/tmp/ERICsinst/config/secinst_omsrvs_response.zip root@omsrvs:/tmp\r"}
expect "Pass" {send "shroot12\r"}
expect "root@omsas" { send -- "ssh omsrvs\r"}
expect "Pass" {send "shroot12\r"}
expect "root@omsrvs:~# " { send -- "/opt/ericsson/secinst/bin/config.sh -p ERICracrs:poll -r /tmp/secinst_omsrvs_response.zip\r"}
expect eof
