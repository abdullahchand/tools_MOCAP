from os.path import join
from os import makedirs
from glob import glob
import numpy as np
import pickle
import json

from shutil import copyfile
# copyfile(src, dst)
def convert_pkl2npz(inpath, outpath):
    fnames = sorted(glob(join(inpath, '*', '000.obj')))
    parms = {
        'poses': [],
        'trans': [],
        'betas': []
    }
    print(str(len(fnames)))
    count = 0
    for fname in fnames:
        copyfile(fname,outpath+str(count)+".obj")
        count+=1


def main():
    seq = 'no_frontal_reg_w_interp'
    inpath = '/mnt/g/Ubuntu/Movrs/MultiViewSmplfyX/MuVSx/MultiVIewSmplfyX/output_smpl/meshes/'
    outpath = '/mnt/g/Ubuntu/Movrs/MultiViewSMPL/objs_sequence/'
    convert_pkl2npz(inpath, outpath)


if __name__ == '__main__':
    main()
