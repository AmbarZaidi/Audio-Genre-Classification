import operator 
from dist import distance
def getNeighbors(trainingSet , instance , k):
	distances =[]
	for x in range (len(trainingSet)):
		dist = distance(trainingSet[x], instance, k )+ distance(instance, trainingSet[x], k)
		distances.append((trainingSet[x][2], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors	

def nearestClass(neighbors):
	classVote ={}
	for x in range(len(neighbors)):
		response = neighbors[x]
		if response in classVote:
			classVote[response]+=1 
		else:
			classVote[response]=1 
	sorter = sorted(classVote.iteritems(), key = operator.itemgetter(1), reverse=True)
	return sorter[0][0]		
