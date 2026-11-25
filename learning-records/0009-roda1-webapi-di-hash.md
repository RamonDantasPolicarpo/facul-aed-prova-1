# Roda 1: Hash consolidado; ajustes em Controllers, Status Codes e DI

Na Roda 1, Ramon demonstrou domínio sólido de Hash vs Criptografia e MD5/SHA-256/bcrypt/Argon2id. Precisou ajustar a diferença entre Minimal API e Controllers, o status HTTP de criação (`201 Created` vs `200 OK`) e de validação (`400 Bad Request` vs `401`), além do conceito de Injeção de Dependência (DI).

## Evidence
- Acertou: Hash é mão única (irreversível) e criptografia é mão dupla com chave/secret.
- Acertou: MD5 é inseguro/rápido; para senhas usam-se bcrypt/Argon2id com work factor. Reforço: MD5 sofre de **colisões** (128 bits), enquanto SHA-256 (256 bits) continua seguro para **integridade**.
- Confundiu Minimal API vs Controllers com "atomicidade" (correto: organização/separação de responsabilidades — rotas soltas no `Program.cs` vs classes Controller dedicadas).
- Acertou `404 Not Found`; disse `200 OK` para `POST` de criação (padrão REST: `201 Created`) e hesitou entre `401` e `400` para erro de validação (correto: `400 Bad Request`, pois `401` é não autenticado).
- Não conhecia o papel do container de DI (`AddDbContext`): desacoplamento + gerenciamento automático do ciclo de vida (`Scoped`) e descarte de recursos.

## Implications
- Ancorar `AddDbContext` (`Scoped`) na próxima roda explicando o risco de `Singleton`.
- Incluir tabela de Status Codes HTTP (200, 201, 204, 400, 401, 404, 409, 500) na folha de cola e lição HTML.
