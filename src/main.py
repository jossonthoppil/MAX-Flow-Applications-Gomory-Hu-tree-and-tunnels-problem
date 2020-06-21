from lib.ford_fulkerson_algorithm import *
from lib.edmonds_karp_algorithm import *
from lib.push_relabel_algorithm import *
from lib.dinic_algorithm import *

from gomory_hu import GomoryHuTree
from tunnels import *

def main():
	# make a capacity graph
	# node 0  1  2  3  4  5

	print("------------------------------------------------------------------------------------------")
	print("Hello, and welcome")
	print("Enter the option to execute the option you want")
	print("1 - Test various implementations of Max-Flow algorithms")
	print("2 - Test the Gomory-Hu Data Structure, built on the Edmonds-Karp Algorithm for Max-Flow ")
	print("3 - Application of Max Flow: Analysis of escape routes in an underground tunnel network and determining most efficient way to prevent escape")
	print("4 - Exit")
	option = int(input())
	while(option in [1, 2, 3]):

		if(option in [1, 2]):
			# C = [[ 0, 3, 3, 0, 0, 0 ],  # 0
			# 	 [ 0, 0, 2, 3, 0, 0 ],  # 1
			# 	 [ 0, 0, 0, 0, 2, 0 ],  # 2
			# 	 [ 0, 0, 0, 0, 4, 2 ],  # 3
			# 	 [ 0, 0, 0, 0, 0, 2 ],  # 4
			# 	 [ 0, 0, 0, 0, 0, 0 ]]  # 5

			C = [[ 0 , 10, 0, 0, 0, 8 ],  # 0
				 [ 10, 0 , 4, 0, 2, 3 ],  # 1
				 [ 0,  4,  0, 5, 4, 2 ],  # 2
				 [ 0,  0,  5, 0, 7, 2 ],  # 3
				 [ 0,  2,  4, 7, 0, 3 ],  # 4
				 [ 8,  3,  2, 2, 3, 0 ]]  # 5

			source = 0  
			sink = 5 

		if (option == 1):
			print("	--------------------------------------------------------------------------------")
			print("	Enter the algorithm option to test it's implementation")
			print("	1 - Ford-Fulkerson Algorithm ")
			print("	2 - Edmonds-Karp Algorithm")
			print("	3 - Dinic's Algorithm")
			print("	4 - Push-Relabel Algorithm") 

			algorithm = int(input("	"))

			if(algorithm in [1, 2, 3, 4, 5]):

				if(algorithm == 1):  

					print()
					max_flow_value = ford_fulkerson_max_flow(C, source, sink)
					print ("	Ford-Fulkerson algorithm")
					print ("	max flow value is: ", max_flow_value)
					print()

				elif(algorithm == 2):

					print()
					max_flow_value = edmonds_karp_max_flow(C, source, sink)
					print ("	Edmonds-Karp algorithm")
					print ("	max flow value is: ", max_flow_value)
					print()

				elif(algorithm == 3):	

					print()
					max_flow_value = dinic_maxflow(C, source, sink)
					print ("	Dinic's algorithm")
					print ("	max flow value is: ", max_flow_value)
					print()

				else:
					print()
					max_flow_value = push_relabel_max_flow(C, source, sink)
					print ("	Push-Relabel algorithm")
					print ("	max flow value is: ", max_flow_value)
					print()

			else:
				print("		Invalid option, please try again")

		elif (option == 2):

			print()
			#print("	Constructing the Gomory-Hu tree using Edmond-Karp algorithm")
			tree = GomoryHuTree(C)

			print()
				
			#print(gomory_tree)

			print("	Gomory-Hu Tree constructed. Ready to handle queries")
			print()
			tree = GomoryHuTree(C)

			print()


			# Print Tree Contents
			gomory_tree = []
			for node in tree.tree:
				
				if(tree.tree[node] > 0):
					print("	", node, tree.tree[node])	
			print()
			# Query for min cut between 0 and 4
			print("        Enter the 2 vertices to query for the minimum cut")
			print()

			print("        Enter the vertex 1 - ", end = " ")
			v1 = int(input())
			print()
			print("        Enter the vertex 2 - ", end = " ")
			v2 = int(input())
			#print("        The Max-Flow minimum-cut between them is")
			print("	The maximum flow between the 2 vertices is - ", tree.query(v1, v2))
			#print("       ", tree.query(v2, v1))

		elif (option == 3):
			result = tunnels()
			print("\n\n\n\t\t\tThe answer for the minimum number of tunnels to collapse is : " + str(result))
		
		print()
		print("------------------------------------------------------------------------------------------")
		print("Enter the option to execute the option you want")
		print("1 - Test various implementations of Max-Flow algorithms")
		print("2 - Test the Gomory-Hu Data Structure, built on the Edmonds-Karp Algorithm for Max-Flow ")
		print("3 - Application of Max Flow: Analysis of escape routes in an underground tunnel network and determining most efficient way to prevent escape")
		print("4 - Exit")
		option = int(input())


if __name__ == "__main__":
    main()