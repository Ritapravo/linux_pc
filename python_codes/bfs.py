def bfs(graph, v):
    n = len(graph)
    vis = [False]*n
    traversal = []
    st = []
    st.append(v)
    vis[v-1]=True
    while(st!=[]):
        v = st.pop(0)
        traversal.append(v)
        for i in graph[v-1]:
            if(not vis[i-1]):
                st.append(i)
                vis[i-1] = True
    return traversal


if __name__=="__main__":
    graph = [[2, 3] ,[1, 4, 5] ,[1, 6, 7] ,[8, 2] ,[8, 2] ,[8, 3] ,[8, 3] ,[4, 5, 6, 7]];
    bfs_visit = bfs(graph, 2)
    print(bfs_visit)