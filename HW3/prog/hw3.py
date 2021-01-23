import itertools
import random
import re
import string
from collections import defaultdict, Counter
from functools import reduce
from operator import eq, neg

from sortedcontainers import SortedSet

import search
from utils import argmin_random_tie, count, first, extend

from csp import * 


#1

print("[Backtracking Search] ")
print("4 queens: ", (backtracking_search(NQueensCSP(4))))
print("12 queens: ", (backtracking_search(NQueensCSP(12))))
print("20 queens: ", (backtracking_search(NQueensCSP(20))))


#2
print("[Backtracking Search- Forewards]")
print("4 queens: ", (backtracking_search(NQueensCSP(4), inference=forward_checking)))
print("12 queens: ", (backtracking_search(NQueensCSP(12), inference=forward_checking)))
print("20 queens: ", (backtracking_search(NQueensCSP(20), inference=forward_checking)))


#3
print("[Map Coloring with Backtracking!!!!]")
print((backtracking_search(australia_csp)))


#4
print("[Map Coloring with FOUR Colors!]")
australia_csp_4color = MapColoringCSP(list('RGBY'), """SA: WA NT Q NSW V; NT: WA Q; NSW: Q V; T: """)
print((backtracking_search(australia_csp_4color)))
print("Only 3 colors needed since the 3/4 color solutions are the same every time")


#5
print("[Map Coloring with TWO Colors!]")
australia_csp_4color = MapColoringCSP(list('RG'), """SA: WA NT Q NSW V; NT: WA Q; NSW: Q V; T: """)
print((backtracking_search(australia_csp_2color)))
print("No solutions found for 2 color")


#6
print("[Coloring w/ AC-3]")
print((AC3(australia_csp)))



#7
print(" [United States Map w/ Backtracking]")
print((backtracking_search(usa_csp)))

