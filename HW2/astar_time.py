import csv
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'


def astar_time(start, end):
    # Begin your code (Part 6)
    #raise NotImplementedError("To be implemented")
    '''
    line 26 ~ 37 : Reads the file into Edges, every start node have a list, inside are end node and time to next node, and 
    let start node, end node to be integer, and store the maximum speed of all speed
    line 39 ~ 53 : Reads the file into heuristic_value, every node stores (its distance to end node / maximum speed) to be
    the new heuristic value. Because its direct distance to end node must less than the distance through edges, and its speed
    must less than maximum speed. Time = distance / speed, so this is an admissible heuristic function because it doesn't
    overestimate the cost of the minimum cost path from a node to the end node.
    line 55 ~ 60 : Prepare for astar, use list to simulate priority queue to store node we want to visit, visited stores node
    have been visited, previous_node stores current node's parent node, time_to_start stores the time from current node 
    to start node
    line 61 ~ 88 : Implementation of astar, let non-visited node in queue, until end is visited. In order to simulate priority
    queue, I sort the list by the time from current node to start plus heuristic value
    line 67 ~ 71 : Calculate path, from end to start to rebuild the path, and start should be taken careful
    (line 70), and reverse the path
    line 78 ~ 86 : Check next node whether in queue and visited already, if it's not in queue and not visited, just add it,
    else update the time_to_start and previous_node
    '''
    Edges = {}
    max_speed = 0
    with open(edgeFile, newline = '') as Edgefile:
        edges = csv.reader(Edgefile)
        for edge in edges:
            if edge[0] == 'start':
                continue
            edge[0], edge[1] = int(edge[0]), int(edge[1])
            if edge[0] not in Edges:
                Edges[edge[0]] = []
            Edges[edge[0]].append([edge[1], float(edge[2]) / (float(edge[3]) * 5 / 18)])
            max_speed = max(max_speed, float(edge[3]) * 5 / 18)

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
            
            heuristic_value[heuristic[0]] /= max_speed

    open_list = [[heuristic_value[start], start]]
    previous_node = {}
    time_to_start = {}
    visited = set()
    visited.add(start)
    time_to_start[start] = 0
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

            return path, time_to_start[end], len(visited)
        
        if now_node[1] not in Edges:
            continue
        for next_node in Edges[now_node[1]]:
            if next_node[0] not in visited:
                if next_node[0] not in open_list:
                    previous_node[next_node[0]] = now_node[1]
                    time_to_start[next_node[0]] = time_to_start[now_node[1]] + next_node[1]
                    open_list.append([time_to_start[next_node[0]] + heuristic_value[next_node[0]], next_node[0]])
            else:
                if time_to_start[next_node[0]] > time_to_start[now_node[1]] + next_node[1]:
                    time_to_start[next_node[0]] = time_to_start[now_node[1]] + next_node[1]
                    previous_node[next_node[0]] = now_node[1]
            visited.add(next_node[0])
        open_list.sort()
    # End your code (Part 6)


if __name__ == '__main__':
    path, time, num_visited = astar_time(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total second of path: {time}')
    print(f'The number of visited nodes: {num_visited}')
    path, time, num_visited = astar_time(426882161,  1737223506)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total second of path: {time}')
    print(f'The number of visited nodes: {num_visited}')
    path, time, num_visited = astar_time(1718165260, 8513026827)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total second of path: {time}')
    print(f'The number of visited nodes: {num_visited}')
