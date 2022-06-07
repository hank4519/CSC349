

from re import sub
import sys
import random
import itertools

def get_degrees(graph): 
    degrees = dict() 
    for i in range(len(graph)): 
        node1 = graph[i][0] 
        node2 = graph[i][1]
        if node1 not in degrees: 
            degrees[node1] = 1 
        else: 
            degrees[node1] = degrees[node1] + 1 
        if node2 not in degrees: 
            degrees[node2] = 1 
        else: 
            degrees[node2] = degrees[node2] + 1
    return degrees 

def find_max_degree(degrees): 
    max_count = 0 
    max_count_node = int()
    for node, counts in  degrees.items(): 
        if counts > max_count: 
            max_count_node = node 
            max_count = counts
    return max_count_node, max_count 

def remove_edges_start_with_node(graph, node): 
    for edge in list(graph): 
        if edge[0] == node or edge[1] == node: 
            graph.remove(edge)
    

def smart_greedy_vertex_cover(graph, vertex_degrees): 
    C = [] 
    while len(graph) > 0: 
        node, counts = find_max_degree(vertex_degrees) 
        remove_edges_start_with_node(graph, node) 
        vertex_degrees = get_degrees(graph) 
        C.append(node)
    return C  

def basic_greedy_vertex_cover(graph): 
    C = []
    while len(graph) > 0:
        random_choosing = random.randint(0, len(graph) - 1)
        node1, node2 = graph[random_choosing] 
        remove_edges_start_with_node(graph, node1) 
        remove_edges_start_with_node(graph, node2) 
        C.append(node1)
        C.append(node2) 
    return C

def exact_vertex_cover(graph3, all_vertices): 
    copied_graph = list()
    ans = [] 
    for L in range(1, len(all_vertices) + 1): 
        for subset in itertools.combinations(all_vertices, L):
            copied_graph = list(graph3) 
            for node in subset: 
                remove_edges_start_with_node(copied_graph, node) 
            if len(copied_graph) == 0: 
                ans = list(subset)
                break 
        if len(ans) != 0: 
            break
    return ans


if __name__ == "__main__":
    # f = open('in1.txt', 'r') 
    if len(sys.argv) != 2: 
        quit() 
    f = open(sys.argv[1], 'r')
    lines = f.readlines() 
    graph = list() 
    for line in lines: 
        line = line.strip() 
        components = line.split(' ') 
        graph.append([int(components[0]), int(components[1])])
    graph1 = list(graph)
    vertex_degrees = get_degrees(graph1)
    covers1 = smart_greedy_vertex_cover(graph1, vertex_degrees) 
    # print(covers1)

    graph2 = list(graph) 
    covers2 = basic_greedy_vertex_cover(graph2)
    # print(covers2)

    graph3 = list(graph) 
    all_vertices = set() 
    for vertex1, vertex2 in graph3: 
        all_vertices.add(vertex1)
        all_vertices.add(vertex2) 
    covers3 = exact_vertex_cover(graph3, all_vertices)
    # print(covers3)

    print("log-Approximation: %s" % ' '.join([str(v) for v in covers1]))
    print("2-Approximation: %s" % ' '.join([str(v) for v in covers2]))
    print("Exact Solution: %s" % ' '.join([str(v) for v in covers3]))



    