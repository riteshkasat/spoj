import heapq as hp 
import sys

nodes, n = map(int, raw_input().strip().split())
a = {}
d= {}
nextlist = []
result = []

for i in range(1,nodes+1):
	a[i] = []
	d[i] = 0

for i in range(n):
	x = map(int,raw_input().strip().split())
	# print x
	node = x[0]
	neighbours = x[1]
	
	for j in range(neighbours):
		a[x[j+2]].append(node)
		d[node] += 1

for i in d:
	if d[i] == 0:
		hp.heappush(nextlist, i)

while len(nextlist)>0:

	node = hp.heappop(nextlist)
	result.append(node)
	for neighbour in a[node]:
		d[neighbour] = d[neighbour]-1
		if d[neighbour] == 0:
			hp.heappush(nextlist, neighbour)

s = ""
for ele in result:
	s+=str(ele)
	s+=' '



print s.strip()

