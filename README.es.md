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
- **Política de entorno y aislamiento** — dónde puede ejecutarse una ejecución y qué puede tocar (sistema de archivos, red, credenciales, efectos secundarios), separada de la aprobación. Véase [`docs/environment-and-sandbox-policy.md`](docs/environment-and-sandbox-policy.md).
- **Disciplina de árboles de trabajo y ramas** — el aislamiento del trabajo en curso para que los cambios humanos y de los agentes sigan siendo revisables. Véase [`docs/core-concepts.md`](docs/core-concepts.md).
- **Normas de verificación** — la evidencia por encima del acuerdo: pruebas, CI, revisiones, artefactos, reproducibilidad. Véase [`docs/verification-standards.md`](docs/verification-standards.md).
- **Gobernanza estricta de seguridad y ligera de estado** — los límites de seguridad se verifican con rigor, mientras que la evidencia de estado se mantiene concisa: roadmap, estado actual y registros de desarrollo documentan autoridad de fase, decisiones vigentes, colas abiertas y límites de seguridad, no contabilidad ya probada por historial de git, CI, metadatos de PR o artefactos generados. Véase [`docs/verification-standards.md`](docs/verification-standards.md).
- **Manifiesto de ejecución de agente** — un registro de auditoría por ejecución de qué se autorizó, qué se ejecutó realmente, y las evidencias y el límite implicados; un registro, no una autorización. Véase [`docs/agent-run-manifest.md`](docs/agent-run-manifest.md).
- **Plantillas** — puntos de partida listos para copiar en [`templates/`](templates/): el archivo de flujo local por sí solo y el conjunto inicial de proyecto completo, ambos componentes del mismo modelo de gobernanza de ciclo de vida completo.
- **Estructura de proyecto gobernado** — una cadena de autoridad documental más completa para repositorios maduros: `GOAL.md`, PRD, diseño, hoja de ruta/estado, seguimiento de funciones, planes de fase y `docs/AI_FLOW.md`. Véase [`docs/governed-project-structure.md`](docs/governed-project-structure.md).
- **Columna vertebral de conocimiento** — registros de desarrollo, lecciones, prácticas, índices generados solo para `docs/` e informes de deriva para repositorios gobernados: `docs/dev_log/`, `docs/lessons/`, `docs/practices/` y `tools/`. Cómo vive ese conocimiento, expira por uso y permanece subordinado a la cadena de autoridad se define en [`docs/knowledge-governance.md`](docs/knowledge-governance.md).
- **Conformidad y manifiesto de adopción** — qué puede afirmar un proyecto, declarado en un manifiesto de adopción legible por máquina ([`schemas/lithos-adoption-manifest.schema.json`](schemas/lithos-adoption-manifest.schema.json), rellenado a partir de [`templates/lithos-adoption-manifest.json`](templates/lithos-adoption-manifest.json)), con [fixtures de conformidad](fixtures/conformance/) que muestran qué pasa y qué debe fallar. Véase [`docs/conformance-and-fixtures.md`](docs/conformance-and-fixtures.md).
- **Política de PR autónoma** — qué puede hacer un agente con las pull requests por su cuenta, y qué nunca debe auto-aprobar ni auto-fusionar. Véase [`docs/autonomous-pr-policy.md`](docs/autonomous-pr-policy.md).
- **Escaneo estático de seguridad** — una puerta determinista que rechaza valores con forma de secreto, rutas locales privadas y marcadores de trabajo inacabado antes de la revisión o la publicación. Véase [`docs/static-safety-scan.md`](docs/static-safety-scan.md).
- **Gobernanza de regresión por escenarios** — fixtures nombradas que fijan afirmaciones y ejemplos con comportamiento para capturar regresiones de forma mecánica. Véase [`docs/scenario-regression-governance.md`](docs/scenario-regression-governance.md).
- **Gobernanza de lanzamiento y cadena de suministro** — aprobación del propietario, registros de procedencia y límites de publicación para artefactos distribuidos. Véase [`docs/release-and-supply-chain-governance.md`](docs/release-and-supply-chain-governance.md).
- **Interoperabilidad de herramientas** — los artefactos que portan el estado de colaboración son neutrales respecto al proveedor y portables, de modo que un proyecto puede cambiar de herramientas sin perder su gobernanza. Véase [`docs/tooling-interoperability.md`](docs/tooling-interoperability.md).
- **Gobernanza de README bilingües** — el README fuente y los README localizados se mantienen semánticamente alineados cuando cambian las afirmaciones visibles.
- **Habilidades** — procedimientos operativos reutilizables en [`skills/`](skills/): la única habilidad paraguas [`lithos`](skills/lithos/SKILL.md) dirige a un agente para adoptar, auditar, actualizar, revisar o aplicar el control de publicación de un proyecto, con un procedimiento por intención en [`skills/lithos/references/`](skills/lithos/references/).
- **Ejemplos** — una adopción trabajada del modelo de ciclo de vida completo en [`examples/`](examples/).

## Alcance — qué no es Lithos

Lithos es una **norma y un conjunto de herramientas de colaboración para el desarrollo de software**. **No** es un entorno de ejecución, un marco de agentes ni un producto de ejecución.

Adoptar Lithos **no** autoriza la ejecución autónoma ni en vivo de la IA. Su semántica de aprobación es *organizativa*: describe cuándo una persona ha sancionado una clase de trabajo, no la concesión de un permiso a la máquina. Toda acción en vivo, destructiva o visible externamente sigue requiriendo la aprobación explícita y contemporánea que defina el proyecto adoptante. Véase [`docs/approval-semantics.md`](docs/approval-semantics.md).

## Adopción rápida

1. Lea [`docs/philosophy.md`](docs/philosophy.md) y [`docs/core-concepts.md`](docs/core-concepts.md).
2. Decida dónde vivirán sus reglas de colaboración: elija su propio nombre de archivo de flujo local (p. ej. `AI_FLOW.md`, `ai-collaborative-development-standards.md`, o un nombre que encaje en su repositorio). Véase [`docs/local-adoption.md`](docs/local-adoption.md).
3. Copie un punto de partida — ambos son componentes del mismo modelo de ciclo de vida completo: [`templates/governed-ai-flow.md`](templates/governed-ai-flow.md) es el archivo de flujo local por sí solo, mantenido conciso; la estructura completa [`templates/governed-project/`](templates/governed-project/) despliega el mismo modelo de extremo a extremo con registros de desarrollo, lecciones, prácticas, índice generado, informe de deriva y reglas de README bilingües.
4. Añada el contrato [`templates/AGENTS.md.snippet`](templates/AGENTS.md.snippet) a su `AGENTS.md`.
5. Adopte [`templates/pr-checklist.md`](templates/pr-checklist.md) y las [normas de verificación](docs/verification-standards.md), y declare a qué se conforma en un [manifiesto de adopción](templates/lithos-adoption-manifest.json).

Un recorrido completo se encuentra en [`examples/governed-project/`](examples/governed-project/).

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
│   ├── environment-and-sandbox-policy.md
│   ├── local-adoption.md
│   ├── governed-project-structure.md
│   ├── verification-standards.md
│   ├── agent-run-manifest.md
│   ├── knowledge-governance.md
│   ├── conformance-and-fixtures.md
│   ├── tooling-interoperability.md
│   ├── autonomous-pr-policy.md
│   ├── static-safety-scan.md
│   ├── scenario-regression-governance.md
│   ├── release-and-supply-chain-governance.md
│   └── versioning-and-governance.md
├── schemas/                   Esquema de manifiesto de adopción legible por máquina
├── skills/                    Procedimientos operativos reutilizables
│   └── lithos/                Habilidad paraguas única: enruta adoptar / auditar / actualizar / revisar / publicar
│       └── references/        Un procedimiento por intención: adoptar, auditar, actualización gobernada, cambio de versión, revisión de PR, control de publicación
├── templates/                 Archivos de adopción local y estructura de proyecto gobernado listos para copiar
├── fixtures/                  Fixtures de conformidad (que pasan y que rechazan)
├── examples/                  Adopciones trabajadas
└── scripts/                   Verificación del repositorio (biblioteca estándar de Python)
```

## Gobernanza y versionado

Lithos se versiona y gobierna como una norma, no como una base de código cambiante. Véase [`docs/versioning-and-governance.md`](docs/versioning-and-governance.md) y [`AGENTS.md`](AGENTS.md).

## Licencia

Publicado bajo la [Licencia MIT](LICENSE).

Copyright (c) 2026 jovijovi and Lithos Contributors.
