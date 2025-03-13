import csv
edgeFile = 'edges.csv'


def ucs(start, end):
    # Begin your code (Part 3)
    #raise NotImplementedError("To be implemented")
    '''
    line 21 ~ 30 : Reads the file into Edges, every start node have a list, inside are end node and distance, and let start
    node, end node to be integer
    line 32 ~ 36 : Prepare for ucs, use list to simulate priority queue to store node we want to visit, visited stores node
    have been visited, previous_node stores current node's parent node, dis_to_start stores the distance from current node
    to start node
    line 37 ~ 70 : Implementation of ucs, let non-visited node in queue, until end is visited. In order to simulate priority
    queue, I sort the list by the distance from current node to start
    line 44 ~ 48 : Calculate path, from end to start to rebuild the path, and start should be taken careful
    (line 47), and reverse the path
    line 55 ~ 69 : Check next node whether in queue already, if it's not in queue, just add it, if in queue already, update the
    dis_to_start and previous_node
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

    queue = [[0, start]]
    visited = set()
    previous_node = {}
    dis_to_start = {}
    dis_to_start[start] = 0
    while len(queue) > 0:
        now_node = queue.pop(0)
        visited.add(now_node[1])
        if now_node[1] == end:
            i = end
            path = [end]

            while previous_node[i] != start:
                path.append(previous_node[i])
                i = previous_node[i]
            path.append(start)
            path.reverse()

            return path, dis_to_start[end], len(visited)
        
        if now_node[1] not in Edges:
            continue
        for next_node in Edges[now_node[1]]:
            if next_node[0] not in visited:
                flag = False
                for node in queue:
                    if node[1] == next_node[0]:
                        flag = True
                        if dis_to_start[next_node[0]] > next_node[1] + now_node[0]:
                            dis_to_start[next_node[0]] = next_node[1] + now_node[0]
                            previous_node[next_node[0]] = now_node[1]
                            node[0] = dis_to_start[next_node[0]]
                            break
                if flag:
                    continue
                previous_node[next_node[0]] = now_node[1]
                dis_to_start[next_node[0]] = now_node[0] + next_node[1]
                queue.append([dis_to_start[next_node[0]], next_node[0]])
        queue.sort()
    # End your code (Part 3)


if __name__ == '__main__':
    path, dist, num_visited = ucs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
    path, dist, num_visited = ucs(426882161,  1737223506)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
    path, dist, num_visited = ucs(1718165260, 8513026827)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
