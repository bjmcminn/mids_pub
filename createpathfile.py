#!/usr/bin/python
import sys
import os

def main(argv):
	parentDirectory = argv[1]
	
	sys.stderr.write("--> Parent folder is: " + parentDirectory + "\n");
	
	output_file = open("pathlist.txt","w")	
	
	listDirectories = os.listdir(parentDirectory)
	
	for directory in listDirectories:
		contents = os.listdir(parentDirectory + "/" + directory)
		output_file.write(parentDirectory + "/" + directory + "/" + contents[0] + "\n")
		
if __name__ == "__main__":
    main(sys.argv)