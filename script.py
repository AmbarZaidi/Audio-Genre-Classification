from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav

(rate,sig) = wav.read("english.wav")

print len(sig)
mfcc_feat = mfcc(sig,rate ,winlen=0.020)
d_mfcc_feat = delta(mfcc_feat, 2)
fbank_feat = logfbank(sig,rate)

print len(mfcc_feat)
# print(fbank_feat[1:5,:])
