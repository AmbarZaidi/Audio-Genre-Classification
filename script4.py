from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav
import os 
import numpy as np

directory = "/home/saurabh/AudioClassifier/genres/"

window = np.append(np.array([0]),np.hamming(441))

features_list =[]
class_list = []

def hm( n ):
	return window[n]

def crawler1 ( directory ) :
	for folder in os.listdir(directory) :
		print folder
		crawler2(directory+folder+"/")

def crawler2 ( directory ) : 
	#print directory
	for folder in next(os.walk(directory))[1]:
		print "_",folder
		class_list.append(folder)
		for file in os.listdir(directory+folder) :
			print file,
			
			(rate,sig) = wav.read(directory+folder+"/"+file)
			mfcc_feat = mfcc(sig,rate ,winlen=0.020,winfunc=hm)
			print len(sig),rate,len(mfcc_feat), len(mfcc_feat[0])

			features_list.append(mfcc_feat)



		#os.system(("sox "+directory+filename+" -e signed-integer "+directory+"wav/"+filename[:-3]+".wav"))

if __name__ == "__main__":
	crawler1(directory)
	print len(features_list),len(features_list[0]),len(features_list[0][0])
	print features_list[0]