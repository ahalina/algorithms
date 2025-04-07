def dfsi(g, st, nn):
    vv = [False] * (nn + 1)
    ss = []
    rr = []
    ss.append(st)
    while ss:
        v = ss.pop()
        if not vv[v]:
            vv[v] = True
            rr.append(str(v))
            for nei in reversed(g[v]):
                if not vv[nei]:
                    ss.append(nei)
    return rr

n_v = int(input())
gr = {i: [] for i in range(1, n_v + 1)}
for i in range(1, n_v + 1):
    p = list(map(int, input().split()))
    k_nei = p[0]
    neis = p[1:]
    gr[i] = neis
res = dfsi(gr, 1, n_v)
print(' '.join(res))