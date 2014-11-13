#!/usr/bin/python
import sys
import pysentiment as ps

from boto.s3.connection import S3Connection
from boto.s3.key import Key

AWS_KEY = ""
AWS_SECRET = ""
PATH_BUCKET_NAME = "bjmw205-mdasent"
DATA_BUCKET_NAME = "midsedgar"
PATH_TO_FILE_LIST = "input/mockpathfile.txt"
PATH_TO_FILE_LIST2 = "input/pathlist.txt"

def main(argv):
	sys.stderr.write("--> Started mapper\n");
	
	hiv4 = ps.HIV4()
	sys.stderr.write("--> Initialized sentimentor\n")
	
	conn = S3Connection(AWS_KEY, AWS_SECRET)
	path_bucket = conn.get_bucket(PATH_BUCKET_NAME)
	
	# Print buckets 	
	#rs = conn.get_all_buckets()
	#for bucket in rs:
	#	print bucket
	
	# Print keys
	#rs = data_bucket.list()
	#for key_obj in rs:
	#	print key_obj
		
	sys.stderr.write("--> Created AWS connection\n")
	
	sys.stderr.write("--> Reading path file\n")
	k = Key(path_bucket)
	k.key = PATH_TO_FILE_LIST2
	pathfile = k.get_contents_as_string()
	# print pathfile
	sys.stderr.write("--> Done reading path file\n\n")
	
	counter=0
	
	# Create a file-like object from the string returned from s3
	try:
		lines = pathfile.split('\n')
	except AttributeError:
		lines = pathfile
		
	data_bucket = conn.get_bucket(DATA_BUCKET_NAME)
	k = Key(data_bucket)

	for path in lines:
		counter+=1
		sys.stderr.write("--> Looping through lines of pathfile, on line number = " + str(counter) + "\n")
		sys.stderr.write("--> Grabbing filename: " + path + " from S3\n")
		k.key = path
		filecontents = k.get_contents_as_string()
		sys.stderr.write("--> Successfully grabbed " + path + ". The contents are --- " + filecontents[0:40] + "...\n")

		tokens = hiv4.tokenize(filecontents)
		score = hiv4.get_score(tokens)
		sys.stderr.write("--> Score for the filecontents are: " + str(score) + "\n\n")
		print (path, str(score))
								


if __name__ == "__main__":
    main(sys.argv)