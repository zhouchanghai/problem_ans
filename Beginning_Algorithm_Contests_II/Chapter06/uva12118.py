#Eulerian path
def solve(V,edges):
    if not edges:
        return 0
    adj = [[] for i in range(V+1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    visited = [0] * (V+1)
    oddNodes, oddComps, evenComps = 0, 0, 0
    for i in range(1,V+1):
        if visited[i] or not adj[i]: continue
        q = [i]
        odds = 0
        while q:
            tmp = set()
            for a in q:
                if visited[a]: continue
                visited[a] = 1
                if len(adj[a]) % 2:
                    odds += 1
                for b in adj[a]:
                    if not visited[b]:
                        tmp.add(b)
            q = tmp
        oddNodes += odds
        if odds > 0:
            oddComps += 1
        else:
            evenComps += 1
    #print("oddComps {} evenComps {} oddNodes {} edges {}".format(oddComps,evenComps,oddNodes, len(edges)))
    connect = oddComps + evenComps - 1
    if connect == 0:
        return len(edges) + max((oddNodes-2)//2, 0)

    if evenComps == 0:
        # O-O-O-O
        oddNodes -= 2*connect
    elif evenComps == 1:
        # E-O-O-O
        oddNodes -= 2*(connect-1)
    else: #evenComps >= 2
        # First, connect all even components
        # E-E-E-E for each E connect at the same node except the two ends
        # Use evenComps-1 connections and add 2 odd nodes
        # Every other connection reduces 2 odd nodes
        oddNodes = oddNodes + 2 - (connect - (evenComps - 1))*2
    return len(edges) + connect + max((oddNodes-2)//2, 0)

c = 0
while True:
    c += 1
    V,E,T = input().strip().split()
    V,E,T = int(V), int(E), int(T)
    if V == 0:
        break
    edges = []
    for i in range(E):
        a,b = input().strip().split()
        edges.append((int(a), int(b)))
    print("Case {}: {}".format(c, T*solve(V,edges)))