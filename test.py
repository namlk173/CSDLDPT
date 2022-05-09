from turtle import color
from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import math
index = {}
images = {}

path_dir = r"DATASET/"

images = []
hists = []
for image_name in os.listdir(path_dir):
    image_path = path_dir  + image_name
    image = cv2.imread(image_path)
    images.append(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hists.append(hist)

# show histogram
# fig = plt.figure(figsize=(8,8))
# rows = 5
# columns = round(len(images)/5)
# i = 1
# for hist in hists:
#     fig.add_subplot(rows, columns, i)
#     plt.plot(hist, color='b')
#     plt.axis('off')
#     plt.title(i)
#     i = i+1
# plt.show()





OPENCV_METHODS = (
	("Correlation", cv2.HISTCMP_CORREL),
	("Chi-Squared", cv2.HISTCMP_CHISQR),
	("Intersection", cv2.HISTCMP_INTERSECT),
	("Hellinger", cv2.HISTCMP_BHATTACHARYYA))
# loop over the comparison methods
for (methodName, method) in OPENCV_METHODS:
	# initialize the results dictionary and the sort
	# direction
	results = {}
	reverse = False
	# if we are using the correlation or intersection
	# method, then sort the results in reverse order
	if methodName in ("Correlation", "Intersection"):
		reverse = True

	for i in range (0, len(hists)-1):
		# compute the distance between the two histograms
		# using the method and update the results dictionary
		d = round(cv2.compareHist(hists[0], hists[i], method),2)
		results.update({i:d})
	# sort the results
print(results)

# show image
fig = plt.figure(figsize=(8,8))
rows = 5
columns = round(len(images)/5)
i = 1
for image in images:
    fig.add_subplot(rows, columns, i)
    plt.imshow(image)
    plt.axis('off')
    plt.title(i)
    i = i+1
plt.show()