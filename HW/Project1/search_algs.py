#!/usr/bin/python3

def BFS(graph, start_node, goal_node):
    explored = list()
    queue = [start_node] #FIFO
    explored.append(start_node)
    path = []
    cost = 0
    while True:
        if not queue:
            return
        node = queue.pop(0)
        path.append(node)
        if node == goal_node:
            return len(path), path, cost
        if node in graph:
            for neighbor in graph[node]:
                if neighbor[0] not in explored:
                    explored.append(neighbor[0])
                    queue.append(neighbor[0])
                    cost = cost + neighbor[1]
    return len(path), path, cost

def DFS(graph, start_node, goal_node):
    explored = []
    queue = [start_node]
    cost = 0
    while True:
        if not queue:
            return
        node = queue[-1]
        if node not in explored:
            explored.append(node)
        if node == goal_node:
            return len(explored), explored, cost
        is_node_explored = True
        for child in graph[node]:
            if child[0] not in explored:
                is_node_explored = False
                queue.append(child[0])
                cost = cost + child[1]
                break
        if is_node_explored:
            queue.pop()
    return len(explored), explored, cost

def IDS(graph, start_node, goal_node, limit):
    depth  = 0
    while depth < limit:
        result = DLS(graph, start_node, goal_node, [], depth, 0)
        if result != 'limit reached':
            return result
        else:
            depth = depth + 1

def DLS(graph, start_node, goal_node, explored, limit, cost):
    if start_node not in explored:
        explored.append(start_node)
    if limit == 0:
        return 'limit reached'
    elif start_node == goal_node:
        return len(explored), explored, cost
    else:
        is_limit = False
        if start_node in graph:
            for child in graph[start_node]:
                if child[0] not in explored:
                    result = DLS(graph, child[0], goal_node, explored, limit - 1, cost + child[1])
                    if result == 'limit reached':
                        is_limit = True
                    elif result is not None:
                        return result
        if is_limit:
            return 'limit reached'
        else:
            return

def UCS(graph, start_node, goal_node):
    visited = []
    queue_node = [start_node]
    queue_cost = [0]
    path = []
    total_nodes = set()
    while True:
        if not queue_node:
            return
        min_cost_idx = queue_cost.index(min(queue_cost))
        cost = queue_cost.pop(min_cost_idx)
        node = queue_node.pop(min_cost_idx)
        # path.append(node)
        # print(queue_node)
        # cost = queue_cost.pop() #just pop or pop(0) or do min and pop?!
        # node = queue_node.pop()
        # path.insert(0, node)
        path.insert(0, node)
        total_nodes.add(node)
        if node not in visited:
            visited.append(node)
        if node == goal_node:
            return len(total_nodes), visited, total_cost
        else:
            for neighbor in graph[node]:
                if neighbor[0] not in visited:
                    queue_node.insert(0, neighbor[0])
                    total_cost = float(cost) + float(neighbor[1])
                    queue_cost.insert(0, total_cost)
                    #path.append(neighbor[0])
                    # path.insert(0, neighbor[0])
                    # path_final = path[0]
                    path.insert(0, node)
    return len(total_nodes), visited, total_cost

def Astar(graph, start_node, goal_node):
    
    # def aSearch(self, heuristic):
        actual = self.start
        leaves = PriorityQueue()
        leaves.put((actual.costHeur(heuristic), actual))
        closed = list()
        while True:
            if leaves.empty():
                return None
            actual = leaves.get()[1]
            if actual.goalState():
                return actual
            elif actual.state.puzzle not in closed:
                closed.append(actual.state.puzzle)
                succ = actual.succ()
                while not succ.empty():
                    child = succ.get()
                    leaves.put((child.costHeur(heuristic)+child.depth, child))
