My Attempt at Bank Queue.

Basis of Algorithm, since it will be difficult to decide the optimal person to serve starting at time=0,
instead, we can decide who to serve from the latest time(or even the max time allotted). This will allow us to
select the optimal/max person to serve starting from the latest time, and then push people who might still be
optimal options ahead to an earlier time. This algorithm allows for the optimal solution to the problem.
