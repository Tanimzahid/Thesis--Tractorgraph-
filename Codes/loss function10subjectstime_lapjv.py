import time

	
#from tkinter import *
#from lapjv import lapjv
#from dipy.viz import fvtk
from lapjv_1 import lapjv_func
from dipy.tracking.distances import bundles_distances_mam
from dipy.tracking.distances import bundles_distances_mdf
from nibabel import trackvis
from dipy.tracking.utils import length
import numpy as np
import copy
import scipy
import nibabel
import os
#import vtk.util.colors as colors
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
'''def show_tract(segmented_tract, color, match_trk):
	ren = fvtk.ren()           
	fvtk.add(ren, fvtk.line(segmented_tract.tolist(),colors=color, linewidth=2,opacity=0.3))
	fvtk.add(ren, fvtk.line(match_trk,colors=colors.green, linewidth=2,opacity=0.3))
	fvtk.show(ren)
	fvtk.clear(ren)'''
def pointmatch_greedy(dis):
	#print("Track Distance Greedy Method.. ") 
	start = time.time()	
	match2=[]
	onlydismatch2=[]
	for row_idx,row in enumerate (dis):
		for col_idx,element in enumerate(row):
			if element == min(dis[row_idx]):				
				match2.append([element,row_idx,col_idx])
				onlydismatch2.append([element])
				#np.append(match,row_idx)
				#np.append(match,col_idx)
				
				dis[:,col_idx]= 'inf'
				#print(element)
				#print()
				break
				
	match2= np.array(match2)
	match2=match2.reshape(len(T_A),3)	
	#print("total values in match")
	#print(len(match2))
	#print(match2)
	#print(dis)      
	sum1=sum(np.array(onlydismatch2)) 
	#print("loss function")
	#print(sum1)
	matchidx=match2[:,2]
	matchidx= np.array(matchidx)
	matchidx=matchidx.astype(int)

	match_trk1=[T_A2[i] for i in matchidx]
	end = time.time()
	totaltime=end - start	
	#show_tract(T_A,colors.red,match_trk1)
	return match_trk1,sum1,totaltime
def pointmatch_greedywithoutblock(dis): 
	start = time.time()
	"the code you want to test stays here"
    
	#print("Track Distance Greedy Method without blocking column.. ")    
	match=[]
	onlydismatch=[]
	for row_idx,row in enumerate (dis):
		for col_idx,element in enumerate(row):
			if element == min(dis[row_idx]):				
				match.append([element,row_idx,col_idx])
				onlydismatch.append([element])
				#np.append(match,row_idx)
				#np.append(match,col_idx)
				
				#dis[:,col_idx]= 'inf'
				#print(element)
				#print()
				break
	end = time.time()			
	match= np.array(match)
	match=match.reshape(len(T_A),3)	
	#print(dis)
	#print("total values in match")
	#print(len(match))
	#print(match)
	sum2=sum(np.array(onlydismatch))
	#print("loss function")
	#print(sum2)	
	matchidx=match[:,2]
	matchidx= np.array(matchidx)
	matchidx=matchidx.astype(int)

	match_trk4=[T_A2[i] for i in matchidx]
	
	totaltime=end - start
	#show_tract(T_A,colors.red,match_trk1)
	return match_trk4,sum2,totaltime	

def pointmatch_hungarian(dis,dis2):
	start = time.time()	
	row_ind, col_ind = linear_sum_assignment(dis)
	end = time.time()
	#print("Track Distance Hungarian Method.. ")
	
	match3=[]
	'''for row_idx,row in enumerate (dis2):
		for col_idx,element in enumerate(col_ind):
			#if element == min(dis[row_idx]):				
			match3.append(dis2[row_idx][element])'''
	for row,col in zip(row_ind,col_ind):
		match3.append(dis2[row,col])


		
		
	sum3=sum(np.array(match3))
	#print("total values in match")
	#print(len(match3))
	#print("loss function")
	#print(sum3)	
	#print(match3)
	#print(row_ind)
	#print(col_ind)
	match_trk2=[T_A2[i] for i in col_ind]
	
	
	totaltime=end - start	
	#show_tract(T_A,colors.red,match_trk2)
	return match_trk2,sum3,totaltime,row_ind,col_ind
	
def pointmatch_lapjv(dis,dis2):
   
     
	
	match4=[]
	start=time.time()
	col_ind= lapjv_func(dis)
	end = time.time()
	row_idx,col_idx=dis.shape
	row_idx2= list(range(row_idx))
	row_idx2=np.array(row_idx2)
	for i,j in zip(row_idx2,col_ind):
		match4.append(dis2[i][j])
		
			
	match_trk3=[T_A2[i] for i in col_ind]
	#match_trk2=[T_A2[i] for i in col_ind]
	sum4=sum(np.array(match4))
	
	totaltime=end - start	
	
	print("lapjv")
	return match_trk3,sum4,totaltime,row_idx2,col_ind
	

if __name__ == '__main__':

    
	loss_hungarian=[]
    
	loss_greedy=[]
    
	loss_greedy_withoutblock=[]
	loss_lapjv=[]
	time_hungarian=[]
	time_lapjv=[]
    
	time_greedy=[]
    
	time_greedy_withoutblock=[]	
	names1=['F:\Thesis\data\\100307\\100307_af.left.trk']
	#names1=['F:\Thesis\data\\100307\\100307_af.left.trk','F:\Thesis\data\\124422\\124422_af.left.trk','F:\Thesis\data\\161731\\161731_af.left.trk','F:\Thesis\data\\199655\\199655_af.left.trk','F:\Thesis\data\\201111\\201111_af.left.trk']
	names2=['F:\Thesis\data\\124422\\124422_af.left.trk','F:\Thesis\data\\161731\\161731_af.left.trk','F:\Thesis\data\\199655\\199655_af.left.trk','F:\Thesis\data\\201111\\201111_af.left.trk']  
    
	for x in names1:
		for y in names2:
			if x==y:
				continue
			T_A_filename = x
			T_A,hdr= loadtrkfile(T_A_filename, threshold_short_streamlines=10.0) 
			
			#T_A.tolist()
			T_A_filename2 = y
			#T_A_filename2 = 'F:\Thesis\data\\100307\\100307_af.right.trk'
			T_A2,hdr= loadtrkfile(T_A_filename2, threshold_short_streamlines=10.0) 
			#T_A2.tolist()


			
			#dis=[mam_distances(T_A[0], T_A2[0], metric='avg' ) for i in enumerate(0,len(T_A))]
			dis=[mam_distances(i, j, metric='avg' ) for i in T_A for j in T_A2]
			dis= np.array(dis)
			dis=dis.reshape(len(T_A), len(T_A2))
			dis2= copy.deepcopy(dis)
			dis3=copy.deepcopy(dis)

			#match_trk3=pointmatch_lapjv(dis)
			match_trk3,loss4,time4,row1,col1=pointmatch_lapjv(dis,dis3)
			loss_lapjv.append(loss4)
			time_lapjv.append(time4)			
			match_trk2,loss1,time1,row2,col2=pointmatch_hungarian(dis,dis2)
			loss_hungarian.append(loss1)
			time_hungarian.append(time1)
			match_trk1,loss2,time2=pointmatch_greedy(dis)
			loss_greedy.append(loss2)
			time_greedy.append(time2)
			match_trk4,loss3,time3=pointmatch_greedywithoutblock(dis)
			loss_greedy_withoutblock.append(loss3)
			time_greedy_withoutblock.append(time3)
			#print(x)
			#print(y)
			
			print("loss for greedy method" )
			print(loss2)
			print(time2)
			print("loss for greedy method without blocking column" )
			print(loss3)
			print(time3)
			print("loss for hungarian method" )
			print(loss1)
			print(time1)
			print("loss for lapjv method")
			print(loss4)
			print(time4)			
			
			


	#print("Track Distance .. ")
	
	#lengths = list(length(T_A))
	
	
	
	fig, ax = plt.subplots(1)
	ax.plot(loss_hungarian,'r',loss_greedy,'b',loss_greedy_withoutblock,'C7',loss_lapjv,'m')
	
	

	ax.set_title('loss function')
	plt.show()
	fig2, ax2 = plt.subplots(1)
	ax2.plot(time_hungarian,'r',time_greedy,'b',time_greedy_withoutblock,'C7',time_lapjv,'m')
	
	

	ax2.set_title('time needed for different algorithms')
	plt.show()


	
	#plt.show()
	#print(dis)
	
		