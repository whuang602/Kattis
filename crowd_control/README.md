My attempt at the Crowd Control problem

Goal: We want to maximize the number of people who can walk through the streets given a constant stream, meaning that we want to maximize the minimum capacity of the streets/paths from intersection 0 to intersection n-1.

Algorithm: 

1) Utilize Kruskal Algorithm (to select edges with max weight) in conjunction with UnionFind (to detect cycle) to find the Max Spanning Tree. 

2) Given said MST, we can use Depth First Search to find the path from starting intersection to the latest intersection. This is done via creating two DFS lists (one starting from intersection 0 and one starting from final intersection) which can then be used to determine the optimal path from the starting vertex to the desired vertex. If unsure of how to do this, just print out both lists and look for the pattern.

3) Given the optimal path and therefore streets that aren't adjacent to these paths, the streets to be blocked can be determined. This can either be done backwards by blocking all paths and selecting certain paths to unblock or selecting only adjacent streets to block. Either should work.

Note: The program mainly uses lists, but can easily be made more efficient and simpler with use of other data structures (dicts, etc). Based on what I know, Dijkstra's algorithm can be altered to achieve a similar result.
