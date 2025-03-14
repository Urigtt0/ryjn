#№2
#dist наход расстояние 
#itertools перебирает все знач
'''from itertools import *
from math import *

lst = [list(map(float, input().split())) for i in range(6)]
a = permutations(lst, r=4)
mini = 1000000000
rast = []
tochki = []
for x in a:
    rast = [dist(x[0], x[1]), dist(x[1], x[2]), dist(x[2], x[3])]
    if sum(rast) < mini:
        mini = sum(rast)
        tochki = x
for j in tochki:
    print(*j)
print(round(mini, 2))'''


'''otnvl, trebvl, V, skor = map(float, input().split())
t = 293
davl = 2.34 * 10**3
molmas = 18 / 1000
ungas = 8.31
skor = skor / 1000
davl1 = 
RT = ungas * t'''

#№1
'''N, K = int(input()), int(input())
sokr = list(map(int, input().split()))
h = dict()
for i in range(N):
    mostik = list(map(int, input().split()))
    if mostik[0] in h:
        h[mostik[0]].append(mostik[1])
    else:
        h[mostik[0]] = [mostik[1]]'''
a = [34, 345, 67, 1, 5]
import math
b = math.lcm(*a)
print(b)
'''import itertools
b = list(permutations(a, r=2))
print(b)'''


    