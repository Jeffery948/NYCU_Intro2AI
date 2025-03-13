import csv
edgeFile = 'edges.csv'


def dfs(start, end):
    # Begin your code (Part 2)
    #raise NotImplementedError("To be implemented")
    '''
    line 17 ~ 26 : Reads the file into Edges, every start node have a list, inside are end node and distance, and let start
    node, end node to be integer
    line 28 ~ 31 : Prepare for dfs, use list to simulate stack to store node we want to visit, visited stores node have been
    visited, previous_node stores current node's parent node and the distance to parent node
    line 32 ~ 54 : Implementation of dfs, let non-visited node in stack, until end is visited
    line 44 ~ 50 : Calculate path and distance, from end to start to rebuild the path, and start should be taken careful
    (line 48 ~ 49), and reverse the path
    '''
    Edges = {}
    with open(edgeFile, newline = '') as Edgefile:
        edges = csv.reader(Edgefile)
        for edge in edges:
            if edge[0] == 'start':
                continue
            edge[0], edge[1] = int(edge[0]), int(edge[1])
            if edge[0] not in Edges:
                Edges[edge[0]] = []
            Edges[edge[0]].append([edge[1], float(edge[2])])

    stack = [start]
    visited = set()
    visited.add(start)
    previous_node = {}
    while len(stack) > 0:
        now_node = stack.pop()
        if now_node not in Edges:
            continue
        for next_node in Edges[now_node]:
            if next_node[0] not in visited:
                previous_node[next_node[0]] = [now_node, next_node[1]]
                if next_node[0] == end:
                    i = end
                    path = [end]
                    dis = 0.0

                    while previous_node[i][0] != start:
                        dis += previous_node[i][1]
                        path.append(previous_node[i][0])
                        i = previous_node[i][0]
                    dis += previous_node[i][1]
                    path.append(start)
                    path.reverse()
                        
                    return path, dis, len(visited)
                visited.add(next_node[0])
                stack.append(next_node[0])
    # End your code (Part 2)


if __name__ == '__main__':
    path, dist, num_visited = dfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
    path, dist, num_visited = dfs(426882161,  1737223506)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
    path, dist, num_visited = dfs(1718165260, 8513026827)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
