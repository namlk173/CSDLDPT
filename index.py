from colordescriptor import ColorDescriptor
import argparse
import glob
import cv2
import os

# ap = argparse.ArgumentParser()
# ap.add_argument("-d", "--dataset", required=True, help="Path to the directory that contains the images to be indexed")
# ap.add_argument("-i", "--index", required=True, help="Path to where the computed index will be stored")
# args  = vars(ap.parse_args())
path_dir_data = r"dataset/"
cd = ColorDescriptor((8, 12, 3))

output = open("index.csv", "w")

for imagePath in os.listdir(path_dir_data):

    imageID  = imagePath
    image = cv2.imread(path_dir_data + imagePath)

    features = cd.describe(image)
    features = [str(f) for f in features]
    output.write("%s,%s\n" % (imageID, ",".join(features)))
output.close()
