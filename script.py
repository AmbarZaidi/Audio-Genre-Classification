from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank , fbank
import scipy.io.wavfile as wav
import numpy as np
from tempfile import TemporaryFile
import os
import pickle
import random 
from neighbors import getNeighbors , nearestClass
from accuracy import getAccuracy

directory = "/home/saurabh/AudioClassifier/genres/"
f= open("my.dat" ,'w')
i=0


for folder in os.listdir(directory):
	i+=1
	if i==11 :
		break 	
	for file in os.listdir(directory+folder+"/wav/"):	
		(rate,sig) = wav.read(directory+folder+"/wav/"+file)
		mfcc_feat = mfcc(sig,rate ,winlen=0.020, appendEnergy = False)
		covariance = np.cov(np.matrix.transpose(mfcc_feat))
		mean_matrix = mfcc_feat.mean(0)
		feature = (mean_matrix , covariance , i)
		pickle.dump(feature , f)



f.close()
dataset = []
def loadDataset(filename , split , trSet , teSet):
	with open("my.dat" , 'r') as f:
		while True:
			try:
				dataset.append(pickle.load(f))
			except EOFError:
				f.close()
				break	
	
	for x in range(len(dataset)):
		if random.random() <split :			
			trSet.append(dataset[x])
		else:
			teSet.append(dataset[x])	
						
			
# print len(dataset)
trainingSet = []
testSet = []
loadDataset("my.dat" , 0.66, trainingSet, testSet)

# # print "yes"
# for x in range(len(trainingSet)):
# 	print trainingSet[x][2]

# print "hello"

# for x in range(len(testSet)):
# 	print testSet[x][2]

# print testSet[25][2]


leng = len(testSet)
predictions = []
for x in range (leng):
	predictions.append(nearestClass(getNeighbors(trainingSet ,testSet[x] , 5))) 

print "accuracy"
accuracy1 = getAccuracy(testSet , predictions)
print accuracy1
