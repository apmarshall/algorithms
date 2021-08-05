def bfs(graph, start):
    disc_q = []
    proccessed = []
    disc_q + start
    while q != []:
        v = q[0]
        process_vertex_early(v)
        processed + v
        cands = graph.edges[v]
        while cands != []:
            y = cands[0]
            if ((index(processed, y) == null) || (graph.Directed == True)):
                process_edge(v, y)
            if (index(disc_q, y) == null):
                disc_q + y
            cands = cands.remove(y)
        proces_vertex_late(v)
        q = q.remove(v)