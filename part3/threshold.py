import matplotlib.pyplot as plt
from scipy.misc import imread
img = imread("Slides/Images/IMAG0537.jpg")

from skimage.color import rgb2grey

img_g = rgb2grey(img)
# We just take a guess: half the max.
t = img_g.max() / 2.0
thresh = img_g > t

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)
ax0.imshow(img_g, cmap=plt.cm.Greys_r)
ax0.set_title("Original image")
ax0.axis("off")
ax1.hist(img_g)
ax1.set_title("Histogram, t = %2f" % t)
ax1.axvline(t, color='r')
ax2.imshow(thresh, cmap=plt.cm.Greys_r)
ax2.set_title("Thresholded at %.2f" % t)
ax2.axis("off")
plt.show()
