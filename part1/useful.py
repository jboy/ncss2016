# This is a collection of useful functions for commonly-used settings.
# It might save you some typing...

from __future__ import print_function

import matplotlib.cm as cm
import matplotlib.pyplot as mplt
import numpy as np


def show_greyscale_image(img, smooth=False, use_false_colours=False):
    """Show a greyscale image using Matplotlib.

    If `smooth` is True, use default Matplotlib image smoothing.
    If `use_false_colours` is True, render the image using default
    Matplotlib false colours rather than greyscale.
    """
    if len(img.shape) > 2:
        # The image is not greyscale. :(
        raise ValueError("image is not greyscale: it has shape %s" %
                str(img.shape))

    colourmap = None if use_false_colours else cm.Greys_r
    if smooth:
        mplt.imshow(img, cmap=colourmap)
    else:
        mplt.imshow(img, cmap=colourmap, interpolation="none")
    mplt.show()


def show_colour_image(img, smooth=False):
    """Show a colour image using Matplotlib.

    If `smooth` is True, use default Matplotlib image smoothing.
    """
    if len(img.shape) < 3:
        # The image is not colour. :(
        raise ValueError("image is not colour: it has shape %s" %
                str(img.shape))

    if smooth:
        mplt.imshow(img)
    else:
        mplt.imshow(img, interpolation="none")
    mplt.show()


def as_uint8(img, shift_min_to_0=False, scale_max_to_255=False):
    """Convert an image to data-type uint8, re-scaling if desired.

    This function is useful because if we ask Matplotlib to render an image
    of data-type float32 or float64, Matplotlib will auto-rescale the image
    into the range [0, 255], which may not be what we want.  But if we pass
    an image of data-type uint8 to Matplotlib, it won't be re-scaled.

    Since images of data-type float32 or float64 are often in the range
    [0.0, 1.0] or [-1.0, 1.0], if it looks like this image is using one of
    these ranges, multiply it by 255.0.
    """
    if img.dtype.kind == 'f':
        # It's a floating point data-type.
        if img.min() > -1.0001 and img.max() < 1.0001:
            # Assume it's in range [0.0, 1.0] or [-1.0, 1.0].
            img = img * 255  # Scale it into range [0.0, 255.0].
        else:
            img = img.copy()  # Just create a fresh copy for us to edit.
    elif shift_min_to_0 or scale_max_to_255:
        # The image has an integer data-type rather than floating-point.
        # Convert it to floating-point for shifting & scaling.
        img = img.astype(np.float32)

    if shift_min_to_0:
        img -= img.min()

    # Be wary of division-by-zero and negative maxima.
    img_max = img.max()
    if scale_max_to_255 and img_max > 0.0:
        img *= (255.0 / img_max)

    if img.dtype.kind == 'f':
        return np.clip(img, 0.0, 255.0).astype(np.uint8)
    else:
        return np.clip(img, 0, 255).astype(np.uint8)


if __name__ == "__main__":
    # Test / usage demo
    from skimage import data
    camera = data.camera()
    show_greyscale_image(camera, smooth=True, use_false_colours=True)
    #show_colour_image(camera, smooth=True)  # raises ValueError

