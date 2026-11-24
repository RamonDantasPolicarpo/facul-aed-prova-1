# Ramon domina anatomia básica de árvore e relação árvore-grafo, mas precisa construir ABB do zero

Na Roda 1 da preparação para a Prova 2, Ramon respondeu corretamente à definição de aresta, folha e profundidade, e já trouxe por pesquisa própria a relação exata entre árvore e grafo (grafo conexo sem ciclos). Porém, ainda não viu como funciona a regra de inserção na Árvore Binária de Busca (ABB) nem o impacto de entradas ordenadas na altura (árvore degenerada).

## Evidence
- Definiu corretamente: aresta = conexão entre nós; folha = nó sem filhos; profundidade = número de arestas da raiz até o nó.
- Acertou que toda árvore é um grafo em que todos os vértices são alcançáveis e sem ciclo.
- Não soube diferenciar lista vs árvore (linear vs hierárquica) nem rastrear inserção em ABB (`8, 3, 10, 1, 6, 14`) ou explicar árvore degenerada.

## Implications
- Explicar Lista (linear) vs Árvore (hierárquica) de forma direta.
- Ensinar a regra da ABB (`esquerda < raiz < direita`) com diagrama visual e passo a passo.
- Mostrar visualmente a árvore degenerada quando os dados chegam ordenados (`O(N)` vs `O(log N)`).
- Avançar em seguida para Kahoot 6 (Percursos e Reconstrução).
