#! /usr/bin/env python
# Time-stamp: <2017-06-03 22:38:35 cp983411>

import argparse
import nibabel as nib
import numpy as np


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get information on mri files')
    parser.add_argument('files', nargs='+',
                        action="append", default=[],
                        help='image files to check')

    args = parser.parse_args()

    files = args.files[0]
    np.set_printoptions(precision=2, suppress=True)

    for f in files:
        print()
        print(f)
        i = nib.load(f)
        h = i.header
        print("  Voxel size:", end=" ")
        print(h.get_zooms())
        print("  Shape:", end=" ")
        print(h.get_data_shape())
        print('  Data type:', end=" ")
        print(h.get_data_dtype())
        print("  Affine:")
        print(i.affine)
