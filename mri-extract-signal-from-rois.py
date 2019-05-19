#! /usr/bin/env python
# Time-stamp: <2019-05-19 10:54:12 christophe@pallier.org>


"""Usage: extract_signal_from_rois -m MASKSPATTERN -i IMAGESPATTERN -o OUTPUT_CSVFILE

Extract average values in a set of masks from a set of images. 
Notes:
 * This is basically a wrapper around nilearn's NiftiMapsMasker.fit_transform.
 * The masks and images must have the same bounding box.

Arguments:
  -m MASKSPATTERN          glob pattern for 3D binary images used as masks
  -i IMAGESPATTERN         glob pattern for brain images
  -o OUTPUT_CSVFILE        name of the output dataframe with 3 columns: images,  roi, value


"""

import sys
from glob import glob
import os
import os.path as op
from docopt import docopt
import pandas as pd
from nilearn.input_data import NiftiMapsMasker


def extract_data(images, masks):
    """ given a set of brain images and a set of masks,  extract the average signal inside each mask for each brain image.
        Returns a dataframe with 3 columns: image, mask, value.
    """

    masker = NiftiMapsMasker(masks)
    values = masker.fit_transform(images)
    nimgs, nmasks = values.shape


    cp = op.commonpath(images)
    labelsimages = [i.replace(cp, '') for i in images]
    print(cp)
    print(labelsimages)

    cpmask =  op.commonprefix(masks)
    labelsrois = [i.replace(cpmask, '').replace('.nii.gz', '') for i in masks]
    print(cpmask)
    print(labelsrois)

    df = pd.DataFrame(columns=['image', 'mask', 'value'])
    row = 0
    for iimg in range(nimgs):
        for iroi in range(nmasks):
            df.loc[row] = pd.Series({'image': labelsimages[iimg] ,
                                   'mask': labelsrois[iroi],
                                   'value': values[iimg, iroi]})
            row = row + 1
    return df


if __name__ == '__main__':
    args = docopt(__doc__, help=True)  # parse arguments based on docstring above
    outputfname = args['-o']

    maskspattern = args['-m']
    masks = glob(maskspattern)
    if masks == []:
        print(f'could not find files {maskspattern}')
        sys.exit(1)

    imagespattern = args['-i']
    images = glob(imagespattern)
    if images == []:
        print(f'could not find files {imagespattern}')
        sys.exit(1)

    df = extract_data(images, masks)
    df.to_csv(outputfname, index=False)
