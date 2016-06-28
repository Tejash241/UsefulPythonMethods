def are_images_same(image, reference_image):
	return image.shape == reference_image.shape and not(np.bitwise_xor(image,reference_image).any())

"""
Sorts the contours in an image according to their x, y values
"""	
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

"""
Returns an image from a url. Can also be done via urllib.urlretrieve()
"""
import urllib
def url_imread(url):
    req = urllib.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1) # 'load it as it is'
    return img

"""
converts rgb image into gray scale. Can also use cv2.cvtToGray()
"""
import numpy as np
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
