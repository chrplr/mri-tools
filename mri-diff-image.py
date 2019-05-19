#! /usr/bin/env python
# Time-stamp: <2017-06-03 22:26:28 cp983411>

import sys

img1, img2, img3 = sys.argv[1:4]

import nibabel as nib

i1 = nib.load(img1)
i2 = nib.load(img2)

assert i1.header.get_data_shape == i2.header.get_data_shape()
assert i1.header.get_affine() == i2.header.get_affine()

i3data = i1.get_data() - i2.get_data()

i3 = nib.Nifti1Image(i3data, affine = i1.get_affine())

i3.save(img3)
