import matplotlib.pyplot as plt
from scipy.misc import imread
img = imread("Slides/Images/IMAG0537.jpg")

from skimage.color import rgb2grey
try:
    # http://scikit-image.org/docs/dev/api/skimage.feature.html#skimage.feature.canny
    from skimage.filters import canny
except ImportError:
    # Must be an older version of skimage...
    from skimage.filter import canny

img_g = rgb2grey(img)
# Canny only accepts greyscale images.
edges = canny(img_g, 2)

fig, (ax0, ax1) = plt.subplots(nrows=2)
ax0.imshow(img_g, cmap=plt.cm.Greys_r)
ax0.set_title("Original image")
ax0.axis("off")
ax1.imshow(edges, cmap=plt.cm.Greys_r)
ax1.set_title("Edges by Canny")
ax1.axis("off")
plt.show()
