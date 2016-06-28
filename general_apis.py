import cv2
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
"""
returns the exception that is stored in the system
"""
import sys
def get_exception_message():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)

