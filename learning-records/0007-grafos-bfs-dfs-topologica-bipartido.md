# Ramon acertou quase todo o Kahoot 7 por intuição e consolidou BFS/DFS, topológica e bipartido

Na Roda 3 (Kahoot 7), Ramon acertou $V-1$ arestas em árvore, grafo não direcionado, pesos nas arestas, grau 0 para nó isolado, BFS para menor rota, DFS para ciclos e dependência circular impedindo ordenação topológica. Precisou apenas ajustar o *porquê* da BFS (exploração por níveis, não busca binária) e o conceito de grafo bipartido (dois grupos disjuntos sem arestas internas).

## Evidence
- Acertou: árvore com 5 e 15 vértices → 4 e 14 ($V - 1$).
- Acertou: amizade mútua → grafo não direcionado; pedágios → pesos nas arestas; isolado → grau 0.
- Acertou BFS (menor rota) e DFS (ciclos), mas achou que BFS ordenava para busca binária (correto: explora por níveis usando fila).
- Acertou que ciclo impede ordenação topológica por voltar ao início (dependência circular).
- Chutou "duas raízes" para grafo bipartido (correto: dois grupos disjuntos de vértices).

## Implications
- Lição 08 (`0008-grafos-bfs-dfs-topologica.html`) criada para consolidar os conceitos de Kahoot 7 com quiz interativo.
- Folha de consulta rápida (`reference/consulta-prova-2-arvores-grafos.html`) criada para revisão final nos minutos antes da prova às 19h.
