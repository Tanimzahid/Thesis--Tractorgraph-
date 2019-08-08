from tkinter import *
from dipy.viz import fvtk
from dipy.tracking.distances import bundles_distances_mam
from dipy.tracking.distances import bundles_distances_mdf
from nibabel import trackvis
from dipy.tracking.utils import length
import numpy as np
import nibabel
import os
import vtk.util.colors as colors
import _tkinter
import matplotlib.pyplot as plt
from dipy.tracking.vox2track import streamline_mapping
from dipy.tracking import utils
from dipy.tracking.distances import mam_distances 



def loadtrkfile(T_filename, threshold_short_streamlines=10.0):
    """Load tractogram from TRK file and remove short streamlines with
    length below threshold.
    """
    print("Loading %s" % T_filename)
    T, hdr = trackvis.read(T_filename, as_generator=False)
    T = np.array([s[0] for s in T], dtype=np.object)
    

   
    return T, hdr



if __name__ == '__main__':

	T_A_filename = 'F:\Thesis\data\\100307\\100307_af.left.trk'
	T_A,hdr= loadtrkfile(T_A_filename, threshold_short_streamlines=10.0) 
	
	T_A.tolist()
	T_A_filename2 = 'F:\Thesis\data\\124422\\124422_af.left.trk'
	#T_A_filename2 = 'F:\Thesis\data\\100307\\100307_af.right.trk'
	T_A2,hdr= loadtrkfile(T_A_filename2, threshold_short_streamlines=10.0) 
	T_A2.tolist()


	
	dis=mam_distances(T_A[0], T_A2[0], metric='avg' )


	print("Track Distance .. ")
	
	lengths = list(length(T_A))
	fig_hist, ax = plt.subplots()
	
	ax.plot(dis)
	plt.show()
	print(dis)
	
	
