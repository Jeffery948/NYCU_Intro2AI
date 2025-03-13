import csv
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'


def astar(start, end):
    # Begin your code (Part 4)
    #raise NotImplementedError("To be implemented")
    '''
    line 23 ~ 32 : Reads the file into Edges, every start node have a list, inside are end node and distance, and let start
    node, end node to be integer
    line 34 ~ 46 : Reads the file into heuristic_value, every node stores its distance to end node
    line 48 ~ 53 : Prepare for astar, use list to simulate priority queue to store node we want to visit, visited stores node
    have been visited, previous_node stores current node's parent node, dis_to_start stores the distance from current node 
    to start node
    line 54 ~ 81 : Implementation of astar, let non-visited node in queue, until end is visited. In order to simulate priority
    queue, I sort the list by the distance from current node to start plus heuristic value
    line 60 ~ 64 : Calculate path, from end to start to rebuild the path, and start should be taken careful
    (line 63), and reverse the path
    line 71 ~ 79 : Check next node whether in queue and visited already, if it's not in queue and not visited, just add it,
    else update the dis_to_start and previous_node
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

    heuristic_value = {}
    with open(heuristicFile, newline = '') as Heuristic:
        heuristics = csv.reader(Heuristic)
        for heuristic in heuristics:
            if heuristic[0] == 'node':
                continue
            heuristic[0] = int(heuristic[0])
            if end == 1079387396:
                heuristic_value[heuristic[0]] = float(heuristic[1])
            elif end == 1737223506:
                heuristic_value[heuristic[0]] = float(heuristic[2])
            else:
                heuristic_value[heuristic[0]] = float(heuristic[3])

    open_list = [[heuristic_value[start], start]]
    previous_node = {}
    dis_to_start = {}
    visited = set()
    visited.add(start)
    dis_to_start[start] = 0
    while len(open_list) > 0:
        now_node = open_list.pop(0)
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
                if next_node[0] not in open_list:
                    previous_node[next_node[0]] = now_node[1]
                    dis_to_start[next_node[0]] = dis_to_start[now_node[1]] + next_node[1]
                    open_list.append([dis_to_start[next_node[0]] + heuristic_value[next_node[0]], next_node[0]])
            else:
                if dis_to_start[next_node[0]] > dis_to_start[now_node[1]] + next_node[1]:
                    dis_to_start[next_node[0]] = dis_to_start[now_node[1]] + next_node[1]
                    previous_node[next_node[0]] = now_node[1]
            visited.add(next_node[0])
        open_list.sort()
    # End your code (Part 4)


if __name__ == '__main__':
    path, dist, num_visited = astar(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
    path, dist, num_visited = astar(426882161,  1737223506)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
    path, dist, num_visited = astar(1718165260, 8513026827)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
