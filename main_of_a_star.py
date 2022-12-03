from graph import Graph, Node
from a_star_final import AStar
# from a_star_hope_lkher import AStar

def run():
    # Create graph
    graph = Graph()
    # Add vertices
    graph.add_node(Node('S', (1,1)))
    graph.add_node(Node('B', (1,2)))
    graph.add_node(Node('C', (1,4)))
    graph.add_node(Node('D', (2,1)))
    graph.add_node(Node('E', (2,2)))
    graph.add_node(Node('F', (2,3)))
    graph.add_node(Node('G', (2,4)))
    graph.add_node(Node('H', (3,1)))
    graph.add_node(Node('I', (3,4)))
    graph.add_node(Node('J', (4,1)))
    graph.add_node(Node('K', (4,2)))
    graph.add_node(Node('T', (4,3)))
    graph.add_node(Node('L', (4,4)))
    
    # Add edges
    graph.add_edge('S', 'B', 1)
    graph.add_edge('S', 'D', 1)
    graph.add_edge('B', 'E', 1)
    graph.add_edge('C', 'G', 1)
    graph.add_edge('D', 'E', 1)
    graph.add_edge('D', 'H', 1)
    graph.add_edge('E', 'F', 1)
    graph.add_edge('F', 'G', 1)
    graph.add_edge('G', 'I', 1)
    graph.add_edge('H', 'J', 1)
    graph.add_edge('I', 'L', 1)
    graph.add_edge('J', 'K', 1)
    graph.add_edge('K', 'T', 1)
    graph.add_edge('T', 'L', 1)


    # # Add vertices
    # graph.add_node(Node('A', (3,1)))
    # graph.add_node(Node('B', (2,1)))
    # graph.add_node(Node('D', (4,1)))    
    # graph.add_node(Node('I', (1,1)))
    # graph.add_node(Node('J', (2,2)))
    # graph.add_node(Node('K', (1,2)))
    # graph.add_node(Node('L', (1,3)))
    # graph.add_node(Node('M', (2,3)))
    # graph.add_node(Node('N', (3,3)))
    # graph.add_node(Node('O', (2,4)))
    # graph.add_node(Node('P', (1,4)))
    # graph.add_node(Node('Q', (3,4)))
    # graph.add_node(Node('R', (4,4)))
    # graph.add_node(Node('S', (5,4)))
    # graph.add_node(Node('T', (6,4)))
    # graph.add_node(Node('U', (4,3)))
    # graph.add_node(Node('V', (5,3)))
    # graph.add_node(Node('W', (6,3)))
    # graph.add_node(Node('X', (5,2)))
    # graph.add_node(Node('Y', (6,2)))
    # graph.add_node(Node('Z', (6,1)))
    

    # graph.add_edge('A', 'D', 1)
    # graph.add_edge('A', 'B', 1)
    # graph.add_edge('B', 'I', 1)
    # graph.add_edge('B', 'J', 1)
    # graph.add_edge('J', 'K', 1)
    # graph.add_edge('J', 'M', 1)
    # graph.add_edge('I', 'K', 1)
    # graph.add_edge('L', 'M', 1)
    # graph.add_edge('K', 'L', 1)
    # graph.add_edge('L', 'P', 1)
    # graph.add_edge('M', 'O', 1)
    # graph.add_edge('M', 'N', 1)
    # graph.add_edge('N', 'Q', 1)
    # graph.add_edge('O', 'Q', 1)
    # graph.add_edge('P', 'O', 1)    
    # graph.add_edge('Q', 'R', 1)
    # graph.add_edge('N', 'U', 1)
    # graph.add_edge('U', 'R', 1)
    # graph.add_edge('U', 'V', 1)
    # graph.add_edge('R', 'S', 1)
    # graph.add_edge('V', 'S', 1)
    # graph.add_edge('V', 'W', 1)
    # graph.add_edge('S', 'T', 1)
    # graph.add_edge('W', 'T', 1)
    # graph.add_edge('X', 'V', 1)    
    # graph.add_edge('X', 'Y', 1)
    # graph.add_edge('Y', 'W', 1)
    # graph.add_edge('A', 'D', 1)
    # graph.add_edge('Y', 'Z', 1)





    # Execute the algorithm
    alg = AStar(graph, "S", "T", 4 )
    # alg = AStar(graph, "A", "Z", 3)

    # path, path_length, list1, opened, closed= alg.search()
    
    # print(" -> ".join(path))
    # print(f"Length of the path: {path_length}")
    # print(f"closed list sorted according to h deccesente : {list1}")
    # print(f"opened list: {opened}")
    # print(f"closed list: {closed}")
    # print(f"opened list: {close_by_h}")
    
    path, path_length = alg.search()
    
    print(" ================= iteration ================= ")
    print(" -> ".join(path))
    print(f"Length of the path: {path_length}")
    # print(f"closed list: {closed }")
    # print(f"opened list: {opened }")
      

    #   iteration = 0
    # while True:
    #   iteration + 1
    #   if path[-1] == "T": 
    #     return True




    

    
if __name__ == '__main__':
  run()

# S -> D -> H -> J -> K -> T
# Length of the path: 17