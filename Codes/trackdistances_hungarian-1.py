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
from scipy.optimize import linear_sum_assignment



def loadtrkfile(T_filename, threshold_short_streamlines=10.0):
    """Load tractogram from TRK file and remove short streamlines with
    length below threshold.
    """
    print("Loading %s" % T_filename)
    T, hdr = trackvis.read(T_filename, as_generator=False)
    T = np.array([s[0] for s in T], dtype=np.object)
    

   
    return T, hdr
def show_tract(segmented_tract, color, match_trk):
	ren = fvtk.ren()           
	fvtk.add(ren, fvtk.line(segmented_tract.tolist(),colors=color, linewidth=2,opacity=0.3))
	fvtk.add(ren, fvtk.line(match_trk,colors=colors.green, linewidth=2,opacity=0.3))
	fvtk.show(ren)
	fvtk.clear(ren)



if __name__ == '__main__':

	T_A_filename = 'F:\Thesis\data\\100307\\100307_af.left.trk'
	T_A,hdr= loadtrkfile(T_A_filename, threshold_short_streamlines=10.0) 
	
	#T_A.tolist()
	T_A_filename2 = 'F:\Thesis\data\\124422\\124422_af.left.trk'
	
	
	T_A2,hdr= loadtrkfile(T_A_filename2, threshold_short_streamlines=10.0) 
	#T_A2.tolist()


	
	#dis=[mam_distances(T_A[0], T_A2[0], metric='avg' ) for i in enumerate(0,len(T_A))]
	dis=[mam_distances(i, j, metric='avg' ) for i in T_A for j in T_A2]
	dis= np.array(dis)
	dis=dis.reshape(len(T_A), len(T_A2))
	row_ind, col_ind = linear_sum_assignment(dis)
	print("Track Distance Hungarian Method.. ")
	
	match_trk=[T_A2[i] for i in col_ind]
	show_tract(T_A,colors.red,match_trk)
	
			
	

	
	
	#lengths = list(length(T_A))
	#fig_hist, ax = plt.subplots()
	
	#ax.plot(dis)
	#plt.show()
	#print(dis)
	
	