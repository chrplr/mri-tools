#! /usr/bin/env python
#! Time-stamp: <2019-02-01 11:01:01 christophe@pallier.org>

""" resample MRI images, changing the voxel size."""

import argparse
import os.path as op
import nibabel as nib
import numpy as np
from nilearn.image import resample_img


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--xyz', type=float, nargs=3,
                        help='new voxel size', default=(4, 4, 4))
    parser.add_argument('--verbose', type=bool, default=True,
                        help='list files being converted')
    parser.add_argument('files', nargs='+',
                        action="append", default=[],
                        help='nifti files to process')

    args = parser.parse_args()
    xyz = args.xyz

    prefix = "r{:.1f}x{:.1f}x{:.1f}_".format(xyz[0], xyz[1], xyz[2])

    VERBOSE = args.verbose
    files = args.files[0]

    l = len(files)
    for i, imgname in enumerate(files):
        folder, fname = op.split(imgname)
        sname = op.join(folder, prefix + fname)
        if (VERBOSE):
            print(f'{i + 1}/{l} Resampling to {xyz} "{imgname}" -> "{sname}"')
        img = nib.load(imgname)
        resampled = resample_img(img, np.diag(xyz))
        nib.save(resampled, sname)
