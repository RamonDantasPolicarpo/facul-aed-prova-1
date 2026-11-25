# Roda 3: IQueryable, Eager Loading e Atomicidade bem compreendidos; ajuste em N+1 (51) e AsNoTracking

Na Roda 3, Ramon acertou a diferença entre filtrar no banco (`Where` antes de `ToListAsync`) vs na memória, entendeu a ideia de Eager Loading (`Include`) e a necessidade de transação explícita (atomicidade/tudo ou nada). Precisou apenas ajustar a contagem exata do N+1 (`1 + N = 51`), o conceito exato de `AsNoTracking()` (desligar Change Tracker em leituras) e os nomes específicos das migrations (`Up`/`Down`, `__EFMigrationsHistory`).

## Evidence
- Acertou: `Where` antes de `ToListAsync` filtra no banco (`IQueryable`); depois filtra em memória.
- Chutou próximo: `AsNoTracking()` é para leituras que não serão modificadas (desativa Change Tracker); em `PUT`/`DELETE` precisa do rastreamento.
- Quase acertou N+1: disse 50 consultas (faltou somar a +1 consulta inicial dos 50 pedidos = 51); acertou que Eager Loading (`Include`) resolve em 1 consulta.
- Entendeu o objetivo das migrations; precisa fixar `Up()`/`Down()` e `__EFMigrationsHistory`.
- Acertou a lógica de transação explícita: atomicidade entre múltiplos `SaveChangesAsync()` (`BeginTransactionAsync` + `CommitAsync`/`RollbackAsync`).

## Implications
- Lição 11 (`0011-linq-n1-migrations-transacoes.html`) criada para consolidar esses tópicos.
- Seguir para Roda 4 (DTOs, Validação automática, `ProblemDetails`, `GlobalExceptionHandler` e Repository/UoW).
