# accuracy.py

def getAccuracy(testSet, predictions):
	correct = 0 
	for x in range (len(testSet)):
		if testSet[x][-1]==predictions[x]:
			correct+=1
	return 1.0*correct/len(testSet)		