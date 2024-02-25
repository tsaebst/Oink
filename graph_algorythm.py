class Edge:
    def __init__(self, w, v, d):
        self.w = w
        self.v = v
        self.d = d

    def unite(self, v1, v2, verts, size_of_component):
        # finding the root of current component in which the verts data is located
        v1 = self.find(v1-1, verts)
        v2 = self.find(v2-1, verts)
        # check if it's not the same component
        if v1 == v2:
            return False
        # check how many verts are in each component
        if size_of_component[v1] < size_of_component[v2]:
            v1, v2 = v2, v1
        # upd the root of v2 component( now it's v1's root)
        verts[v2] = v1
        # upd the size of the biggest component
        size_of_component[v1] += size_of_component[v2]
        return True

    def find(self, v, verts):
        # if vert is not the one from which the component is being built around
        if verts[v] != v:
            # recursively searching for the verts
            verts[v] = self.find(verts[v], verts)
        return verts[v]

# initializing the anount of verts/edges, overall weight value of the route of the spanning tree
res = 0
n, m = map(int, input().split())
edges = [Edge(0, 0, 0) for i in range(m)]

for i in range(m):
    edges[i].w, edges[i].v, edges[i].d = map(int, input().split())

edges.sort(key=lambda x: x.d)

verts = list(range(n))
# the group represents the amount of components in graph around the particular vert
# each of them is filled with just one vert only, index of which is equal to n-i-1 position here
size_of_component = [1] * (n)
for i in range(m):
    # check if we can unite 2 components
    if edges[i].unite(edges[i].w, edges[i].v, verts, size_of_component):
        # upd the 'size', which is overall weight component to the result
        res += edges[i].d
print(res)