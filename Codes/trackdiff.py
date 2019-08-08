from tkinter import *
from dipy.viz import fvtk
from dipy.tracking.distances import bundles_distances_mam
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






def loadtrkfile(T_filename, threshold_short_streamlines=10.0):
    """Load tractogram from TRK file and remove short streamlines with
    length below threshold.
    """
    print("Loading %s" % T_filename)
    T, hdr = trackvis.read(T_filename, as_generator=False)
    T = np.array([s[0] for s in T], dtype=np.object)
   

   
    return T, hdr




def show_tract(segmented_tract, color):
    ren = fvtk.ren()           
    fvtk.add(ren, fvtk.line(segmented_tract.tolist(),colors=color, linewidth=2,opacity=0.3))
    fvtk.show(ren)
    fvtk.clear(ren)




def countstreamlines():
    print("total %s streamlines" % ( len(T_A)))



def showhistogram():
    lengths = list(length(T_A))
    fig_hist, ax = plt.subplots()
    ax.hist(lengths, color='burlywood')
    ax.set_xlabel('Length')
    ax.set_ylabel('Count')
    plt.savefig("F:\Thesis\ss\\201111_uf.right.png")
    plt.show()

def load():
    T_A, hdr = loadtrkfile(T_A_filename, threshold_short_streamlines=threshold_short_streamlines) 
    

if __name__ == '__main__':
    
    print(__doc__)
    np.random.seed(0)

    T_A_filename = 'F:\Thesis\Resources\\alldata\\201111_uf.right.trk'
 
    
    threshold_short_streamlines = 0.0     

    
   
    color=colors.red
    T_A, hdr = loadtrkfile(T_A_filename, threshold_short_streamlines=threshold_short_streamlines) 
    
    countstreamlines()
    showhistogram()
    
    
    

    tractography,header=trackvis.read(T_A_filename)

    tractography = [streamline[0] for streamline in tractography]

    affine=utils.affine_for_trackvis(voxel_size=np.array([2,2,2]))

  

    print ("---Number of voxel---")

    print (len(streamline_mapping(T_A,affine=affine).keys()))
    show_tract(T_A, color)
    
