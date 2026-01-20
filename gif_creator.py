import imageio.v3 as iio
import os
from os import listdir
#getting current directory
directory = os.getcwd()

filenames = []
images = []
#using current directory path to get all images in current folder in one list
for filename in os.listdir(directory):
  if filename.endswith(".jpg"):
    filenames.append(filename)
#sorting the list to make sure the images will be displayed in the proper order
filenames.sort()

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite("hair.gif", images, duration = 500, loop = 0)

