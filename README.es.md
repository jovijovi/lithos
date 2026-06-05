<div align="center">

<img src="assets/lithos-logo-horizontal.png" alt="Lithos" width="420" />

### Normas de desarrollo de software en colaboración con la IA

*Inscribir cómo los humanos y la IA construyen software juntos.*

[English](README.md) · [中文](README.zh-CN.md) · [Français](README.fr.md) · [Русский](README.ru.md) · [Español](README.es.md)

</div>

---

## Qué es Lithos

Lithos es una norma abierta sobre **cómo los humanos y la IA colaboran en el software**. Define los roles, los límites de aprobación, la disciplina de trabajo y las evidencias que un proyecto debe esperar cuando personas y agentes construyen software juntos, sin imponer ninguna herramienta, proveedor ni entorno de ejecución concreto.

Existe porque el desarrollo asistido por IA ya es habitual, mientras que las *reglas de actuación* suelen seguir siendo improvisadas. Lithos hace que esas reglas sean explícitas, revisables y transferibles entre equipos.

Lithos se lee en tres planos:

1. **Marca — Lithos.** Un nombre y una identidad estables para la norma, de modo que un proyecto pueda decir «seguimos Lithos» con un significado preciso.
2. **Norma formal — *Normas de desarrollo de software en colaboración con la IA*.** Los documentos normativos de [`docs/`](docs/): roles, semántica de aprobación, verificación, gobernanza. Están redactados para ser citados.
3. **Forma de adopción local.** Cómo un repositorio concreto adopta realmente la norma: un archivo de flujo de trabajo local (cuyo nombre elige el proyecto), un contrato `AGENTS.md`, una lista de verificación de PR, y las plantillas y habilidades que hacen operativa la norma en el día a día.

## Qué define Lithos

- **Roles** — un reparto genérico (propietario, controlador/operador, arquitecto, agente de implementación, revisor, verificador) con límites de autoridad claros. Véase [`docs/roles.md`](docs/roles.md).
- **Semántica de aprobación** — umbrales distintos para la preparación/comprobación previa, la implementación, los efectos destructivos o externos, y la ejecución en vivo/en tiempo de ejecución. Véase [`docs/approval-semantics.md`](docs/approval-semantics.md).
- **Disciplina de árboles de trabajo y ramas** — el aislamiento del trabajo en curso para que los cambios humanos y de los agentes sigan siendo revisables. Véase [`docs/core-concepts.md`](docs/core-concepts.md).
- **Normas de verificación** — la evidencia por encima del acuerdo: pruebas, CI, revisiones, artefactos, reproducibilidad. Véase [`docs/verification-standards.md`](docs/verification-standards.md).
- **Plantillas** — archivos de flujo local listos para copiar en [`templates/`](templates/), mínimo y gobernado.
- **Estructura de proyecto gobernado** — una cadena de autoridad documental más completa para repositorios maduros: `GOAL.md`, PRD, diseño, hoja de ruta/estado, seguimiento de funciones, planes de fase y `docs/AI_FLOW.md`. Véase [`docs/governed-project-structure.md`](docs/governed-project-structure.md).
- **Columna vertebral de conocimiento** — registros de desarrollo, lecciones, prácticas, índices generados solo para `docs/` e informes de deriva para repositorios gobernados: `docs/dev_log/`, `docs/lessons/`, `docs/practices/` y `tools/`.
- **Gobernanza de README bilingües** — el README fuente y los README localizados se mantienen semánticamente alineados cuando cambian las afirmaciones visibles.
- **Habilidades** — procedimientos operativos reutilizables en [`skills/`](skills/) para crear, auditar y adaptar un flujo de IA local.
- **Ejemplos** — adopciones trabajadas en [`examples/`](examples/), desde un único colaborador hasta un proyecto gobernado.

## Alcance — qué no es Lithos

Lithos es una **norma y un conjunto de herramientas de colaboración para el desarrollo de software**. **No** es un entorno de ejecución, un marco de agentes ni un producto de ejecución.

Adoptar Lithos **no** autoriza la ejecución autónoma ni en vivo de la IA. Su semántica de aprobación es *organizativa*: describe cuándo una persona ha sancionado una clase de trabajo, no la concesión de un permiso a la máquina. Toda acción en vivo, destructiva o visible externamente sigue requiriendo la aprobación explícita y contemporánea que defina el proyecto adoptante. Véase [`docs/approval-semantics.md`](docs/approval-semantics.md).

## Adopción rápida

1. Lea [`docs/philosophy.md`](docs/philosophy.md) y [`docs/core-concepts.md`](docs/core-concepts.md).
2. Decida dónde vivirán sus reglas de colaboración: elija su propio nombre de archivo de flujo local (p. ej. `AI_FLOW.md`, `ai-collaborative-development-standards.md`, o un nombre que encaje en su repositorio). Véase [`docs/local-adoption.md`](docs/local-adoption.md).
3. Copie un punto de partida: [`templates/minimal-ai-flow.md`](templates/minimal-ai-flow.md) para un proyecto pequeño, [`templates/governed-ai-flow.md`](templates/governed-ai-flow.md) para uno con revisión formal, o la estructura completa [`templates/governed-project/`](templates/governed-project/) para un repositorio gobernado maduro con registros de desarrollo, lecciones, prácticas, índice generado, informe de deriva y reglas de README bilingües.
4. Añada el contrato [`templates/AGENTS.md.snippet`](templates/AGENTS.md.snippet) a su `AGENTS.md`.
5. Adopte [`templates/pr-checklist.md`](templates/pr-checklist.md) y las [normas de verificación](docs/verification-standards.md).

Un recorrido completo se encuentra en [`examples/minimal-project/`](examples/minimal-project/) y [`examples/governed-project/`](examples/governed-project/).

## Mapa del repositorio

```
.
├── README.md                  Página de inicio canónica (en inglés)
├── README.<lang>.md           Páginas de inicio localizadas
├── LICENSE                    MIT
├── AGENTS.md                  Cómo contribuyen los agentes a este repositorio
├── docs/                      La norma formal (normativa)
│   ├── philosophy.md
│   ├── core-concepts.md
│   ├── roles.md
│   ├── approval-semantics.md
│   ├── local-adoption.md
│   ├── governed-project-structure.md
│   ├── verification-standards.md
│   └── versioning-and-governance.md
├── skills/                    Procedimientos operativos reutilizables
│   ├── create-local-ai-flow/
│   ├── audit-local-ai-flow/
│   └── adapt-ai-flow-for-governed-project/
├── templates/                 Archivos de adopción local y estructura de proyecto gobernado listos para copiar
├── examples/                  Adopciones trabajadas
└── scripts/                   Verificación del repositorio (biblioteca estándar de Python)
```

## Gobernanza y versionado

Lithos se versiona y gobierna como una norma, no como una base de código cambiante. Véase [`docs/versioning-and-governance.md`](docs/versioning-and-governance.md) y [`AGENTS.md`](AGENTS.md).

## Licencia

Publicado bajo la [Licencia MIT](LICENSE).

Copyright (c) 2026 jovijovi and Lithos Contributors.
