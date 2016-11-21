Runtime
------------------------------

Problem 1

When calculating the Big O notation for a particular algorithm, 
it’s necessary to consider the length of time it takes for the algorithm 
to run as the algorithm’s workload approaches infinity. 
You can think of the workload as the number of tasks required to complete a job. 
What determines the workload of figuring out whether your box of animal crackers contains an elephant?

Answer: O(n)


Order the following runtimes in descending order of efficiency (that is, fastest runtimes first, slowest last) as n approaches infinity:

Answer:

O(1)
O(log n)
O(n)
O(n log n)
O(n2)
O(2n) (i.e. 2 to the n-th power)

Stacks and Queues
------------------------------


In the following cases, would a stack or queue be a more appropriate data structure?
1. The process of loading and unloading pallets onto a flatbed truck. Answer: Stack using LIFO.
2. Putting bottle caps on bottles of beer as they roll down an assembly line. Answer: Queue using FIFO.
3. Calculating the solution to this mathematical expression: 2 + (7 * 4) - (3 / 2) Answer: Stack using LIFO, due to needing to know the order and closing of each bracket.
4. Describe two more situations where a queue would be an appropriate data structure. Automatic Carwash line, Bullets in a gun
5. Describe two more situations where a stack would be an appropriate data structure. Plates stacked in a cupboard, Books stacked on a table


Linked Lists
------------------------------

Given the linked list below, which are the nodes? The nodes are the boxes containing data and the arrows which refer to the next node. 
There is the node class which contains the apple node, berry node, and cherry node.

What is the data for each node? The data for each node is the string inside of each node. i.e. the apple node contains the "apple" string.
Where is the head? The head is initialized with the linked-list.
Where is the tail? The tail was not initialized, by traversing the link list we determine that the cherry node is the tail.
(Please be as specific as possible — exactly which parts of the diagram correspond to each part? Arrows? Boxes? Text?)

What’s the difference between doubly- and singly-linked lists? A doubly linked-list contain both the next and previous nodes. 
Whereas, a singly-linked list contains just the next node.

Why is it faster to append to a linked list if we keep track of the tail as an attribute?
It is faster to keep track of the tail because it prevents having the traverse to every node in the list.



Trees
------------------------------

Given the tree above, in what order would a Breadth First Search (BFS) algorithm visit each node until finding burrito (starting at food)? Just list the order of nodes visited; no need to recreate the state of the algorithm data in your answer.

[food]
[Italian, Indian, Mexican]
[Indian, Mexican, lasagna, pizza]
[Mexican, lasagna, pizza, tikka masala, saag]
[lasagna, pizza, tikka masala, saag, burrito, tacos, enchiladas]
[pizza, tikka masala, saag, burrito, tacos, enchiladas]
[tikka masala, saag, burrito, tacos, enchiladas]
[saag, burrito, tacos, enchiladas]
[burrito, tacos, enchiladas]

Pop burrito.

Given the tree above, in what order would a Depth First Search (DFS) algorithm visit each node until finding Chicago-style (starting at food)? Just list the order of nodes visited; no need to recreate the state of the algorithm data in your answer.

[food]
[Italian, Indian, Mexican]
[Italian, Indian, burrito, tacos, enchiladas]
[Italian, Indian, burrito, tacos]
[Italian, Indian, burrito]
[Italian, Indian]
[Italian, tikka masala, saag]
[Italian, tikka masala]
[Italian]
[lasagna, pizza]
[lasagna, thin crust, Chicago-style, New York-style, Sicilian]
[lasagna, thin crust, Chicago-style, New York-style]
[lasagna, thin crust, Chicago-style]

Pop Chicago-style.

How is a binary search tree different from other trees? Binary search tree nodes has at most 2 children, rules for arrangement, and is made of nodes.
