import csv
edgeFile = 'edges.csv'


def bfs(start, end):
    # Begin your code (Part 1)
    #raise NotImplementedError("To be implemented")
    '''
    line 17 ~ 26 : Reads the file into Edges, every start node have a list, inside are end node and distance, and let start
    node, end node to be integer
    line 28 ~ 31 : Prepare for bfs, use list to simulate queue to store node we want to visit, visited stores node have been
    visited, previous_node stores current node's parent node and the distance to parent node
    line 32 ~ 54 : Implementation of bfs, let non-visited node in queue, until end is visited
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

    queue = [start]
    visited = set()
    visited.add(start)
    previous_node = {}
    while len(queue) > 0:
        now_node = queue.pop(0)
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
                queue.append(next_node[0])
    # End your code (Part 1)


if __name__ == '__main__':
    path, dist, num_visited = bfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
    path, dist, num_visited = bfs(426882161,  1737223506)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
    path, dist, num_visited = bfs(1718165260, 8513026827)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
