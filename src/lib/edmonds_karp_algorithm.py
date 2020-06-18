#Edmonds-Karp Algorithm

#find path by using BFS
def ek_bfs(C, F, s, t):
		queue = [s]
		paths = {s:[]}
		if s == t:
			return paths[s]
		while queue: 
			u = queue.pop(0)
			for v in range(len(C)):
					if(C[u][v]-F[u][v]>0) and v not in paths:
						paths[v] = paths[u]+[(u,v)]
						
						if v == t:
							print(paths[v])
							return paths[v]
						queue.append(v)
		return None


def edmonds_karp_max_flow(C, s, t):
	
	n = len(C) 
	F = []

	for i in range(n):
		F.append([0] * n)		
	
	path = ek_bfs(C, F, s, t)
 
	while path != None:

		flow = min(C[u][v] - F[u][v] for u,v in path)

		for u,v in path:
			F[u][v] += flow
			F[v][u] -= flow

		path = ek_bfs(C, F, s, t)

	final_flow = []
	for i in range(n):
		final_flow.append(F[s][i])  			# Find the final total flow by adding flows across all paths

	return (sum(final_flow))