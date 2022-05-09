from searcher import Searcher
from colordescriptor import ColorDescriptor
import argparse
import cv2
import matplotlib.pyplot as plt


data_dir = r"dataset"
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--index", required=True, help="Path to where the computed index will be stored")
# ap.add_argument("-q", "--query", required = True,
# 	help = "Path to the query image")
# ap.add_argument("-r", "--result-path", required = True,
# 	help = "Path to the result path")
# args = vars(ap.parse_args())
cd = ColorDescriptor((8, 12, 3))
query = cv2.imread("dataset/a1.jpg")
features = cd.describe(query)
# perform the search
searcher = Searcher("index.csv")
results = searcher.search(features)
# display the query

fig = plt.figure(figsize=(8,8))
rows = 3
cols = 5
fig.add_subplot(rows, cols, 1)
plt.imshow(query)
plt.title("query")

i = 2
# loop over the results
for (x, (score, resultID)) in enumerate(results):
	# load the result image and display it

    fig.add_subplot(rows, cols, i)
    result = cv2.imread(data_dir + "/" + resultID)
    plt.imshow(result)
    plt.axis('off')
    plt.title(f"d = {round(score,2)}")
    i = i+ 1
plt.show()