#!/usr/bin/env python

from __future__ import print_function

import sys

import matplotlib.cm as cm
import matplotlib.figure as plotfig
import matplotlib.pyplot as plotter
import numpy as np

from scipy import misc as scipy_misc
from skimage.filter import sobel

IMG_FNAME = sys.argv[1]
img = scipy_misc.imread(IMG_FNAME)

if img.dtype == np.uint8:
    mmm_fmt = "%d/%d/%d"
else:
    mmm_fmt = "%.1f/%.1f/%.1f"
info = "Image: shape=%s, dtype=%s, max/mean/min = " + mmm_fmt
print(info % (img.shape, img.dtype, img.max(), img.mean(), img.min()))


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
    chan = sobel(img[...,i])
    add_subplot(fig, plot_shape, i+1, chan, chan_name)#, cmap=cm.Greys_r)

plotter.show()

