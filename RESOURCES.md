# Algoritmos e Estrutura de Dados — Resources

## Knowledge

- [Docs Python: Listas como Pilhas e Filas](https://docs.python.org/pt-br/3/tutorial/datastructures.html#using-lists-as-stacks)
  Documentação oficial Python em PT-BR. Explica como usar listas como pilhas e filas. Use para: entender append/pop e a recomendação de usar deque.

- [Docs Python: collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)
  Referência oficial do deque. Use para: entender todos os métodos disponíveis e por que é O(1) nas duas pontas (usado em BFS / percurso por nível).

- [Docs Python: heapq](https://docs.python.org/3/library/heapq.html)
  Referência oficial da heap. Use para: entender min-heap, heappush, heappop e o truque de negar valores para max-heap.

- [Docs Python: bisect](https://docs.python.org/3/library/bisect.html)
  Referência oficial do bisect. Use para: entender bisect_left vs bisect_right e inserção em lista ordenada.

- [IME-USP: Árvores Binárias de Busca](https://www.ime.usp.br/~pf/algoritmos/aulas/binst.html)
  Material clássico do Prof. Paulo Feofiloff (USP) em português. Use para: definições formais de ABB, busca, inserção e percursos.

- [IME-USP: Grafos e Buscas (BFS / DFS)](https://www.ime.usp.br/~pf/algoritmos_para_grafos/)
  Referência acadêmica em PT-BR sobre grafos, árvores como grafos acíclicos conexos, BFS, DFS e ordenação topológica.

- [VisuAlgo: Binary Search Tree & Graph Traversal](https://visualgo.net/en/bst)
  Visualizador interativo de ABB e grafos. Use para: ver inserções, percursos e degeneração acontecendo passo a passo.

## Wisdom (Communities)

- Comunidade da sala de aula / WhatsApp da turma do CEUB
  Use para: tirar dúvidas com colegas sobre o formato da prova e tópicos do professor.

## Gaps

- Não encontrei recurso de alta qualidade em PT-BR específico sobre Insertion Sort com Python. A lição 04 cobre o tópico diretamente.

---

# Desenvolvimento Back-End (C# / .NET) — Resources

## Knowledge

- [Microsoft Learn: Visão geral do Entity Framework Core](https://learn.microsoft.com/pt-br/ef/core/)
  Documentação oficial em PT-BR do EF Core. Use para: entender `DbContext`, `DbSet<T>`, Change Tracker, mapeamento e provedores.

- [Microsoft Learn: Tempo de vida e configuração do DbContext](https://learn.microsoft.com/pt-br/ef/core/dbcontext-configuration/)
  Referência oficial sobre `Scoped` vs `Singleton`, thread-safety e descarte automático via injeção de dependência.

- [Microsoft Learn: Consultas com e sem rastreamento (AsNoTracking)](https://learn.microsoft.com/pt-br/ef/core/querying/tracking)
  Explica quando usar `AsNoTracking()` para leitura, como o Change Tracker funciona e impacto em memória/performance.

- [Microsoft Learn: Carregamento de dados relacionados (Eager vs Lazy)](https://learn.microsoft.com/pt-br/ef/core/querying/related-data/)
  Referência sobre `Include()` / `ThenInclude()`, Lazy Loading e como evitar o problema de consultas N+1.

- [Microsoft Learn: Visão geral das Migrations do EF Core](https://learn.microsoft.com/pt-br/ef/core/managing-schemas/migrations/)
  Explica `dotnet ef migrations add`, `database update`, snapshot e a tabela `__EFMigrationsHistory`.

- [Microsoft Learn: Criar APIs Web com ASP.NET Core (Controllers e Validação)](https://learn.microsoft.com/pt-br/aspnet/core/web-api/)
  Documentação oficial sobre `[ApiController]`, validação automática com Data Annotations e retorno padronizado com `ProblemDetails` / `ValidationProblemDetails`.

- [MDN / Conceitos de Hash Criptográfico (MD5 vs SHA-256)](https://learn.microsoft.com/pt-br/dotnet/standard/security/cryptographic-services)
  Serviços criptográficos no .NET: diferença entre hash (unidirecional, integridade) e criptografia, e por que SHA-256 substituiu MD5.
