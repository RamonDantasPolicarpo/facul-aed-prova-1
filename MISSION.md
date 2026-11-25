# Mission: Passar na Prova Teórica de Desenvolvimento Back-End

## Why
Ramon tem prova teórica HOJE (25/11/2026 às 19h) de Desenvolvimento Back-End (C# / .NET, Prof. Daniel Lim-Apo, CEUB). Ele precisa dominar os conceitos da Unidade 4 (ORM, Entity Framework Core, ASP.NET Core Web API, Validação, Transações) e os fundamentos anteriores (Web API com Minimal API vs Controllers, HTTP/REST e Hashing MD5/SHA-256).

## Success looks like
- Diferenciar Minimal API vs Controllers em ASP.NET Core Web API e explicar Injeção de Dependência (`Program.cs`) e verbos/status HTTP
- Explicar Hash criptográfico (unidirecional, integridade, efeito avalanche) e a diferença entre MD5 (inseguro, colisões) e SHA-256
- Explicar Impedância Objeto-Relacional e o papel do ORM (EF Core), `DbContext`, `DbSet<T>` e estados do Change Tracker (`Added`, `Modified`, `Deleted`, `Unchanged`, `Detached`)
- Explicar ciclo de vida do `DbContext` (`Scoped` por requisição HTTP vs `Singleton` e por que Singleton causa concorrência/vazamento)
- Diferenciar Convenções, Data Annotations e Fluent API (relacionamento 1:N, FK, `OnDelete`)
- Diferenciar `IQueryable` vs `IEnumerable` (filtro no banco vs memória), `Select` (evitar overfetching), `AsNoTracking()` e `Include()` (Eager vs Lazy Loading e problema N+1)
- Explicar Migrations (`dotnet ef migrations add` / `database update`, `__EFMigrationsHistory`)
- Diferenciar transação implícita (`SaveChangesAsync`) de explícita (`BeginTransactionAsync`, `Commit`, `Rollback`)
- Explicar por que usar DTOs (evitar ciclos JSON, acoplamento e overfetching), validação automática (`[ApiController]`), `ProblemDetails` (400/404/409/500) e `IExceptionHandler`

## Constraints
- ~2h05 de estudo (16:52 – 19:00)
- Prova teórica em C# / .NET (foco em conceitos e interpretação de código, não em decorar boilerplate)
- Já programa em Java; referências a Java (JPA/Hibernate, `@RestController`, Streams, `@ControllerAdvice`) ajudam a ancorar conceitos
- Preferência por roda de perguntas no chat + lições HTML interativas + folha de cola rápida

## Out of scope
- Implementação prática completa do projeto `LojaApi` do zero ou configuração de ambiente `.NET` local
