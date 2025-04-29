from typing import List

class DisjointSet:
    def __init__(self, size: int):
        # init parent with each element as its own representative
        self.parent = list((range(size)))
        # init rank of each to 0
        # rank is used to optimize the union operation
        self.rank = [0] * size

    def find_representative(self, i):
        # similar to traversing from head to last node of a linked list
        if self.parent[i] == i:
            return i
        return self.find_representative(self.parent[i])

    def unite(self, i, j):
        i_r = self.find_representative(i)
        j_r = self.find_representative(j)
        
        # make the representative of set i be the representative of set j if the rank of i is less than j, and vice versa
        if self.rank[i_r] < self.rank[j_r]:
            self.parent[i_r] = j_r
        elif self.rank[i_r] > self.rank[j_r]:
            self.parent[j_r] = i_r
        else:
            self.parent[j_r] = i_r
            self.rank[i_r] += 1
        
    def in_same_set(self, a, b):
        # determine if elements a,b are in the same set
        return self.find_representative(a) == self.find_representative(b)



def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    # kruskal's algo for undirected unweighted graph
    n = len(edges)
    d_set = DisjointSet(n)
    diff = edges.copy()

    # note: nodes are 1-indexed in this question
    for (source, dest) in edges:
        ...
        s = source-1
        d = dest-1
        if not d_set.in_same_set(s, d):
            d_set.unite(s, d)
            diff.remove([source, dest])
    
    # return the last element of list difference
    return diff[-1]

print(findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]))
