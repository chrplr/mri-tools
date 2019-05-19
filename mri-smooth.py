#! /usr/bin/env python
# Time-stamp <2019-02-01 09:48:54 christophe@pallier.org>

""" Smooth a series of nifti image files.
See <https://matthew-brett.github.io/teaching/smoothing_intro.html>
"""

import sys
import os.path as op
import argparse
import nibabel
import nilearn.image

def batch_smooth(filelist, fwhm=4, verbose=False):
    l = len(filelist)
    for i, img in enumerate(filelist):
        folder, fname = op.split(img)
        sname = op.join(folder, 's' + fname)  # add prefix 's' to filename
        if (VERBOSE):
            print(f'{i + 1}/{l}: Smoothing @ {fwhm}mm "{img}" -> "{sname}"')
        sv = nilearn.image.smooth_img(img, fwhm=4)
        nibabel.save(sv, sname)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--fwhm', type=float, default=4.0,
                        help='Full Width at Half Maximum')
    parser.add_argument('--verbose', type=bool, default=True,
                        help='list files being converted')
    parser.add_argument('files', nargs='+',
                        action="append", default=[],
                        help='nifti files to smooth')

    args = parser.parse_args()

    FWHM = args.fwhm
    VERBOSE = args.verbose
    files = args.files[0]
    batch_smooth(files, fwhm=FWHM, verbose=VERBOSE)
