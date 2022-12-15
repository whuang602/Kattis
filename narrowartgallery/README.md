My two attempts at narrow art gallery

The first attempt (narrowartgallery1) uses a somewhat greedy algorithm which turns out to work up until we encounter K >= N-2. At this point, due to the nature of the algorithm, it's likely to permanently trap itself when it has one last or two rooms left to close. 

Alternate version for the first attempt: instead of emphasizing the selection of rooms to close, calculate the cost of closing every combinations of K rooms and find the max (total-closed_cost) from that. Extremely greedy and have a long runtime.

The 2nd attempt (narrowartgallery2) is based on dynamic programming. The basic premise is that we will create a 3d matrix that stores every imaginable combinations of closed rooms. However, through the placement of the recursive calls, the optimal values for closing 1 to K-1 rooms when given only 1 to 2N rooms will be calculated first. This makes the recursive calls for max K and max rooms # take minimal runtime and therefore satisfies the Kattis requirement. More specifically, it can be observed that since you can't close both horizontal rooms, you only have to worry about closing one of the two rooms at a time. 
