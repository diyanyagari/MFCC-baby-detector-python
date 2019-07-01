import librosa
import matplotlib.pyplot as plt
# from dtw import dtw
import librosa.display
from fastdtw import fastdtw 
from scipy.spatial.distance import euclidean
import numpy as np
import json

#Loading audio files
sample1, sampleLength1 = librosa.load('../sampleBabySound/every 7 sec/sample1.wav') 
sample2, sampleLength2 = librosa.load('../sampleBabySound/every 7 sec/sample2.wav') 
sample3, sampleLength3 = librosa.load('../sampleBabySound/every 7 sec/sample3.wav') 
sample4, sampleLength4 = librosa.load('../sampleBabySound/every 7 sec/sample4.wav') 
sample5, sampleLength5 = librosa.load('../sampleBabySound/every 7 sec/sample5.wav') 
sample6, sampleLength6 = librosa.load('../sampleBabySound/every 7 sec/sample6.wav') 
sample7, sampleLength7 = librosa.load('../sampleBabySound/every 7 sec/sample7.wav') 
sample8, sampleLength8 = librosa.load('../sampleBabySound/every 7 sec/sample8.wav') 
sample9, sampleLength9 = librosa.load('../sampleBabySound/every 7 sec/sample9.wav') 
sample10, sampleLength10 = librosa.load('../sampleBabySound/every 7 sec/sample10.wav') 
sample11, sampleLength11 = librosa.load('../sampleBabySound/every 7 sec/sample11.wav') 
sample12, sampleLength12 = librosa.load('../sampleBabySound/every 7 sec/sample12.wav') 
sample13, sampleLength13 = librosa.load('../sampleBabySound/every 7 sec/sample13.wav') 
sample14, sampleLength14 = librosa.load('../sampleBabySound/every 7 sec/sample14.wav') 
sample15, sampleLength15 = librosa.load('../sampleBabySound/every 7 sec/sample15.wav') 
sample16, sampleLength16 = librosa.load('../sampleBabySound/every 7 sec/sample16.wav') 
sample17, sampleLength17 = librosa.load('../sampleBabySound/every 7 sec/sample17.wav') 
sample18, sampleLength18 = librosa.load('../sampleBabySound/every 7 sec/sample18.wav') 
sample19, sampleLength19 = librosa.load('../sampleBabySound/every 7 sec/sample19.wav') 
sample20, sampleLength20 = librosa.load('../sampleBabySound/every 7 sec/sample20.wav') 
sample21, sampleLength21 = librosa.load('../sampleBabySound/every 7 sec/sample21.wav') 
sample22, sampleLength22 = librosa.load('../sampleBabySound/every 7 sec/sample22.wav') 
sample23, sampleLength23 = librosa.load('../sampleBabySound/every 7 sec/sample23.wav') 
sample24, sampleLength24 = librosa.load('../sampleBabySound/every 7 sec/sample24.wav') 
sample25, sampleLength25 = librosa.load('../sampleBabySound/every 7 sec/sample25.wav') 
sample26, sampleLength26 = librosa.load('../sampleBabySound/every 7 sec/sample26.wav') 
sample27, sampleLength27 = librosa.load('../sampleBabySound/every 7 sec/sample27.wav') 
sample28, sampleLength28 = librosa.load('../sampleBabySound/every 7 sec/sample28.wav') 
sample29, sampleLength29 = librosa.load('../sampleBabySound/every 7 sec/sample29.wav') 
sample30, sampleLength30 = librosa.load('../sampleBabySound/every 7 sec/sample30.wav')

mfcc1 = librosa.feature.mfcc(sample1,sampleLength1,n_mfcc=40)   #Computing MFCC values
mfcc2 = librosa.feature.mfcc(sample2,sampleLength2,n_mfcc=40)   #Computing MFCC values
mfcc3 = librosa.feature.mfcc(sample3,sampleLength3,n_mfcc=40)   #Computing MFCC values
mfcc4 = librosa.feature.mfcc(sample4,sampleLength4,n_mfcc=40)   #Computing MFCC values
mfcc5 = librosa.feature.mfcc(sample5,sampleLength5,n_mfcc=40)   #Computing MFCC values
mfcc6 = librosa.feature.mfcc(sample6,sampleLength6,n_mfcc=40)   #Computing MFCC values
mfcc7 = librosa.feature.mfcc(sample7,sampleLength7,n_mfcc=40)   #Computing MFCC values
mfcc8 = librosa.feature.mfcc(sample8,sampleLength8,n_mfcc=40)   #Computing MFCC values
mfcc9 = librosa.feature.mfcc(sample9,sampleLength9,n_mfcc=40)   #Computing MFCC values
mfcc10 = librosa.feature.mfcc(sample10,sampleLength10,n_mfcc=40)   #Computing MFCC values
mfcc11 = librosa.feature.mfcc(sample11,sampleLength11,n_mfcc=40)   #Computing MFCC values
mfcc12 = librosa.feature.mfcc(sample12,sampleLength12,n_mfcc=40)   #Computing MFCC values
mfcc13 = librosa.feature.mfcc(sample13,sampleLength13,n_mfcc=40)   #Computing MFCC values
mfcc14 = librosa.feature.mfcc(sample14,sampleLength14,n_mfcc=40)   #Computing MFCC values
mfcc15 = librosa.feature.mfcc(sample15,sampleLength15,n_mfcc=40)   #Computing MFCC values
mfcc16 = librosa.feature.mfcc(sample16,sampleLength16,n_mfcc=40)   #Computing MFCC values
mfcc17 = librosa.feature.mfcc(sample17,sampleLength17,n_mfcc=40)   #Computing MFCC values
mfcc18 = librosa.feature.mfcc(sample18,sampleLength18,n_mfcc=40)   #Computing MFCC values
mfcc19 = librosa.feature.mfcc(sample19,sampleLength19,n_mfcc=40)   #Computing MFCC values
mfcc20 = librosa.feature.mfcc(sample20,sampleLength20,n_mfcc=40)   #Computing MFCC values
mfcc21 = librosa.feature.mfcc(sample21,sampleLength21,n_mfcc=40)   #Computing MFCC values
mfcc22 = librosa.feature.mfcc(sample22,sampleLength22,n_mfcc=40)   #Computing MFCC values
mfcc23 = librosa.feature.mfcc(sample23,sampleLength23,n_mfcc=40)   #Computing MFCC values
mfcc24 = librosa.feature.mfcc(sample24,sampleLength24,n_mfcc=40)   #Computing MFCC values
mfcc25 = librosa.feature.mfcc(sample25,sampleLength25,n_mfcc=40)   #Computing MFCC values
mfcc26 = librosa.feature.mfcc(sample26,sampleLength26,n_mfcc=40)   #Computing MFCC values
mfcc27 = librosa.feature.mfcc(sample27,sampleLength27,n_mfcc=40)   #Computing MFCC values
mfcc28 = librosa.feature.mfcc(sample28,sampleLength28,n_mfcc=40)   #Computing MFCC values
mfcc29 = librosa.feature.mfcc(sample29,sampleLength29,n_mfcc=40)   #Computing MFCC values
mfcc30 = librosa.feature.mfcc(sample30,sampleLength30,n_mfcc=40)   #Computing MFCC values

np.save('dataLatih/data1.json', mfcc1)
np.save('dataLatih/data2.json', mfcc2)
np.save('dataLatih/data3.json', mfcc3)
np.save('dataLatih/data4.json', mfcc4)
np.save('dataLatih/data5.json', mfcc5)
np.save('dataLatih/data6.json', mfcc6)
np.save('dataLatih/data7.json', mfcc7)
np.save('dataLatih/data8.json', mfcc8)
np.save('dataLatih/data9.json', mfcc9)
np.save('dataLatih/data10.json', mfcc10)
np.save('dataLatih/data11.json', mfcc11)
np.save('dataLatih/data12.json', mfcc12)
np.save('dataLatih/data13.json', mfcc13)
np.save('dataLatih/data14.json', mfcc14)
np.save('dataLatih/data15.json', mfcc15)
np.save('dataLatih/data16.json', mfcc16)
np.save('dataLatih/data17.json', mfcc17)
np.save('dataLatih/data18.json', mfcc18)
np.save('dataLatih/data19.json', mfcc19)
np.save('dataLatih/data20.json', mfcc20)
np.save('dataLatih/data21.json', mfcc21)
np.save('dataLatih/data22.json', mfcc22)
np.save('dataLatih/data23.json', mfcc23)
np.save('dataLatih/data24.json', mfcc24)
np.save('dataLatih/data25.json', mfcc25)
np.save('dataLatih/data26.json', mfcc26)
np.save('dataLatih/data27.json', mfcc27)
np.save('dataLatih/data28.json', mfcc28)
np.save('dataLatih/data29.json', mfcc29)
np.save('dataLatih/data30.json', mfcc30)

# t = np.load('data.json.npy')
# print t