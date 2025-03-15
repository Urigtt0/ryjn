#№1
'''N, K = map(int, input().split())
sokr = list(map(int, input().split()))
h = dict()
for i in range(N - 1):
    mostik = list(map(int, input().split()))
    if mostik[0] in h:
        h[mostik[0]].append(mostik[1])
    else:
        h[mostik[0]] = [mostik[1]]
    if mostik[1] in h:
        h[mostik[1]].append(mostik[0])
    else:
        h[mostik[1]] = [mostik[0]]
        l = []
for k, j in h.items():
    if len(j) == 2 :
        s = sokr[k-1] + sokr[j[0]-1] + sokr[j[1]-1]
        l.append(s)
print(max(l))'''


#№2
from math import *
from itertools import *
lst = [list(map(float, input().split())) for i in range(6)]
a = permutations(lst, r=4)
mini = 1000000000
rast = []
tochki = []
for t in a:
    rast = [dist(t[0], t[1]), dist(t[1], t[2]), dist(t[2], t[3])]
    if sum(rast) < mini:
        mini = sum(rast)
        tochki = t
for j in tochki:
    print(*j)
print(round(mini, 2))