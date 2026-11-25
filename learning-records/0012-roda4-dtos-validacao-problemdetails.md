# Roda 4: DTOs e [ApiController] dominados; ajustes em 409 Conflict e Repository/UoW

Na Roda 4, Ramon acertou os motivos de usar DTOs, o bloqueio automático do `[ApiController]` antes do controller e o motivo de segurança para não vazar stack trace. Precisou apenas ajustar que `DbUpdateException` mapeia para `409 Conflict`, o papel exato do `GlobalExceptionHandler` (interceptar exceções inesperadas) e por que `DbContext` já atua como Repository (`DbSet<T>`) + Unit of Work (`SaveChangesAsync`).

## Evidence
- Acertou: DTOs protegem estrutura interna, evitam campos indesejados e reduzem payload (complemento: evitam ciclos de serialização JSON).
- Acertou: `[ApiController]` valida Data Annotations antes de entrar no método e retorna `400 Bad Request`.
- Acertou: não vazar stack trace protege detalhes internos; ajuste: `GlobalExceptionHandler` intercepta exceções não tratadas e mapeia `DbUpdateException` para `409 Conflict` (e `_` para `500`).
- Lacuna: desconhecia DAO, Repository e Unit of Work e a relação com `DbSet<T>` / `DbContext`.

## Implications
- Lição 12 (`0012-dtos-validacao-problemdetails-padroes.html`) criada.
- Folha de consulta rápida (`reference/consulta-prova-backend.html`) criada para revisão final até as 19h.
