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

#=================== IMAGE PROCESSING ==============================================================
def are_images_same(image, reference_image):
	return image.shape == reference_image.shape and not(np.bitwise_xor(image,reference_image).any())
	
def sort_contours(contours, method="left-to-right"):
	reverse = False
	i = 0
	if method == "right-to-left" or method == "bottom-to-top":
		reverse = True
	if method == "top-to-bottom" or method == "bottom-to-top":
		i = 1
	bounding_boxes = [cv2.boundingRect(c) for c in cnts]
	(cnts, bounding_boxes) = zip(*sorted(zip(cnts, bounding_boxes),
		key=lambda b:b[1][i], reverse=reverse))
	return (cnts)
