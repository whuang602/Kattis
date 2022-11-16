My two attempts at narrow art gallery

The first attempt (narrowartgallery1) uses a somewhat greedy algorithm which turns out to work up until we encounter K >= N+2. At this point, due to the nature of the algorithm, it's likely to permanent trap itself when it has one last or two rooms left to close. 

Alternate version for the first attempt: instead of emphasizing the selection of rooms to close, calculate the cost of closing every combinations of K rooms and find the max (total-closed_cost) from that.

