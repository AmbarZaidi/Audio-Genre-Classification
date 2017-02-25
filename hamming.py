from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav
import numpy as np

(rate,sig) = wav.read("english.wav")

window = np.append(np.array([0]),np.hamming(160))
#window.append()

print window
def hm( n ):
	return window[n]

#print hm(5)
#n_farmes = len(sig)/

#print window
#print sig[1:1000]

#while i<len(sig):

mfcc_feat = mfcc(sig,rate ,winlen=0.020,winfunc=hm)
d_mfcc_feat = delta(mfcc_feat, 2)
fbank_feat = logfbank(sig,rate)

print mfcc_feat[1:3]
print "-------------------"
