#!/usr/bin/python

from email.mime.text import MIMEText
from subprocess import Popen, PIPE

msg = MIMEText( "The tmon server process does not seem to run" )

msg['From']    = '<sender@host>'
msg['To']      = '<receiver@otherhost>'
msg['Subject'] = 'tmon server down'

p = Popen( ["/usr/sbin/sendmail", '-t', '-oi'], stdin=PIPE )
p.communicate(msg.as_string().encode())
