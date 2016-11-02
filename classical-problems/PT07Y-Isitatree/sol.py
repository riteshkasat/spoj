import sys
def dfs(n, g, visted, parent):
	visited[n] = True

	for node in graph[n]:
		if visited[node] == True and parent[n]!=node:
			return False

		elif visited[node] == True and parent[n] == node:
			continue	

		else:
			parent[node] = n
			dfs (node, g, visited, parent)

	return True

n,m = map(int, raw_input().strip().split())
graph = {}
visited = {}
parent = {}
for i in range(1,n+1):
	graph[i] = []
	parent[i] = None
	visited[i] = False

for i in range(m):
	p,q = map(int, raw_input().strip().split())
	graph[p].append(q)
	graph[q].append(p)


count  = 0
for node in graph:
	if visited[node] == False:
		count+=1
		result = dfs(node, graph, visited, parent)

	if result == False or count>1:
		print "NO"
		sys.exit(0)



print "YES"

