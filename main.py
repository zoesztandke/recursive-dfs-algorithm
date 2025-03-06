from typing import Dict, Set, Union

def dfs(G: Dict[Union[int, str], Set[Union[int, str]]]) -> None:
    visited = {node: False for node in G}

    for v in G:
        if not visited[v]:
            dfs_from_vertex(G, v, visited)

def dfs_from_vertex(G, v, visited) -> None:
    visited[v] = True
    for w in v:
        if not visited[w]:
            dfs_from_vertex(G, w, visited)