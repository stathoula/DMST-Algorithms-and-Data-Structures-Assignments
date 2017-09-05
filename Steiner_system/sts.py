import random
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("number", help="number of dimitraka", type=int)
args = parser.parse_args()

numberOfEntries = args.number
blocks = []

#This is a dictionary which shows how many times a number x appear in the blocks
numOfAppearance = {}
for i in range(1,numberOfEntries+1):
	numOfAppearance[i] = 0

CD = numberOfEntries * (numberOfEntries - 1) / 6
CD2 = CD
maxAppearance = (numberOfEntries-1)/2
#With this def we pick the x
def getx(numOfAppearance):	
	while True:
		x = random.randint(1,numberOfEntries)
		if  numOfAppearance[x] < maxAppearance:
			break
	return x
#with this method we find all the numbers that x makes couple with
def getlistwithx(x,blocks):	
	list = []
	for triada in blocks:
		if x in triada:
			for y in triada:
				if y != x:
					list.append(y)
	return list
	
#################Solution#########
while CD > 0:
	x = getx(numOfAppearance)
	listOfx = getlistwithx(x,blocks)
	
	while True:
		y = random.randint(1,numberOfEntries)
		if y not in listOfx and y != x:
			break
	
	while True:
		z = random.randint(1,numberOfEntries)
		if z not in listOfx and z != x and z!=y:
			break

	for triada in blocks:			
		if y in triada and z in triada:
			blocks.remove(triada)
			for n in triada:
				numOfAppearance[n] = numOfAppearance[n] - 1
			CD = CD + 1
			break
	
	tempTriada = [x,y,z]
	tempTriada.sort()
	tempTriada = tuple(tempTriada)
	blocks.append(tempTriada)
	for n in tempTriada:
		numOfAppearance[n] = numOfAppearance[n] + 1
	CD = CD - 1

blocks.sort()		
print(blocks)
print("%d" % CD2)
		


