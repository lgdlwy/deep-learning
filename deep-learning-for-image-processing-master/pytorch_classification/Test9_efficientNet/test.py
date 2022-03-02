
import copy
default_cnf = [[3, 32, 16, 1, 1, True,  1],
                       [3, 16, 24, 6, 2, True,  2],
                       [5, 24, 40, 6, 2, True,  2],
                       [3, 40, 80, 6, 2, True,  3],
                       [5, 80, 112, 6, 1, True,  3],
                       [5, 112, 192, 6, 2, True, 4],
                       [3, 192, 320, 6, 1, True,  1]]
cnf = copy.copy(default_cnf)
for stage, args in enumerate(default_cnf):


    print(cnf.pop(-1))