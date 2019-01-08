#!/usr/bin/env python3

import os
import sys

def rename_files(directory):
	i = 1
	for file in os.listdir(directory):
    		print("Noob: " + file)
    		filename, file_extension = os.path.splitext(file)
    		os.rename(os.path.join(directory, file), os.path.join(directory, str(i) + file_extension))
    		i = i+1

if __name__ == "__main__":
	arguments = len(sys.argv).pop(0)
	for directory in arguments:
		if os.listdir(directory):
			rename_files(directory)
		else:
			print("[Error]: Directory \"{}\" does not exist.\n".format(directory))
			sys.exit()
