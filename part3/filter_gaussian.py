import matplotlib.pyplot as plt
from scipy.misc import imread
img = imread("Slides/Images/IMAG0537.jpg")

try:
    # http://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.gaussian
    from skimage.filters import gaussian
except ImportError:
    # Must be an older version of skimage...
    from skimage.filter import gaussian_filter as gaussian
blurred15 = gaussian(img, 15)

fig, (ax0, ax1) = plt.subplots(nrows=2)
ax0.imshow(img)
ax0.set_title("Original image")
ax0.axis("off")
ax1.imshow(blurred15)
ax1.set_title("Blurred using gaussian(15)")
ax1.axis("off")
plt.show()
