from collections import deque

def bfs(grafo, inicio):
    fila = deque([inicio])
    visitados = {inicio}
    while fila:
        atual = fila.popleft()      # ← Fila: sai quem entrou primeiro!
        print(atual, end=" ")
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)