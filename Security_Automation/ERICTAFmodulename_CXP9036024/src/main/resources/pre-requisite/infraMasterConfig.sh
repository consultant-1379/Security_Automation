#!/usr/bin/expect -f
spawn ssh -X root@atvts1440.athtem.eei.ericsson.se
expect "root@atvts1440.athtem.eei.ericsson.se's password" { send "shroot\r"}
set timeout 240
expect "atvts1440" { send -- "ssh omsrvm\r"}
expect "root@omsrvm:~# " { send -- "/opt/ericsson/secinst/bin/config.sh\r"}
expect "Enter password for .cn=directory manager:" { send -- "ldappass\r"}
expect "ERICcsa "
expect "Select ldap domain:" { send "1\r"}
expect "Select ldap domain:" { send "1\r"}
expect eof