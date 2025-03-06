from typing import Dict, Set, Union

def dfs(G: Dict[Union[int, str], Set[Union[int, str]]]) -> None:
    """
    Depth-first search on a graph G - recursive implementation
    :param G: a graph G
    :return: none
    """
    visited = {node: False for node in G} # set all nodes to unvisited initially

    for v in G: # for vertex in G
        if not visited[v]: # if vertex is not visited
            dfs_from_vertex(G, v, visited) # call dfs from that vertex

def dfs_from_vertex(G: Dict[Union[int, str], Set[Union[int, str]]], v: Union[int, str], visited: Dict[Union[int, str], bool]) -> None:
    """
    Depth-first search from vertex v
    :param G: a graph G
    :param v: starting vertex v
    :param visited: a list of states for the vertices
    :return: none
    """
    visited[v] = True # mark vertex as visited

    for w in v: # for each vertex w adjacent to v
        if not visited[w]: # if w is not visited
            dfs_from_vertex(G, w, visited) # call dfs from w