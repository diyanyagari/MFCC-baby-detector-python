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
xrange = range
for i in xrange(1, 31):
	# print i
	# pathFileUji = 'dataLatih/data'+ str(i) +'.json.npy'
	for j in xrange(1, 31):
		distance, path = fastdtw((np.load('dataLatih/data'+ str(i) +'.json.npy')).T, (np.load('dataUjiFile/data'+ str(j) +'.json.npy')).T, dist=euclidean)
		# print pathFileUji
		if(dataTemp <= distance):
			dataTemp = dataTemp
		else:
			dataTemp = distance

	array_hasil.append(dataTemp)

print (array_hasil)
###############################