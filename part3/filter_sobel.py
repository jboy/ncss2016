import matplotlib.pyplot as plt
from scipy.misc import imread
img = imread("Slides/Images/IMAG0537.jpg")

from skimage.color import rgb2grey
try:
    # http://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.sobel
    from skimage.filters import sobel
except ImportError:
    # Must be an older version of skimage...
    from skimage.filter import sobel

img_g = rgb2grey(img)
# Sobel only accepts greyscale images.
gradients = sobel(img_g)

fig, (ax0, ax1) = plt.subplots(nrows=2)
ax0.imshow(img_g, cmap=plt.cm.Greys_r)
ax0.set_title("Original image")
ax0.axis("off")
ax1.imshow(gradients)
ax1.set_title("Gradients by Sobel")
ax1.axis("off")
plt.show()
