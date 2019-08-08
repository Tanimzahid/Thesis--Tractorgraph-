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
#fig, ax = plt.subplots(1)
profile1 = seg.calculate_tract_profile(FA_data, T_A.tolist())
#ax.plot(profile1)
#####################################################################

T_A_filename = 'F:\Thesis\data\\201111\\201111_af.left.trk'
T_filename='F:\Thesis\data\\201111\\201111_af.left.trk'


T_A= loadtrkfile(T_A_filename, threshold_short_streamlines=10.0) 



FA_img = nib.load('F:\Thesis\data\\201111\\201111_data_b1k_1.25mm_FA.nii.gz')
FA_data = FA_img.get_data()

print("Extracting tract profiles...")
#fig, ax = plt.subplots(1)
profile2 = seg.calculate_tract_profile(FA_data, T_A.tolist())
#ax.plot(profile2)
#####################################################################
T_A_filename = 'F:\Thesis\data\\124422\\124422_af.left.trk'
T_filename='F:\Thesis\data\\124422\\124422_af.left.trk'


T_A= loadtrkfile(T_A_filename, threshold_short_streamlines=10.0) 



FA_img = nib.load('F:\Thesis\data\\124422\\124422_data_b1k_1.25mm_FA.nii.gz')
FA_data = FA_img.get_data()

print("Extracting tract profiles...")
#fig, ax = plt.subplots(1)
profile3 = seg.calculate_tract_profile(FA_data, T_A.tolist())
#ax.plot(profile3)
###########################################################

T_A_filename = 'F:\Thesis\data\\161731\\161731_af.left.trk'
T_filename='F:\Thesis\data\\161731\\161731_af.left.trk'


T_A= loadtrkfile(T_A_filename, threshold_short_streamlines=10.0) 



FA_img = nib.load('F:\Thesis\data\\161731\\161731_data_b1k_1.25mm_FA.nii.gz')
FA_data = FA_img.get_data()

print("Extracting tract profiles...")
#fig, ax = plt.subplots(1)
profile4 = seg.calculate_tract_profile(FA_data, T_A.tolist())
#ax.plot(profile4)


##########################################################
T_A_filename = 'F:\Thesis\data\\199655\\199655_af.left.trk'
T_filename='F:\Thesis\data\\199655\\199655_af.left.trk'


T_A= loadtrkfile(T_A_filename, threshold_short_streamlines=10.0) 



FA_img = nib.load('F:\Thesis\data\\199655\\199655_data_b1k_1.25mm_FA.nii.gz')
FA_data = FA_img.get_data()

print("Extracting tract profiles...")
fig, ax = plt.subplots(1)
profile5 = seg.calculate_tract_profile(FA_data, T_A.tolist())
#ax.plot(profile1,'r',profile2,'b',profile3,'g',profile4,'y',profile5,'o')
ax.plot(profile1,'C7',profile2,'C7',profile3,'C7',profile4,'C7',profile5,'C7')
#ax.plot(profile5)
############################################################

avg = [(profile1[j] + profile2[j]+ profile3[j]+profile4[j]+ profile5[j])/5 for j in range(0,100)]
fig, ax = plt.subplots(1)
ax.plot(profile1,'C7',profile2,'C7',profile3,'C7',profile4,'C7',profile5,'C7',avg,'r')


ax.set_title('bundle')
plt.show()