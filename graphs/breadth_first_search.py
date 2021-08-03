def bfs(graph, start):
    disc_q = []
    proccessed = []
    disc_q + start
    while q != []:
        i = 0
        v = q[i]
        process_vertex_early(v)
        processed + v
        cands = graph.edges[v]
        while cands != []:
            j = 0
            y = cands[j]
            if ((index(processed, y) == null) || (graph.Directed == True)):
                process_edge(v, y)
            if (index(disc_q, y) == null):
                disc_q + y
            j++
        proces_vertex_late(v)
        i++