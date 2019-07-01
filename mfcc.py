import librosa
import matplotlib.pyplot as plt
# from dtw import dtw
import librosa.display
from fastdtw import fastdtw 
from scipy.spatial.distance import euclidean
import numpy as np
import json


# PENGUJIAN 
# sample1, sampleLength1 = librosa.load('dataUji/dataUji1.wav')
# sample2, sampleLength2 = librosa.load('sampleBabySound/every 7 sec/sample2.wav') 
# sample3, sampleLength3 = librosa.load('sampleBabySound/every 7 sec/sample3.wav') 
# sample4, sampleLength4 = librosa.load('sampleBabySound/every 7 sec/sample4.wav') 
# sample5, sampleLength5 = librosa.load('sampleBabySound/every 7 sec/sample5.wav') 
# sample6, sampleLength6 = librosa.load('sampleBabySound/every 7 sec/sample6.wav') 
# sample7, sampleLength7 = librosa.load('sampleBabySound/every 7 sec/sample7.wav') 
# sample8, sampleLength8 = librosa.load('sampleBabySound/every 7 sec/sample8.wav') 
# sample9, sampleLength9 = librosa.load('sampleBabySound/every 7 sec/sample9.wav') 
# sample10, sampleLength10 = librosa.load('sampleBabySound/every 7 sec/sample10.wav') 
# sample11, sampleLength11 = librosa.load('sampleBabySound/every 7 sec/sample11.wav') 
# sample12, sampleLength12 = librosa.load('sampleBabySound/every 7 sec/sample12.wav') 
# sample13, sampleLength13 = librosa.load('sampleBabySound/every 7 sec/sample13.wav') 
# sample14, sampleLength14 = librosa.load('sampleBabySound/every 7 sec/sample14.wav') 
# sample15, sampleLength15 = librosa.load('sampleBabySound/every 7 sec/sample15.wav') 
# sample16, sampleLength16 = librosa.load('sampleBabySound/every 7 sec/sample16.wav') 
# sample17, sampleLength17 = librosa.load('sampleBabySound/every 7 sec/sample17.wav') 
# sample18, sampleLength18 = librosa.load('sampleBabySound/every 7 sec/sample18.wav') 
# sample19, sampleLength19 = librosa.load('sampleBabySound/every 7 sec/sample19.wav') 
# sample20, sampleLength20 = librosa.load('sampleBabySound/every 7 sec/sample20.wav') 
# sample21, sampleLength21 = librosa.load('sampleBabySound/every 7 sec/sample21.wav') 
# sample22, sampleLength22 = librosa.load('sampleBabySound/every 7 sec/sample22.wav') 
# sample23, sampleLength23 = librosa.load('sampleBabySound/every 7 sec/sample23.wav') 
# sample24, sampleLength24 = librosa.load('sampleBabySound/every 7 sec/sample24.wav') 
# sample25, sampleLength25 = librosa.load('sampleBabySound/every 7 sec/sample25.wav') 
# sample26, sampleLength26 = librosa.load('sampleBabySound/every 7 sec/sample26.wav') 
# sample27, sampleLength27 = librosa.load('sampleBabySound/every 7 sec/sample27.wav') 
# sample28, sampleLength28 = librosa.load('sampleBabySound/every 7 sec/sample28.wav') 
# sample29, sampleLength29 = librosa.load('sampleBabySound/every 7 sec/sample29.wav') 
# sample30, sampleLength30 = librosa.load('sampleBabySound/every 7 sec/sample30.wav')

#Showing multiple plots using subplot
plt.subplot(1, 2, 1) 
mfcc1 = librosa.feature.mfcc(sample1,sampleLength1,n_mfcc=40)   #Computing MFCC values
librosa.display.specshow(mfcc1)

plt.subplot(1, 2, 2)
mfcc2 = librosa.feature.mfcc(sample2, sampleLength2,n_mfcc=40)
librosa.display.specshow(mfcc2)
print mfcc2

# plt.figure(figsize=(10, 4))
# librosa.display.specshow(mfcc1, x_axis='time')
# plt.colorbar()



with open('data.json', 'w') as f:
    for item in mfcc1:
        print >> f, item

jsonString  = json.dumps(mfcc1)
print jsonString
print mfcc1
np.save('data.json', mfcc1)
print mfcc1

# np.save('allDistanceData.json', array_hasil)
# print array_hasil


# latih = np.load('dataLatih/data1.json.npy')
# uji = np.load('dataUjiFile/data1.json.npy')


# with open('data.txt', 'r+') as json_file:
      # json_data = json.load(json_file)
      # people = json_data['people']
      # people.append({"firstName":"Mehmet"})
      # json_file.seek(0, 0)
      # jsonString = json.dumps(mfcc1)
      # json_file.write(mfcc1)
      # json_file.truncate()

# print np.loadtxt("data.json")

#menampilkan FREQUENCY
plt.tight_layout()
plt.ylabel("dB", fontsize=10)
plt.xlabel("freq", fontsize=10)
plt.plot(mfcc2)
plt.show()

chat_id_bot = 735576128

def xxx(x, y):
    y1, sr1 = librosa.load(x)
    y2, sr2 = librosa.load(y)

    plt.subplot(1, 2, 1) 
    mfcc1 = librosa.feature.mfcc(y1,sr1)   #Computing MFCC values
    librosa.display.specshow(mfcc1)


    plt.subplot(1, 2, 2)
    mfcc2 = librosa.feature.mfcc(y2, sr2)
    librosa.display.specshow(mfcc2)

    dist, path = fastdtw (mfcc1.T, mfcc2.T)

    if (dist <= 2500000):
        return True
    else:
        return False


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print xxx('baby_crying_1_mono.wav', 'baby_crying_1_mono.wav') 
    print 'Got command: %s' % command

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))

bot = telepot.Bot('752717879:AAFXx5ds3hatUt3be2HHsWMGvcJzA0-lLZs')


#get distance for kNN
# distance, path = fastdtw(latih.T, uji.T, dist=euclidean)
# print "distance :"
# print distance
