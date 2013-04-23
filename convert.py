#!/usr/bin/env python   

import re
import sys
import getopt

#test if file exists
def openFile(name, o_type):
	try:
	    #open a file 
		f = open(name, o_type)
	except IOError as e:
	    print "I/O error({0}): {1} {2}".format(e.errno, name, e.strerror)
	    sys.exit(2)
	except:
		print "Unexpected error"
		sys.exit(2)
	
	return f

#convert function
def convert(source, result):
	for line in source:
		start = re.search('http://.*$',line).start()
		stop = len(line)

		headline = line[:start]
		headline = re.sub(' - $','',headline)
		url = re.sub('\n','',line[start:stop]);

		item = '<span><a href="%s">%s</a></span><br />\n' % (url, headline)
		result.write("%s\n" % item)

#main function
def main(argv):
	inputfile = ''
	outputfile = ''

	try:
	  	opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'convert.py -i <inputfile> -o <outputfile>'
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print 'convert.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg

	if inputfile == '':
		print 'convert.py -i <inputfile> -o <outputfile>'
		sys.exit(2)

	if outputfile == '':
		print 'convert.py -i <inputfile> -o <outputfile>'
		sys.exit(2)

	source = openFile(inputfile, 'r')
	result = openFile(outputfile, 'w')

	convert(source,result)
	source.close()
	result.close()

	sys.exit()


#main function
main(sys.argv[1:])

