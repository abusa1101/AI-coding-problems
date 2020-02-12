#!/usr/bin/python3

def bf_search(graph, start_node, goal_node):
    explored = list()
    queue = [start_node] #FIFO
    explored.append(start_node)
    path = []
    cost = 0
    while True:
        if not queue:
            return 'failure'
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

def df_search(graph, start_node, goal_node):
    explored = []
    queue = [start_node]
    cost = 0
    while True:
        if not queue:
            return 'failure'
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

def id_search(graph, start_node, goal_node, limit):
    depth = 0
    while depth < limit:
        result = dl_search(graph, start_node, goal_node, [], depth, 0)
        if result != 'limit reached':
            return result
        else:
            depth = depth + 1

def dl_search(graph, start_node, goal_node, explored, limit, cost):
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
                    result = dl_search(graph, child[0], goal_node,
                                       explored, limit - 1, cost + child[1])
                    if result == 'limit reached':
                        is_limit = True
                    elif result is not None:
                        return result
        if is_limit:
            return 'limit reached'
        else:
            return

def uc_search(graph, start_node, goal_node):
    visited = []
    queue_node = [start_node]
    queue_cost = []
    path = []
    total_cost = 0
    is_init = True
    while True:
        # print(queue_node)
        # print(queue_cost)
        if not queue_node:
            return 'failure'
        # if goal_node in queue_node:
        #     return len(path), path, total_cost
        if is_init:
            cost = 0
            node = queue_node.pop(0)
            is_init = False
        else:
            min_cost_idx = queue_cost.index(min(queue_cost))
            cost = queue_cost.pop(min_cost_idx)
            node = queue_node.pop(min_cost_idx)
        path.append(node)
        total_cost = total_cost + cost
        if node not in visited:
            visited.append(node)
        if node == goal_node:
            return len(path), path, total_cost
        for neighbor in graph[node]:
            if neighbor[0] not in visited and neighbor[0] not in queue_node:
                queue_node.insert(0, neighbor[0])
                queue_cost.insert(0, neighbor[1])
            elif neighbor[0] in queue_node:
                child_idx = queue_node.index(neighbor[0])
                # print(cost)
                # print(neighbor[1])
                # print()
                if float(cost) < float(neighbor[1]):
                    queue_cost.pop(child_idx)
                    queue_node.pop(child_idx)
                    queue_cost.insert(child_idx, neighbor[1])
                    queue_node.insert(child_idx, neighbor[0])
    return len(path), path, total_cost

def a_star(graph, start_node, goal_node):
    visited = []
    queue_node = [start_node]
    queue_cost = []
    path = []
    total_cost = 0
    total_nodes = set()
    is_init = True
    while True:
        # print(queue_node)
        # print(queue_cost)
        if not queue_node:
            return 'failure'
        # if goal_node in queue_node:
        #     return len(path), path, total_cost
        if is_init:
            cost = 0
            node = queue_node.pop(0)
            is_init = False
        else:
            min_cost_idx = queue_cost.index(min(queue_cost))
            cost = queue_cost.pop(min_cost_idx)
            node = queue_node.pop(min_cost_idx)
        path.append(node)
        total_cost = total_cost + cost
        if node not in visited:
            visited.append(node)
        if node == goal_node:
            return len(path), path, total_cost
        for neighbor in graph[node]:
            if neighbor[0] not in visited and neighbor[0] not in queue_node:
                queue_node.insert(0, neighbor[0])
                queue_cost.insert(0, neighbor[1])
            elif neighbor[0] in queue_node:
                child_idx = queue_node.index(neighbor[0])
                # print(cost)
                # print(neighbor[1])
                # print()
                if float(cost) < float(neighbor[1]):
                    queue_cost.pop(child_idx)
                    queue_node.pop(child_idx)
                    queue_cost.insert(child_idx, neighbor[1])
                    queue_node.insert(child_idx, neighbor[0])
    return len(path), path, total_cost
