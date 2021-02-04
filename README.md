# BTS-World

This is my own BTS World Calculator. It operates similarly to the one online,
but with the added feature that my program can compute a valid combination for an Another Story season 2 mission.
magicshop_solver.py is the main program, cardsconverter.py converts messy data from the
BTS World Calculator into a cleaner data set called BTS_World_Managername.txt.

magicshop_solver.py consists of a dynamic programming implementation of a variant of the subset sum problem.
A mission can calculate the amount of points that each card gives when playing it.
Given a set of cards, magicshop_solver.py attempts to find a subset of cards whose points sum up
to a number close enough to a target score, by a 99% margin. There are two added constraints.
For each mission, there is a maximum amount of cards that can be played, and some slots may require a
card from a specific BTS member.

Since the implementation is very expensive space-wise, my algorithm terminates when a combination is found,
so that not the entire matrix needs to be filled.
