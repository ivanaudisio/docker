#!/usr/bin/python

# Open a file
fo = open("/home/foo.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n");

# Close opend file
fo.close()
