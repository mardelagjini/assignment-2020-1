from sys import argv
from pprint import pprint

#diabasma orismatwn
#exei dosei -p
if argv[1] == "-p":
    pp = True
    n = argv[2]
#den exei dosei -p
else:
    pp = False
    n = argv[1]

#metetrepse to keimeno se arithmo
n = int(n)

#bres tous kombous
#kenos grafos
G={}
#to diasthma tou x
x_start = -n
x_end = n
for x in range(x_start+1, x_end):
    #to diasthma tou y
    y_start = -n
    y_end = n
    for y in range(y_start+1, y_end):
        #den ta pairnoume ola
        if abs(x) + abs(y) < n:
            if y>0 or y==0 and x>=0:
                G[(x,y)] = []

#bres tous geitones tous
for x in range(x_start+1, x_end):
    for y in range(y_start+1, y_end):
        if abs(x) + abs(y) < n:
            if y>0 or y==0 and x>=0:

                #oi geitones kinountai sta idia oria
                for neighbor_x in range(x_start+1, x_end):
                    for neighbor_y in range(y_start+1, y_end):
                        if abs(neighbor_x) + abs(neighbor_y) < n:
                            if neighbor_y>0 or neighbor_y==0 and neighbor_x>=0:
               
                                #oi geitones einai panw, katw, deksia i aristera
                                if neighbor_x==x-1 and neighbor_y==y:
                                    G[(x,y)].append((neighbor_x, neighbor_y))
                                if neighbor_x==x and neighbor_y==y-1:
                                    G[(x,y)].append((neighbor_x, neighbor_y))
                                if neighbor_x==x+1 and neighbor_y==y:
                                    G[(x,y)].append((neighbor_x, neighbor_y))
                                if neighbor_x==x and neighbor_y==y+1:
                                    G[(x,y)].append((neighbor_x, neighbor_y))

#ektupose
if pp:
    pprint(G)

#i sunartisi
def CountFixedPolyominoes(G, untried, n, p, c):
    while not len(untried) == 0:
        u = untried.pop()
        p.append(u)
        if len(p) == n:
            c.append(1) #an to c itan arithmos, tha itan local, to kano lista
        else:
            new_neighbors = set()
            #to AdjacencyList
            AdjacencyList = G[u]
            for v in AdjacencyList:

                #ftiakse tous Neighbors[p-u]
                Neighbors = []
                for pair in p:
                    if pair != u:
                        for neighbor_pair in G[pair]:
                            Neighbors.append(neighbor_pair)

                if v not in untried and v not in p and v not in Neighbors:
                    new_neighbors.add(v)
           
            #ftiakse to new_untried
            new_untried = set()
            for item in untried:
                new_untried.add(item)
            for item in new_neighbors:
                new_untried.add(item)
            CountFixedPolyominoes(G, new_untried, n, p, c)
        p.remove(u)
    return len(c)

untried = {(0,0)}
p = []
c = []
print(CountFixedPolyominoes(G, untried, n, p, c))
