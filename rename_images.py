#!/usr/bin/env python3

import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
invalid_directories = ['.git', '.gitignore', '.DS_Store']

def rename_files(directory):
	i = 1
	for file in os.listdir(directory):
    		print("Filename: " + file)
    		filename, file_extension = os.path.splitext(file)
    		os.rename(os.path.join(directory, file), os.path.join(directory, str(i) + file_extension))
    		i = i+1

if __name__ == "__main__":
	arguments = sys.argv.pop(0)
	if arguments[0] == '.':
		directories = [d for d in os.listdir(dir_path) if os.path.isdir(d) and d not in invalid_directories]
		print("DIRECTORIES: " + str(directories))
		for directory in directories:
			rename_files(directory)
		sys.exit()
	for directory in arguments:
		dir = "./" + directory
		print("Arguments: " + str(sys.argv))
		print("Directory: " + directory)
		print("dir: " + dir)
		if os.listdir(dir):
			rename_files(dir)
		else:
			print("[Error]: Directory \"{}\" does not exist.\n".format(directory))
			sys.exit()
