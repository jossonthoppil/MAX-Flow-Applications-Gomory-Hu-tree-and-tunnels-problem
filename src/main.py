from lib.ford_fulkerson_algorithm import *
from lib.edmonds_karp_algorithm import *
from lib.push_relabel_algorithm import *
from lib.dinic_algorithm import *

from gomory_hu import GomoryHuTree

def main():
	# make a capacity graph
	# node 0  1  2  3  4  5
	C = [[ 0, 3, 3, 0, 0, 0 ],  # 0
		 [ 0, 0, 2, 3, 0, 0 ],  # 1
		 [ 0, 0, 0, 0, 2, 0 ],  # 2
		 [ 0, 0, 0, 0, 4, 2 ],  # 3
		 [ 0, 0, 0, 0, 0, 2 ],  # 4
		 [ 0, 0, 0, 0, 0, 0 ]]  # 5

	source = 0  
	sink = 5    

	max_flow_value = ford_fulkerson_max_flow(C, source, sink)
	print ("Ford-Fulkerson algorithm")
	print ("max flow value is: ", max_flow_value)

	print()
	max_flow_value = edmonds_karp_max_flow(C, source, sink)
	print ("Edmonds-Karp algorithm")
	print ("max flow value is: ", max_flow_value)	

	print()
	max_flow_value = push_relabel_max_flow(C, source, sink)
	print ("Push-Relabel algorithm")
	print ("max flow value is: ", max_flow_value)

	print()
	max_flow_value = dinic_maxflow(C, source, sink)
	print ("Dinic's algorithm")
	print ("max flow value is: ", max_flow_value)

	print()
	print("Constructing the Gomory-Hu tree using Edmond-Karp algorithm")
	tree = GomoryHuTree(C)

	# Print Tree Contents
	print(tree)

	# Query for min cut between 0 and 4
	print(tree.query(2, 0))
	print(tree.query(0, 2))

	# Print the edge (0, 3)
	print(tree[0, 3])


if __name__ == "__main__":
    main()