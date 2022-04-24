
import sys

prev = [[] for x in range(1000)]
post = [[] for x in range(1000)]
clock = 1

def previsit (to_visit): 
    global clock
    prev[to_visit] = clock 
    clock = clock + 1 
    
def postvisit (to_visit): 
    global clock
    post[to_visit] = clock
    clock = clock + 1

def find_path_helper(graph: dict, start, end, cycle, visited: set):
   visited.add(start)
   cycle.append(start)
   
   if start == end: 
       return True
   else: 
       for neighbor in graph[start]: 
           if neighbor not in visited: 
               if find_path_helper(graph, neighbor, end, cycle, visited): 
                   return cycle
   
   cycle.pop()
   visited.remove(start) 
   return False; 

def find_path(graph: dict, start, end): 
   cycle = [] 
   visited = set()
   cycle = find_path_helper(graph, start, end, cycle, visited)
   return cycle
   

def examine_pre_postvisit(graph: dict): 
    ans = []
    for curr in range (len(graph)): 
        for neighbor in graph[curr]:
            if prev[curr] > prev [neighbor] and post[curr] < post[neighbor]: 
                ans.append(find_path(graph, neighbor, curr))
    return ans

def traverse_scc_helper(graph: dict, visited: set, to_visit): 
    visited.add(to_visit)
    previsit(to_visit)
    neighbors = graph[to_visit]
    for neighbor in neighbors: 
        if neighbor not in visited: 
            traverse_scc_helper(graph, visited, neighbor)
    postvisit(to_visit) 

def add_single_component(graph, ans:list): 
    existed = set() 
    for i in range (len(ans)): 
        for neighbor in ans[i]: 
            existed.add(neighbor)
    for i in range (len (graph)): 
        if i not in existed: 
            ans.append([i])

def traverse_scc(graph): 
    visited = set()
    for i in range(len(graph)): 
        if i not in visited: 
            traverse_scc_helper(graph, visited, i)
    ans = examine_pre_postvisit(graph)
    add_single_component(graph, ans)
    return ans

def create_adjacency_list(edges): 
    graph = {}
    temp = []
    for edge in edges: 
        if edge[0] not in graph: 
            temp.append(edge[1])
            graph[edge[0]] = temp.copy()
        elif edge[0] in graph: 
            temp.extend(graph[edge[0]])
            temp.append(edge[1]) 
            graph[edge[0]] = temp.copy()
        temp.clear()
    for edge in edges: 
        if edge[1] not in graph: 
            graph[edge[1]] = temp
    return graph


def combine_list(ans: list):
    tmp_set = set() 
    tmp_list = list() 
    flag = True
    while flag: 
        flag = False 
        for i in range (len(ans) - 1): 
            for j in range (i + 1, len(ans)): 
                tmp_list = ans[i] + ans[j] 
                tmp_set = set(tmp_list) 
                if len (tmp_list) != len(tmp_set): 
                    ans.append(list(tmp_set))
                    ans.pop(j)
                    ans.pop(i) 
                    flag = True 
                    break

if __name__ == '__main__': 
    if len(sys.argv) != 2: 
        print('Usage: python3 Find_SCC.py in.txt')
        quit() 
    file_name = sys.argv[1] 
    f = open(file_name, 'r') 
    lines = f.readlines() 
    edges = list()
    for line in lines: 
       elements = line.split(',')
       edges.append((int(elements[0].strip()), int(elements[1].strip())))
    directed_graph = create_adjacency_list(edges)
    if len(directed_graph) >= 1: 
        ans = traverse_scc(directed_graph) 
    ans = sorted(ans, key=lambda x: x[0])
    combine_list(ans)
    ans = sorted(ans, key=lambda x: x[0])
    for i in range(len(ans)):
        ans[i] = sorted(ans[i]) 
    print(len(ans), 'Strongly Connected Component(s):') 
    for i in range (len(ans)): 
        str_ans = [str(a) for a in ans[i]]
        print(', '.join(str_ans))

      