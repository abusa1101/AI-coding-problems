#include "mysearch.h"


Search::Search(Domain* myDomain_) {
    myDomain = myDomain_;
    method = myDomain->method;
}

/*
*   generalSearch()
*
*   High level function that calls a specific search method and
*   then reports the solution.
*/
void Search::generalSearch() {
    // 1) Select the Search Method to use and search
    Solution sol;
    switch (method) {
        case 'B':
            sol = BFS();
            break;
        case 'D':
            sol = DFS();
            break;
        case 'I':
            sol = iterDeep();
            break;
        case 'U':
            sol = uniCost();
            break;
        case 'A':
            sol = aStar();
            break;
        default:
            break;
    }

    cout << "Solution:" << endl;

    // 2) Report a failure if empty
    if (sol.solPath.empty()) {
        cout << "   Failure!" << endl;
        cout << "   Total # of nodes expanded: " <<
                    sol.totalNodesExpanded << endl << endl;
    } else {
        // 3) Else Report the solution and its cost
        cout << "   Found a solution!" << endl;
        cout << "   Total # of nodes expanded: " <<
                    sol.totalNodesExpanded << endl << endl;
        for (int i=0; i < sol.solPath.size(); i++) {
            myDomain->printState(sol.solPath[i]);
        }
        cout << endl << "   Total solution cost = " << sol.totSolCost << endl;
    }
}

Solution Search::BFS() {
    return search<Queue>(maxDepth, false);
}

Solution Search::DFS() {
    return search<Stack>(maxDepth, false);
}

Solution Search::iterDeep() {
    Solution solution;
    int depth = 0;

    while ((depth < maxDepth) && (solution.solPath.empty())) {
        solution = search<Stack>(depth, false);
        depth++;
    }

    return solution;
}

Solution Search::uniCost() {
    return search<priorityQueue>(maxDepth, false);
}

Solution Search::aStar() {
    return search<priorityQueue>(maxDepth, true);
}


/*
*	search()
*
*	General search code function that does all of the work. 
*		
*	queueType: A templatized queue that dictates search order
*   
*   depthLimit: maximum length of solution path that will be considered
*   useHeuristic: Selects whether to use heuristic to guide search or not
*
*	returns the path taken to get to the goal or and empty vector on failure	
*/
template <class queueType>
Solution Search::search(int depthLimit, bool useHeuristic) {
    int num_nodes_expanded = 0;
    Solution sol;

    // Init Open List
    queueType openList;
    Node* newNode = new Node(myDomain->startState);

    openList.push(newNode);

    // init closed list
    std::set<int> closedList;
    std::set<int>::const_iterator it;
    std::pair<std::set<int>::iterator, bool> ret;

    while (1) {
        // 1) Return failure if open list is empty
        if (openList.empty()) {
            cout << __LINE__ << endl;
            cout << "openList.size() = " << openList.size() << endl;
            cout << "openList.empty() = " << openList.empty() << endl;
            sol = Solution();
            sol.totalNodesExpanded = num_nodes_expanded;
            return sol;
        }

        // 2) Otherwise, grab "next" node from open list
        Node* node = openList.pop();

        num_nodes_expanded++;

        // 3) Run Goal Test on the node
        if (myDomain->goalTest(node->state))
            return returnSolution(node, num_nodes_expanded);

        // 4) If node not in closed list and within depth limit, expand it
        ret = closedList.insert(node->state.getHash());
        if ( ret.second  &&  (node->depth < depthLimit) ) {
            std::vector<Action> actions = myDomain->getActions(node->state);

            for (int i=0; i < actions.size(); i++) {
                float g = node->g + actions[i].cost;
                float f = g;
                if (useHeuristic) f += myDomain->heuristic(actions[i].state);

                Node* child = new Node( actions[i].state, node, f, g);
                openList.push(child);
            }
        }
    }
}


/*
*	returnSolution: traceback solution through parent pointers
*/
Solution Search::returnSolution(Node* node, int nodesExp) {
    Solution theSol;

    theSol.totalNodesExpanded = nodesExp;
    theSol.totSolCost = node->g;

    vector<State> sol;

    while (node->parent != nullptr) {
        sol.push_back(node->state);
        node = node->parent;
    }

    sol.push_back(node->state);
    std::reverse(sol.begin(), sol.end());
    theSol.solPath = sol;

    return theSol;
}
































