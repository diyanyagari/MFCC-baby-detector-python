import librosa
import matplotlib.pyplot as plt
# from dtw import dtw
import librosa.display
from fastdtw import fastdtw 
from scipy.spatial.distance import euclidean
import numpy as np
import json

#################################
array_hasil=[];
dataTemp=[];
print
for i in xrange(1, 31):
	for j in xrange(1, 31):
		distance, path = fastdtw((np.load('dataLatih/data'+ str(i) +'.json.npy')).T, (np.load('dataUjiFile/data'+ str(j) +'.json.npy')).T, dist=euclidean)
		if(dataTemp <= distance):
			dataTemp = dataTemp
		else:
			dataTemp = distance

	if(array_hasil<= dataTemp):
		array_hasil = array_hasil
	else :
		array_hasil = dataTemp

print array_hasil
###############################