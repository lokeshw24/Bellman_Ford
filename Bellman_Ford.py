#!/bin/python

class Node :
	name=None
	key=None
	neighbours=[]

	def __init__(self, name, neighbours):
		self.name=name
		self.neighbours=neighbours


	def display_neighbours(self):
		print "(",self.name ,")-->"
		for i in self.neighbours : 
			print i;

class Graph :
	All_Nodes=[]
	Edge_Weights={}
	Neighbours={}
	Key_Values={}

	def add_node( self, node, neighbours ):
		n = Node( node, neighbours)
		self.All_Nodes.append(n)

	def print_nodes(self):
		for nodes in self.All_Nodes :
			nodes.display_neighbours()

	def assign_edge_weights(self, node1, node2, edge_weight):
		edge_name=node1+'-'+node2
		self.Edge_Weights[edge_name]=edge_weight

	def get_all_neighbours(self) :
		#this method is used to get the info of nodes in local data-structures, because they are frequently required.
		for nodes in self.All_Nodes :
			self.Neighbours[nodes.name]=nodes.neighbours
			self.Key_Values[nodes.name]=nodes.key

	def get_neighbours(self, node_name) :
		for nodes in self.All_Nodes :
			if( nodes.name==node_name ) :
				neighbours=nodes.neighbours

		return neighbours

	def Bellman_Ford(self, start_node ):
		def relax_edge(source_node, target_node):
			edge_name=source_node+'-'+target_node
			if ( not( edge_name in self.Edge_Weights ) ):
				print "I m not reached only ! "
				edge_name=target_node+'-'+source_node

			if( self.Key_Values[source_node]+self.Edge_Weights[edge_name] < self.Key_Values[target_node] ) :
				self.Key_Values[target_node]=self.Key_Values[source_node]+self.Edge_Weights[edge_name]
				Parents[target_node]=source_node
				return 1
			return 0

		def check_for_negative_cycles():
			for node in self.Neighbours :
				get_all_neighbours=self.Neighbours[node]

				for neigh in get_all_neighbours :
					edge_name=node+'-'+neigh
					if( self.Key_Values[node]+self.Edge_Weights[edge_name] < self.Key_Values[neigh] ) :
						print "Negative Cycle Exists in Graph.....ABORTING !"
						exit()


		def print_shortest_path(dest_node):
			if ( Parents[dest_node]==None ):
				print dest_node
				return

			print_shortest_path(Parents[dest_node] )
			print dest_node

	# ----------------------------------------------------------------------------

		Parents={}
		Parents[start_node]=None

		self.get_all_neighbours();

		#initialize the key values of every node
		for nodes in self.Key_Values :
			self.Key_Values[nodes]=9999999 #as infinity

		self.Key_Values[start_node]=0


		all_nodes=[]
		for nodes in self.Neighbours :
			all_nodes.append(nodes);
		to_be_relaxed_nodes=[];
		to_be_relaxed_nodes.append(start_node);
	
		while(all_nodes) :	
			current_node=to_be_relaxed_nodes.pop()
			all_nodes.remove(current_node)

			neighbours_of_current_node=self.Neighbours[current_node]

			for neigh_node in neighbours_of_current_node :
				#now relax every edge of the current_node
				if( relax_edge(current_node, neigh_node) ):
					#add in stack
					to_be_relaxed_nodes.append(neigh_node)

		#if any -ve cycles exist in the graph, abort the program
		check_for_negative_cycles()

		#print self.Key_Values, "\n", Parents
		print "Shortest Paths with starting node (" + start_node + ") are : "
		for nodes in self.Key_Values :
			print self.Key_Values[nodes]
			print_shortest_path(nodes)
			print "----"

def init_graph(my_graph) :
	my_graph.add_node('s', ['t','y'])
	my_graph.add_node('t', ['x'])
	my_graph.add_node('x', ['t'])
	my_graph.add_node('y', ['x','z'])
	my_graph.add_node('z', ['x'])
	
	my_graph.assign_edge_weights('s', 't', 5)
	my_graph.assign_edge_weights('s', 'y', 1)
	my_graph.assign_edge_weights('t', 'x', 1)
	my_graph.assign_edge_weights('x', 't', 1)
	my_graph.assign_edge_weights('y', 'x', 2)
	my_graph.assign_edge_weights('y', 'z', 1)
	my_graph.assign_edge_weights('z', 'x', 1)

def main():
	my_graph = Graph()

	#this should be my_graph.init(), as per OOP concept.
	init_graph(my_graph)
	#my_graph.print_nodes()
	
	#Starting the algorithm with 's' as the root
	my_graph.Bellman_Ford('s');

main()
