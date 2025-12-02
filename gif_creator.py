import imageio.v3 as iio

filenames = ['pic-hair1.jpg', 'pic-hair2.jpg', 'pic-hair3.jpg', 'pic-hair4.jpg', 'pic-hair5.jpg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('hair.gif', images, duration = 500, loop = 0)