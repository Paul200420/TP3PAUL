def add_edge(graph, node1, node2):
    """
    Ajoute une arête entre deux nœuds dans un graphe.

    Args:
        graph (dict): Graphe sous forme de dictionnaire d'adjacence.
        node1 (str): Nom du premier nœud.
        node2 (str): Nom du second nœud.

    Returns:
        None
    """
    graph[node1].append(node2)
