
# #BFS
# procedure BFS(G, start_v) is
# 2      let Q be a queue
# 3      label start_v as discovered
# 4      Q.enqueue(start_v)
# 5      while Q is not empty do
# 6          v := Q.dequeue()
# 7          if v is the goal then
# 8              return v
# 9          for all edges from v to w in G.adjacentEdges(v) do
# 10             if w is not labeled as discovered then
# 11                 label w as discovered
# 12                 w.parent := v
# 13                 Q.enqueue(w)

# function BFS(problem) returns a solution, or failure
# node ← a node with STATE = problem.INITIAL-STATE , PATH-COST = 0
# if problem.GOAL-TEST (node.STATE ) then return SOLUTION (node)
# frontier ← a FIFO queue with node as the only element
# explored ← an empty set
# loop do
#     if EMPTY ?( frontier ) then return failure
#     node ← POP ( frontier ) /* chooses the shallowest node in frontier */
#     add node.STATE to explored
#     for each action in problem.ACTIONS (node.STATE ) do
#         child ← CHILD-NODE ( problem, node, action)
#         if child.STATE is not in explored or frontier then
#             if problem.GOAL -TEST (child .STATE ) then return SOLUTION (child )
#             frontier ← INSERT (child , frontier )
# def BFS(graph, root_node, goal):
#     explored = list()
#     frontier = Queue()
#     frontier.put(root_node)
#     while True:
#         if frontier.empty():
#             return None
#         actual = frontier.get()
#         if actual == goal:
#             return actual
#         elif goal not in explored:
#             explored.append(actual.state.puzzle)
#             succ = actual.succ()
#             while not succ.empty():
#                 frontier.put(succ.get())
# starting node = root_node

# //////////////////DFS
# def DFS(graph, root_node, goal_node):
#     explored = list()
#     queue = [root_node]
#     while True:
#         if not queue:
#             return None
#         node = queue.pop()
#         print(node)
#         if node == goal_node:
#             return node
#         if node in graph:
#             for neighbor in graph[node]:
#                 if neighbor not in explored:
#                     explored.append(neighbor)
#                     queue.append(neighbor)
#     return explored
# def dfs(graph, root, goal):
#     visited = set()
#     queue = [(start,[start])]
#     while queue:
#         node = stack.pop()
#         for next in graph[vertex] - set(path):
#         if node not in visited:
#             visited.add(node)
#             queue.extend(graph[node] - visited)
#     return visited
# def dfs_paths(graph, start, end):
#     stack = [(start, [start])]
#     while stack:
#         (vertex, path) = stack.pop()
#         for next in graph[vertex] - set(path):
#             if next == end:
#                 yield path + [next]
#             else:
#                 stack.append((next, path + [next]))
# def DFS(graph, root, goal, depth):
#     leaves = [root] #or set()?
#     while True:
#         if not leaves:
#             return None
#         node = leaves.pop(-1)
#         if node == goal:
#             return node
#         if node.depth is not depth:
#             succ = actual.succ()
#             while not succ.empty():
#                 leaves.put(succ.get())
# def DFS-iterative (graph, root, goal, limit):
#     stack = list()
#     stack.push(root_node)
#     visited = [root_node]
#     while True :
#         if not stack:
#             return None
#         node = stack.top()
#         stack.pop()
#         if node == goal :
#             return node
#         if depth(node) < limit :
#                 children = successor-fn(node)
#                 for child in children
#                 push(child)
#             else :
#                 return None
# # DFS-iterative (G, s):
# #       let S be stack
# #       S.push( s )            //Inserting s in stack
# #       mark s as visited.
# #       while ( S is not empty):
# #           //Pop a vertex from stack to visit next
# #           v  =  S.top( )
# #          S.pop( )
# #          //Push all the neighbours of v in stack that are not visited
# #         for all neighbours w of v in Graph G:
# #             if w is not visited :
# #                      S.push( w )
# #                     mark w as visited
#
#
#     DFS-recursive(G, s):
#         mark s as visited
#         for all neighbours w of s in Graph G:
#             if w is not visited:
#                 DFS-recursive(G, w)/Where G is graph and s is source vertex
# def DFS2(graph, root, visited):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     print(start)
#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited
# def dfs(graph, node, visited):
#     if node not in visited:
#         visited.append(node)
#         for n in graph[node]:
#             dfs(graph,n, visited)
#     return visited

# function DEPTH -LIMITED -S EARCH ( problem, limit ) returns a solution, or failure/cutoff
#     return RECURSIVE -DLS(MAKE-NODE (problem.I NITIAL -S TATE ), problem, limit )
#
# function RECURSIVE -DLS(node, problem, limit ) returns a solution, or failure/cutoff
#     if problem.G OAL -T EST (node.S TATE ) then return S OLUTION (node)
#     else if limit = 0 then return cutoff
#     else
#         cutoff occurred ? ← false
#         for each action in problem.A CTIONS (node.S TATE ) do
#             child ← C HILD -N ODE ( problem, node, action)
#             result ← R ECURSIVE -DLS(child , problem, limit − 1)
#             if result = cutoff then cutoff occurred ? ← true
#             else if result  = failure then return result
#     if cutoff occurred ? then return cutoff else return failure

# def dfs(graph, start, end):
#     frontier = [start, ]
#     explored = []
#
#     while True:
#         if not frontier:
#             return None
#         node = frontier.pop()
#         explored.append(node)
#         if node == goal_node:
#             return node
#
#         # expanding nodes
#         for node in reversed(graph[current_node]):
#             if node not in explored:
#                 frontier.append(node)
# G= {} #initializes the empty dictionary
# G['A'] = {} #Creates a key 'A' in the dictionaries and assigns the key to a value of another empty hash
# (G['A'])['B'] = 1 #Creates a Sub-Hash for key 'A' of the hash,Sub-hash is {'B':1}
# print G

# def DFS_I(graph, start, end, limit):
#     frontier = [start, ]
#     explored = set()
#
#     while True:
#         if not frontier:
#             return None
#         node = frontier.pop()
#         print(node)[]
#         explored.append(node)
#         if node == goal_node:
#             return node
# def DFS_I2(G, s):
#     S = []
#     visited = []
#     S.push(s)
#     visited.append(s)
#     while S:
#         # Pop a vertex from stack to visit next
#         v  =  S.top( )
#         S.pop(v)
#         # Push all the neighbours of v in stack that are not visited
#         for all neighbours w of v in graph:
#             if w is not visited:
#                 S.push(w)
#                 visited.append(w)
#
#
#     DFS-recursive(G, s):
#         mark s as visited
#         for all neighbours w of s in Graph G:
#             if w is not visited:
#                 DFS-recursive(G, w)
# def depth_limited_search(graph, start_node, goal_node, limit):
#     node = start_node
#     print(node)
#     def recursive_dls(graph, node, goal_node, limit):
#         if node == goal_node:
#             return node
#         elif limit == 0:
#             return 'limit reached'
#         else:
#             is_limit = False
#             for child in graph[start_node]:
#                 result = recursive_dls(graph, child, goal_node, limit - 1)
#                 if result == 'limit reached':
#                     is_limit = True
#                 elif result is not None:
#                     return result
#             return 'limit reached' if is_limit else None
#
#     # Body of depth_limited_search:
#     return recursive_dls(graph, node, goal_node, limit)
# def DFS_Rec2(graph, vertex, goal, path, limit):
#     continue_rec = True
#     if continue_rec:
#         limit = limit + 1
#         path += [vertex]
#         print(vertex)
#         if vertex == goal:
#             continue_rec = False
#         if limit < 16:
#             if vertex in graph:
#                 for neighbor in graph[vertex]:
#                     if neighbor not in path:
#                         path = DFS_Rec2(graph, neighbor, goal, path, limit)
#     return path
# def DLS(self,src,target,maxDepth):
#     if src == target :
#         return True
#     # If reached the maximum depth, stop recursing.
#     if maxDepth <= 0 :
#         return False
#     # Recur for all the vertices adjacent to this vertex
#     for i in self.graph[src]:
#             if(self.DLS(i,target,maxDepth-1)):
#                 return True
#     return False

# //////////////////////////////////////# ID
# def IDDFS(self,src, target, maxDepth):
#     # Repeatedly depth-limit search till the
#     # maximum depth
#     for i in range(maxDepth):
#         if (self.DLS(src, target, i)):
#             return True
#     return False


# ///////////////////////////UC
dist[s]    ←0
(distance    to    source    vertex    is    zero)
for        all    v    ∈    V–{s}
do        dist[v]    ←∞
(set    all    other    distances    to    infinity)
S←∅
(S,    the    set    of    visited    vertices    is    initially    empty)
Q←V
(Q,    the    queue    initially    contains    all    vertices)
while    Q    ≠∅
(while    the    queue    is    not    empty)
do            u    ←mindistance(Q,dist)
(select    the    element    of    Q    with    the    min.    distance)
S←S∪{u}
(add    u    to    list    of    visited    vertices)
for    all    v    ∈    neighbors[u]
do        if            dist[v]    >    dist[u]    +    w(u,    v)
(if    new    shortest    path    found)
then                        d[v]    ←d[u]    +    w(u,    v)
(set    new    value    of    shortest    path)
(if    desired,    add    traceback    code)
return    dist


def ucs(G, v):
    visited = set()                  # set of visited nodes
    q = queue.PriorityQueue()        # we store vertices in the (priority) queue as tuples
                                     # (f, n, path), with
                                     # f: the cumulative cost,
                                     # n: the current node,
                                     # path: the path that led to the expansion of the current node
    q.put((0, v, [v]))               # add the starting node, this has zero *cumulative* cost
                                     # and it's path contains only itself.

    while not q.empty():             # while the queue is nonempty
        f, current_node, path = q.get()
        visited.add(current_node)    # mark node visited on expansion,
                                     # only now we know we are on the cheapest path to
                                     # the current node.

        if current_node.is_goal:     # if the current node is a goal
            return path              # return its path
        else:
            for edge in in current_node.out_edges:
                child = edge.to()
                if child not in visited:
                    q.put((current_node_priority + edge.weight, child, path + [child])

def UCS(graph, start_node, goal_node):
    visited = set()
    queupathe = PriorityQueue()
    queue.put((0, start))
    while True:
        if not queue:
            return
        cost, node = queue.get()
        if node not in visited:
            visited.add(node)
            if node == goal_node:
                return
            for i in graph.neighbors(node):
                if i not in visited:
                    total_cost = cost + graph.get_cost(node, i)
                    queue.put((total_cost, i))

def UCS(graph, start, goal_node):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))

    while True:
        if not queue:
            return
        cost, node = queue.get()
        if node not in visited:
            visited.add(node)
            if node == goal_node:
                return visited
            for i in graph[node]:
                if i[0] not in visited:
                    total_cost = float(cost) + float(i[1])
                    queue.put((total_cost, i[0]))
def search(graph, start, end):
    if start not in graph:
        raise TypeError(str(start) + ' not found in graph !')
        return
    if end not in graph:
        raise TypeError(str(end) + ' not found in graph !')
        return

    queue = Q.PriorityQueue()
    queue.put((0, [start]))

    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]

        if end in node[1]:
            print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            break

        cost = node[0]
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))
def search(graph, start, end):
    queue = Q.PriorityQueue()
    queue.put((0, [start]))
    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
        if end in node[1]:
            break
        cost = node[0]
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()   # Fringe (Priority Queue) to store the nodes along with their paths
    visited_nodes = set()   # A set to maintain all the visited nodes
    fringe.push((problem.getStartState(), [], 0), 0)   # Pushing (Node, [Path from start-node till 'Node'], Culmulative backward cost till 'Node') to the fringe. In this case, we are using culmulative backward cost as a factor based on which priority is decided.
    while True:
        popped_element = fringe.pop()
        node = popped_element[0]
        path_till_node = popped_element[1]
        cost_till_node = popped_element[2]
        if problem.isGoalState(node):   # Exit on encountering goal node
            break
        else:
            if node not in visited_nodes:   # Skipping already visited nodes
                visited_nodes.add(node)     # Adding newly encountered nodes to the set of visited nodes
                successors = problem.getSuccessors(node)
                for successor in successors:
                    child_node = successor[0]
                    child_path = successor[1]
                    child_cost = successor[2]
                    full_path = path_till_node + [child_path]   # Computing path of child node from start node
                    full_cost = cost_till_node + child_cost     # Computing culmulative backward cost of child node from start node
                    fringe.push((child_node, full_path, full_cost), full_cost)   # Pushing (Node, [Path], Culmulative backward cost) to the fringe.

    return path_till_node

# def UCS(graph, start_node, goal_node):
#     visited = []
#     queue_node = [start_node]
#     queue_cost = [0]
#     queue_path = []
#     while True:
#         if not queue_node:
#             return
#         cost_til_node = queue_cost.pop()
#         node = queue_node.pop()
#         path_til_node = queue_path.pop()
#         if node == goal_node:
#             return path_til_node, cost_til_node
#         else:
#             if node not in visited:
#                 visited.append(node)
#                 for neighbor in graph[node]:
#                     child_node = neighbor[0]
#                     child_path = neighbor
#                     child_cost =
#                     full_path =
#                     full_cost =
#                     queue_node.append(neighbor[0])
#                     total_cost = float(cost) + float(neighbor[1])
#                     queue_cost.append(total_cost)
#
#     return path_til_node, cost_til_node

def UCS2(graph, root_node, goal_node):
    # print(graph)
    explored = list()
    queue = [root_node] #FIFO
    queue_cost = [0]
    explored.append(root_node)
    path = []
    while True:
        if not queue:
            return
        node = queue.pop(0)
        cost = queue_cost.pop(0)
        path.append(node)
        if node == goal_node:
            return path, queue_cost
        if node in graph:
            for neighbor in graph[node]:
                if neighbor[0] not in explored:
                    explored.append(neighbor[0])
                    queue.append(neighbor[0])
                    total_cost = (cost) + (neighbor[1])
                    queue_cost.append(total_cost)
    return path

        # min_cost_idx = queue_cost.index(min(queue_cost))
        # cost = queue_cost.pop(min_cost_idx)
        # node = queue_node.pop(min_cost_idx)
                # costs = [float(i) for i in queue_cost]
                # total_cost = sum(costs)
                # print(visited)
                # print(total_cost)
# if total_cost < min_cost:
#     min_cost = total_cost
#     min_path = visited

# def ucs(G, v):
#     visited = set()                  # set of visited nodes
#     q = queue.PriorityQueue()        # we store vertices in the (priority) queue as tuples
#                                      # (f, n, path), with
#                                      # f: the cumulative cost,
#                                      # n: the current node,
#                                      # path: the path that led to the expansion of the current node
#     q.put((0, v, [v]))               # add the starting node, this has zero *cumulative* cost
#                                      # and it's path contains only itself.
#
#     while not q.empty():             # while the queue is nonempty
#         f, current_node, path = q.get()
#         visited.add(current_node)    # mark node visited on expansion,
#                                      # only now we know we are on the cheapest path to
#                                      # the current node.
#
#         if current_node.is_goal:     # if the current node is a goal
#             return path              # return its path
#         else:
#             for edge in in current_node.out_edges:
#                 child = edge.to()
#                 if child not in visited:
#                     q.put((current_node_priority + edge.weight, child, path + [child])
# def UCS(graph, start_node, goal_node):
#     visited = set()
#     queue_node = [start_node]
#     queue_cost = [0]
#     while True:
#         if not queue_node:
#             return
#         min_cost_idx = 0
#         cost = 0
#         if queue_cost:
#             min_cost_idx = queue_cost.index(min(queue_cost))
#             cost = queue_cost.pop(min_cost_idx)
#         node = queue_node.pop(min_cost_idx)
#         if node == goal_node:
#             return len(visited), visited, cost
#         visited.add(node)
#         for neighbor in graph[node]:
#             if neighbor[0] not in visited and neighbor[0] not in queue_node:
#                 queue_node.append(neighbor[0])
#             elif neighbor[0] in queue_node:
#                 if neighbor[1] < cost:
#                     del queue_node[neighbor[0]]
#                     del queue_cost[neighbor[1]]
#                     queue_node.append(neighbor[0])
#                     queue_cost.append(neighbor[1])
#                 # queue_node.insert(0, neighbor[0])
#                 # total_cost = float(cost) + float(neighbor[1])
#                 # queue_cost.insert(0, total_cost)
#     return len(visited), visited, cost
/////////////////////////////////////A*

 fringe = util.PriorityQueue()    # Fringe (Priority Queue) to store the nodes along with their paths
    visited_nodes = set()    # A set to maintain all the visited nodes
    fringe.push((problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem) + 0)    # Pushing (Node, [Path from start-node till 'Node'], Culmulative backward cost till 'Node') to the fringe. In this case, we are using the sum of culmulative backward cost and the heutristic of the node as a factor based on which priority is decided.
    while True:
        popped_element = fringe.pop()
        node = popped_element[0]
        path_till_node = popped_element[1]
        cost_till_node = popped_element[2]
        if problem.isGoalState(node):    # Exit on encountering goal node
            break
        else:
            if node not in visited_nodes:    # Skipping already visited nodes
                visited_nodes.add(node)     # Adding newly encountered nodes to the set of visited nodes
                successors = problem.getSuccessors(node)
                for successor in successors:
                    child_node = successor[0]
                    child_path = successor[1]
                    child_cost = successor[2]
                    full_path = path_till_node + [child_path]    # Computing path of child node from start node
                    full_cost = cost_till_node + child_cost    # Computing culmulative backward cost of child node from start node
                    fringe.push((child_node, full_path, full_cost), full_cost + heuristic(child_node, problem))    # Pushing (Node, [Path], Culmulative backward cost) to the fringe.

    return path_till_node

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

def Astar(graph, start_node, goal_node):
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

# visited = []
# queue_node = [start_node]
# queue_cost = []
# path = []
# total_cost = 0
# total_nodes = set()
# is_init = True
# while True:
#     if not queue_node:
#         return 'failure'
#     if is_init:
#         cost = 0
#         node = queue_node.pop(0)
#         is_init = False
#     else:
#         min_cost_idx = queue_cost.index(min(queue_cost))
#         cost = queue_cost.pop(min_cost_idx)
#         node = queue_node.pop(min_cost_idx)
#     path.append(node)
#     total_cost = total_cost + cost
#     if node not in visited:
#         visited.append(node)
#     if node == goal_node:
#         return len(path), path, total_cost
#     for neighbor in graph[node]:
#         if neighbor[0] not in visited and neighbor[0] not in queue_node:
#             queue_node.insert(-1, neighbor[0])
#             queue_cost.insert(-1, neighbor[1])
#         elif neighbor[0] in queue_node:
#             child_idx = queue_node.index(neighbor[0])
#             print(cost)
#             print(neighbor[1])
#             print()
#             if float(cost) < float(neighbor[1]):
#                 queue_cost.pop(child_idx)
#                 queue_node.pop(child_idx)
#                 queue_cost.insert(child_idx, neighbor[1])
#                 queue_node.insert(child_idx, neighbor[0])
# return len(path), path, total_cost
