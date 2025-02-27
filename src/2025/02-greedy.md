# Greedy

A greedy algorithm is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage. In many problems, a greedy strategy does not produce an optimal solution, but a greedy heuristic can yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time. 

# Greedy Algorithms

A greedy algorithm decides what to do in each step, only based on the current situation, without a thought of how the total problem looks like.

In other words, a greedy algorithm makes the locally optimal choice in each step, hoping to find the global optimum solution in the end.

# Two properties must be true for a problem for a greedy algorithm to work:

- __Greedy Choice Property:__ Means that the problem is so that the solution (the global optimum) can be reached by making greedy choices in each step (locally optimal choices).
- __Optimal Substructure:__ Means that the optimal solution to a problem, is a collection of optimal solutions to sub-problems. So solving smaller parts of the problem locally (by making greedy choices) contributes to the overall solution.


# Algorithms That Are Not Greedy

- __Merge Sort__
- __Quick Sort__
- __BFS and DFS Traversal__
- __Finding the nth Fibonacci number using memoization__
