import matplotlib.pyplot as plt
from scipy.misc import imread
img = imread("Slides/Images/IMAG0537.jpg")

from skimage.color import rgb2grey
try:
    # http://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.threshold_otsu
    from skimage.filters import threshold_otsu
except ImportError:
    # Must be an older version of skimage...
    from skimage.filter import threshold_otsu

img_g = rgb2grey(img)
# Otsu determines the "optimal" threshold.
t = threshold_otsu(img_g)
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
