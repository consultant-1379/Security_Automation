#!/usr/bin/expect -f
spawn ssh -X design@ieatrcxb3661.athtem.eei.ericsson.se
expect "<design@ieatrcxb3661.athtem.eei.ericsson.se's password>" { send "shroot\r"}
expect "design@ieatrcxb3661:~$ " { send -- "vncserver -kill :77\r"}
expect "design@ieatrcxb3661:~$ " { send -- "rm /tmp/.X96-lock\r"}
expect "design@ieatrcxb3661:~$ " { send -- "rm /tmp/.X11-unix/X96\r"}
expect "design@ieatrcxb3661:~$ " { send -- "vncserver :77 -geometry 1600x1200\r"}
expect "design@ieatrcxb3661:~$ " { send -- "export DISPLAY=150.132.42.108:1865.0\r"}
expect "design@ieatrcxb3661:~$ " { send -- "vncviewer ieatrcxb3661.athtem.eei.ericsson.se:77\r"}
expect "Pass" { send "shroot\r"}
expect eof
