#!/usr/bin/python

import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("sarathsreedhar@cet.ac.in","hits1997")
message = "hi"
server.sendmail("sarathsreedhar@cet.ac.in","robinraju@cet.ac.in", message)         
print "Successfully sent email"
