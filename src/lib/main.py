from ford_fulkerson_algorithm import *



def main():
	# make a capacity graph
	# node 0  1  2  3  4  5
	C = [[ 0, 3, 3, 0, 0, 0 ],  # 0
		 [ 0, 0, 2, 3, 0, 0 ],  # 1
		 [ 0, 0, 0, 0, 2, 0 ],  # 2
		 [ 0, 0, 0, 0, 4, 2 ],  # 3
		 [ 0, 0, 0, 0, 0, 2 ],  # 4
		 [ 0, 0, 0, 0, 0, 0 ]]  # 5

	source = 0  # A
	sink = 5    # F
	max_flow_value = max_flow(C, source, sink)
	print ("Ford-Fulkerson algorithm")
	print ("max flow value is: ", max_flow_value)



if __name__ == "__main__":
    main()