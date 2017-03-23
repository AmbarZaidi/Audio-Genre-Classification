import math
import numpy as np 

def distance(instance1 , instance2 , k ):
	distance =0 
	mm1 = instance1[0] 
	cm1 = instance1[1]
	mm2 = instance2[0]
	cm2 = instance2[1]
	distance = np.trace(np.dot(np.linalg.inv(cm2), cm1)) 
	distance+=(np.dot(np.dot((mm2-mm1).transpose() , np.linalg.inv(cm2)) , mm2-mm1 )) 
	distance+= np.log(np.linalg.det(cm2)) - np.log(np.linalg.det(cm1))
	distance-= k
	return distance