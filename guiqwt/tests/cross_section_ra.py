# -*- coding: utf-8 -*-
#
# Copyright © 2009-2010 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see guiqwt/__init__.py for details)

"""Radially-averaged cross section test"""

SHOW = True # Show test in GUI-based test launcher

import os.path as osp, numpy as np

from guiqwt.plot import ImageDialog
from guiqwt.builder import make
from guiqwt.cross_section import RACrossSection
from guiqwt.tools import RACrossSectionTool, ImageMaskTool

from guiqwt.tests.image import compute_image

class TestImageDialog(ImageDialog):
    def create_plot(self, options, row=0, column=0, rowspan=1, columnspan=1):
        ImageDialog.create_plot(self, options, row, column, rowspan, columnspan)
        ra_panel = RACrossSection(self)
        self.plot_layout.addWidget(ra_panel, 1, 0)
        self.add_panel(ra_panel)

def test():
    """Test"""
    # -- Create QApplication
    import guidata
    guidata.qapplication()
    # --
    filename = osp.join(osp.dirname(__file__), "brain.png")
    win = TestImageDialog(toolbar=True, wintitle="Radially-averaged cross "
                                                 "section test")
    win.add_tool(RACrossSectionTool)
    tool = win.add_tool(ImageMaskTool)
    win.resize(600, 600)
    data = compute_image(4000, grid=False)
#    data = np.uint16((data+1)*32767)
#    data = np.int16(data*32767)
    data = data[:2000, :2000]
    print data.dtype
    image = make.maskedimage(data, colormap="bone")
#    data2 = np.array(image.data.T[200:], copy=True)
#    image2 = make.image(data2, title="Modified", alpha_mask=True)
    plot = win.get_plot()
    plot.add_item(image)
#    plot.add_item(image2, z=1)
    win.exec_()

if __name__ == "__main__":
    test()