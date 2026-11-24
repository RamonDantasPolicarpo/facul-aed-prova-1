# Ramon entendeu em-ordem e BFS com fila, mas precisa fixar pós-ordem e fórmula do grafo completo

Na Roda 2 (Kahoot 6), Ramon deduziu corretamente que o percurso em-ordem em ABB sai em ordem crescente, que pré-ordem começa pela raiz, que percurso por nível usa fila (`deque`), e que grafo simples não tem laço. Precisou de reforço na definição de pós-ordem e na fórmula de arestas do grafo completo ($V(V-1)/2$). Também pediu código Python completo com `class No` para conseguir acompanhar o raciocínio sem trechos soltos.

## Evidence
- Acertou: Em-ordem na ABB = crescente; Pré-ordem = raiz primeiro; Por nível = fila; Grafo simples sem laço = não.
- Não soube pós-ordem ("não faço ideia") e chutou `V*2-1` (9) para grafo completo de 5 vértices (correto: 10).
- Pediu código completo em Python (com a classe do nó e exemplo rodando), não apenas funções soltas.

## Implications
- Incluir sempre `class No` / exemplo completo nos blocos de código das lições.
- Fixar o macete Pré (antes) / Em (meio) / Pós (depois) para posição da raiz, mais reconstrução (pré + em + dicionário).
- Reforçar a fórmula de arestas do grafo completo $\frac{V(V-1)}{2}$ vs árvore ($V - 1$).
- Seguir para Roda 3 (Kahoot 7: Grafos, BFS vs DFS, Ordenação Topológica e Bipartido).
