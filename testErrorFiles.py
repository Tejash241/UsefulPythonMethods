import cv2
import numpy as np
import sys
from os import listdir
from os.path import isfile, join
import os

INPUT_IMAGE_FOLDER = "./input/img/"
OUTPUT_IMAGE_FOLDER = "./output/dictionary/"

def get_files(mypath):
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath,f))]
	return onlyfiles

def sort_contours(cnts,  method="left-to-right"):
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

def image_found(image):
	files = get_files(OUTPUT_IMAGE_FOLDER)
	for i in range(0, 44):
		try:
			path = os.path.join(OUTPUT_IMAGE_FOLDER, "roi"+str(i)+".png")
			reference_image = cv2.imread(path, 0)
			if image.shape == reference_image.shape and not(np.bitwise_xor(image,reference_image).any()):
				#print "Found"
				return True, i
		except AttributeError, e:
			print "Someone is null. i is %s and length is %s"%(i, len(files))
			print "image", image	
			print "referenceImage", reference_image
	
	return False, -1


path = os.path.join(INPUT_IMAGE_FOLDER, "13_IMG.jpg")
image = cv2.imread(path, 0)
if not os.path.isfile(path):
	print "File not found", path
	exit()
thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]
contours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]
contours = sort_contours(contours)
for cnt in contours:
    if cv2.contourArea(cnt)>10:
        [x,y,w,h] = cv2.boundingRect(cnt)
        if h>9 and w<30:
            #cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            roi = thresh1[y:y+h, x:x+w]
            resized_roi = cv2.resize(roi, (30, 30))
            #now put this digit in the middle of a much larger image
            blank_image = np.zeros((50,50), np.uint8)
            blank_image[0:30, 0:30] = resized_roi
            ifo, index = image_found(blank_image)
            if(ifo):
		    	print "Match found for this contour in image", index
            cv2.imshow("contour", blank_image)
            cv2.waitKey(0)