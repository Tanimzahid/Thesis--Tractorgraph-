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
    plt.show()

def load():
    T_A, hdr = loadtrkfile(T_A_filename, threshold_short_streamlines=threshold_short_streamlines) 
    

if __name__ == '__main__':
    
    print(__doc__)
    np.random.seed(0)

    T_A_filename = 'F:\Thesis\Resources\CST_L.trk'
 
    
    threshold_short_streamlines = 0.0     

    
   
    color=colors.red
    T_A, hdr = loadtrkfile(T_A_filename, threshold_short_streamlines=threshold_short_streamlines) 
    
    
    root = Tk()
    Frame= Frame(root)
    Frame.pack(fill=X)


    button1=Button(Frame,text="Load Tract",fg="blue",command=load)
    button2=Button(Frame,text="Show Tract",fg="blue",command=show_tract(T_A,color))
    button3=Button(Frame,text="Streamlines Count",fg="blue",command=countstreamlines)
    button4=Button(Frame,text="Show histogram",fg="blue",command=showhistogram)

    button1.pack(fill=X)
    button2.pack(fill=X)
    button3.pack(fill=X)
    button4.pack(fill=X)




    root.mainloop()


