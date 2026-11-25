# Roda 2: ORM/Restrict entendidos; lacunas em Singleton/Scoped, Change Tracker e Fluent API

Na Roda 2, Ramon associou corretamente ORM ao Hibernate (Java) e entendeu `DeleteBehavior.Restrict` (erro de integridade referencial ao apagar pai com filhos). Não conhecia os ciclos de vida de DI (`Scoped` vs `Singleton`), o Change Tracker do EF Core nem a divisão de uso entre Data Annotations e Fluent API.

## Evidence
- Acertou: ORM equivale ao Hibernate (Java) e resolve a ponte entre objetos e banco relacional.
- Acertou: `DeleteBehavior.Restrict` impede exclusão de `Category` com `Products` vinculados (erro de integridade).
- Lacuna: desconhecia `Singleton` (1 instância global) vs `Scoped` (1 por requisição HTTP) e os riscos de `DbContext` Singleton (concorrência/thread-safety e vazamento de memória).
- Lacuna: desconhecia os 5 estados do Change Tracker (`Detached`, `Unchanged`, `Added`, `Modified`, `Deleted`).
- Lacuna: desconhecia a regra didática do slide 35 (Data Annotations para DTOs/validação HTTP; Fluent API no `OnModelCreating` para schema e relacionamentos).

## Implications
- Lição 10 (`0010-orm-dbcontext-mapeamento.html`) criada para consolidar esses conceitos com tabela de estados e quiz.
- Seguir para Roda 3 (LINQ/`IQueryable`, `AsNoTracking`, N+1, Migrations e Transações).
