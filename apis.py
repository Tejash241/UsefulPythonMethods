from os import listdir
from os.path import isfile, join
import os
"""
this function safely returns files from a path
input: a path (preferable os.path.join)
output: a list of files from the path
"""
def get_files(mypath):
	only_files = [f for f in listdir(mypath) if isfile(join(mypath,f))]
	return only_files
