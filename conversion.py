import os 

directory = "/home/saurabh/AudioClassifier/genres/"



def crawler ( directory ) : 
	print directory
	os.system("mkdir "+directory+"wav")
	for filename in os.listdir(directory) :
		print filename
		os.system(("sox "+directory+filename+" -e signed-integer "+directory+"wav/"+filename[:-3]+".wav"))

if __name__ == "__main__":
	for folder in os.listdir(directory) :
		print folder
		crawler(directory+folder+"/")