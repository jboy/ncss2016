#!/usr/bin/env python3
#
# Usage:
#  python3 display_rgb_grey.py some-image.jpg

from __future__ import print_function

import sys

import matplotlib as mp
import matplotlib.cm as cm
import matplotlib.figure as plotfig
import matplotlib.pyplot as plotter
import numpy as np
import scipy
import skimage

from scipy import misc as scipy_misc
from skimage import color as skimage_color

IMG_FNAME = sys.argv[1]
img = scipy_misc.imread(IMG_FNAME)
print("Image: shape=%s, dtype=%s, max/mean/min = %.1f/%.1f/%.1f" %
        (img.shape, img.dtype, img.max(), img.mean(), img.min()))


def add_subplot(fig, plot_shape, subplot_idx, img, subplot_title,
        do_plot_hist=False, cmap=None):
    (num_rows, num_cols) = plot_shape
    sub = fig.add_subplot(num_rows, num_cols, subplot_idx+1)
    if do_plot_hist:
        sub.hist(img.ravel(), bins=255, histtype='step', color='black')
        sub.set_xticklabels([])
        sub.set_yticklabels([])
    else:
        sub.axis("off")
        sub.imshow(img, cmap)

    sub.set_title(subplot_title,
            # For more info on the `fontdict` parameter, see:
            #  http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.text
            fontdict=dict(size="small"))

    return sub

plot_title = "Show R, G, B channels"
# Remove all the wasted space around the plot.
subplot_params = plotfig.SubplotParams(
        left=0.02, bottom=0.02, right=0.98, top=0.96)
fig = plotter.figure(plot_title, frameon=False, subplotpars=subplot_params)

plot_shape = (2, 2)
add_subplot(fig, plot_shape, 0, img, "colour")

for i, chan_name in enumerate("RGB"):
    chan = img[...,i]
    #colour = np.zeros_like(img)
    #colour[...,i] = chan[...]
    add_subplot(fig, plot_shape, i+1, chan, chan_name, cmap=cm.Greys_r)
    #add_subplot(fig, plot_shape, i+1, colour, chan_name)

plotter.show()

