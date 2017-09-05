import pprint
import argparse
import math
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--numberOfGroups", help="Number of groups", type = int)
parser.add_argument("filename", help="name of input file")
args = parser.parse_args()

if args.numberOfGroups:
	ngroups = args.numberOfGroups
else:
	ngroups = 2

graph = {}
with open(args.filename) as file:
	for line in file:
		line = line.rstrip()
		line = line.split(' ')
		node1 = int(line[0])
		node2 = int(line[1])
		if node1 not in graph:
			graph[node1] = []
		if node2 not in graph:
			graph[node2] = []
		graph[node1].append(node2)	
		graph[node2].append(node1)	
#pprint.pprint(graph)
	
#with this method we find the possible combinations that a group can have with the other groups
def findCombinations(defGroup,groups):
	combinations = []
	for group in groups:	
		flag = False
		if defGroup != group:
			for x in defGroup:
				for y in graph[x]:
					if y in group:
						tempcomb = [defGroup] + [group]
						tempcomb.sort()
						combinations.append(tempcomb)
						flag = True
						break					
				if flag == True:
					break
	return combinations 
	
#def for finding the a
def find_a(nodes):
	suma = 0
	for node in nodes:
		for v in graph[node]:
			suma +=1
	return suma
	
#def for finding the eij
def find_eij(nodes):
	sum = 0
	for x in nodes[0]:	
		for y in graph[x]:
			if y in nodes[1]:
				sum +=1			
	return sum

#we now find the denominator of the ai and eij
n =  0
for k,v in graph.items():
	for v in graph[k]:
		n +=1
		
#we now find the Qo
Q = 0
for k,v in graph.items():
	tempq = 0
	for v in graph[k]:
		tempq+=1
	Q = Q +(tempq/n)* (tempq/n)	
Q = -Q

groups = [[v] for v in graph.keys()]
number_of_groups = len(groups)

################Solution############
while ngroups != number_of_groups:	
	#we find the possible combinations that we are gonna test
	finalComb = []
	for i in groups:
		zeugari = findCombinations(i,groups)
		finalComb += zeugari
    #we erase the duplicate items from the list
	finalComb = sorted(finalComb)
	finalComb = [finalComb[i] for i in range(len(finalComb)) if i == 0 or finalComb[i] != finalComb[i-1]]

	#we now find the maxDQ 
	dq_of_combs=[]
	max = -100000000000
	for comb in finalComb:
		eij = find_eij(comb) / n 
		ai = find_a(comb[0]) / n
		aj = find_a(comb[1]) / n
		dq = 2 * (eij - ai * aj)
		dq_of_combs.append(dq)	
		if dq > max:
			max = dq	
			maxComb = comb
		
	new_team = maxComb[0] + maxComb[1]
	new_team.sort()
	groups.append(new_team) 
	groups.remove(maxComb[1])
	groups.remove(maxComb[0])
	Q = Q + max
			
	number_of_groups = len(groups)	

groups.sort()
#print the solution
for group in groups:
	print(group)
print("Q = " + "%.4f" % Q)


