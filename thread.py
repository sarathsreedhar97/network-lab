#!/usr/bin/python

import thread
import time

# Define a function for the thread
def print_time( threadName ,delay ):
   time.sleep(delay)
   print "%s: %s" % ( "In thread in" , threadName )

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1",4, ) )
   thread.start_new_thread( print_time, ("Thread-2",2, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass	
