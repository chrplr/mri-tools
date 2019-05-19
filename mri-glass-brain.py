#! /usr/bin/env python3
# Time-stamp: <2019-02-01 12:01:40 christophe@pallier.org>


""" Plot activations (mri images) on glass-brains. """


import sys
import os.path as op
import argparse
import nibabel
import nilearn.image
import nilearn.plotting
from matplotlib.backends.backend_pdf import PdfPages


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot activations on glass-brains.')
    parser.add_argument('--threshold', type=float, default=3.1,
                        help='Threshold')
    parser.add_argument('files', nargs='+',
                        action="append", default=[],
                        help='nifti files to display')

    args = parser.parse_args()

    pdf = PdfPages('output.pdf')

    for f in args.files[0]:
        print(f)
        disp = nilearn.plotting. plot_glass_brain(f,
                                                  threshold=args.threshold,
                                                  display_mode='lyrz',
                                                  colorbar=True,
                                                  title=f)
        pdf.savefig()
        disp.close()

    pdf.close()
