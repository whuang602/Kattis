My attempt at Air Conditioned Minions in Python 3

acm.py does not work completely as it's a greedy algorithm aimed around selecting temperature ranges with the most overlaps, as it turns out, with input like what's inside input.txt, the program will fail as it simply selects all overlaps(even when those overlapped ranges might not even touch each other).

acm2.py works and functions well because its aim is to sort the ranges by lowest temperate ends, and selecting those that it overlaps with. This bypasses the problem that acm.py had.
