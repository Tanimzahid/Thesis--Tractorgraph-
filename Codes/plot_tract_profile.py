"""
==========================
Plotting tract profiles
==========================
An example of tracking and segmenting two tracts, and plotting their tract
profiles for FA (calculated with DTI).
"""
import os.path as op
import matplotlib.pyplot as plt
import numpy as np
import nibabel as nib
import dipy.data as dpd
from dipy.data import fetcher

import AFQ.utils.streamlines as aus
import AFQ.data as afd
import AFQ.tractography as aft
import AFQ.registration as reg
import AFQ.dti as dti
import AFQ.segmentation as seg
from nibabel import trackvis

def loadtrkfile(T_filename, threshold_short_streamlines=10.0):
    """Load tractogram from TRK file and remove short streamlines with
    length below threshold.
    """
    print("Loading %s" % T_filename)
    T, hdr = trackvis.read(T_filename, as_generator=False)
    T = np.array([s[0] for s in T], dtype=np.object)
   

   
    return T


T_A_filename = 'F:\Thesis\data\\100307\\100307_af.left.trk'
T_filename='F:\Thesis\data\\100307\\100307_af.left.trk'


T_A= loadtrkfile(T_A_filename, threshold_short_streamlines=10.0) 



FA_img = nib.load('F:\Thesis\data\\100307\\100307_data_b1k_1.25mm_FA.nii.gz')
FA_data = FA_img.get_data()

print("Extracting tract profiles...")
fig, ax = plt.subplots(1)
profile = seg.calculate_tract_profile(FA_data, T_A.tolist())
ax.plot(profile)
ax.set_title('bundle')

plt.show()