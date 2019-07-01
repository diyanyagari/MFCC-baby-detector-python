import librosa
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
from fastdtw import fastdtw 
from dtw import dtw
from scipy.spatial.distance import euclidean

#library for telegram only mang
import sys
import time
import random
import datetime
import telepot

#Load music file
ySample1, srSample1 = librosa.load('baby_crying_1.wav')
ySample2, srSample2 = librosa.load('baby_crying_2.wav')
ySample3, srSample3 = librosa.load('baby_crying_3.wav')
ySample4, srSample4 = librosa.load('baby_crying_4.wav')
ySample5, srSample5 = librosa.load('baby_crying_5.wav')
y2, sr2 = librosa.load('test_baby.wav')


plt.subplot(1, 2, 1) 
mfccSample1 = librosa.feature.mfcc(ySample1,srSample1)   #Computing MFCC values
# mfccSample2 = librosa.feature.mfcc(ySample2,srSample2)   #Computing MFCC values
# mfccSample3 = librosa.feature.mfcc(ySample3,srSample3)   #Computing MFCC values
# mfccSample4 = librosa.feature.mfcc(ySample4,srSample4)   #Computing MFCC values
# mfccSample5 = librosa.feature.mfcc(ySample5,srSample5)   #Computing MFCC values
librosa.display.specshow(mfccSample1)




plt.subplot(1, 2, 2)
mfcc2 = librosa.feature.mfcc(y2, sr2)
librosa.display.specshow(mfcc2)

bot = telepot.Bot('752717879:AAFXx5ds3hatUt3be2HHsWMGvcJzA0-lLZs')
chat_id_bot = 735576128
chat_id_bot2 = 800079371
chat_id_bot3 = 886011927

def handleTelegram(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    res = dtw_calculation()
    print res
    if res == True:
        bot.sendMessage(chat_id, "Baby Detected")
    elif res == False:
        bot.sendMessage(chat_id, "Baby's Not Crying")

# cost, path = fastdtw (mfcc1.T, mfcc2.T)
def dtw_calculation():
    dist1, path1 = fastdtw (mfccSample1.T, mfcc2.T)

    plt.imshow(mfccSample1.T)
    plt.plot(path[0], path[1], 'w') 

    plt.show() 

    # dist2, path2 = fastdtw (mfccSample2.T, mfcc2.T)
    # dist3, path3 = fastdtw (mfccSample3.T, mfcc2.T)
    # dist4, path4 = fastdtw (mfccSample4.T, mfcc2.T)
    # dist5, path5 = fastdtw (mfccSample5.T, mfcc2.T)

    
    # distance, path = fastdtw(mfcc1.T, mfcc2.T, dist=euclidean)
    # print distance
    # x, y = dtw(mfcc1.T, mfcc2.T)
    # if (distance < 2349538):
        # bot.sendMessage(chat_id_bot, "We're detected your baby is crying")
        # bot.sendMessage(chat_id_bot2, "We're detected your baby is crying")
        # bot.sendMessage(chat_id_bot3, "We're detected your baby is crying")
    #     return True
    # else:
        # bot.sendMessage(chat_id_bot, "Baby's Not Crying")
        # bot.sendMessage(chat_id_bot2, "Baby's Not Crying")
        # bot.sendMessage(chat_id_bot3, "Baby's Not Crying")
        # return False

dtw_calculation()

# plt.imshow(cost.T)
# plt.plot(path[0], path[1], 'w') 

# plt.show()  



#baby_crying_1 >< test_baby1 =  774764.690194
#baby_crying_1 >< baby_crying_1 =  2495471.61897
#baby_crying_1_mono >< test_baby =  685120.16322
