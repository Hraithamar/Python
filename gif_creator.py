import imageio.v3 as iio
import os
from os import listdir

directory = os.getcwd()

filenames = []
images = []

for filename in os.listdir(directory):
  if filename.endswith(".jpg"):
    filenames.append(filename)

filenames.sort()

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite("hair.gif", images, duration = 500, loop = 0)
