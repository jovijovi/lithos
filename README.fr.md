<div align="center">

<img src="assets/lithos-logo-horizontal.png" alt="Lithos" width="420" />

### Normes de développement logiciel en collaboration avec l'IA

*Inscrire la manière dont les humains et l'IA construisent le logiciel ensemble.*

[English](README.md) · [中文](README.zh-CN.md) · [Français](README.fr.md) · [Русский](README.ru.md) · [Español](README.es.md)

</div>

---

## Ce qu'est Lithos

Lithos est une norme ouverte décrivant **la manière dont les humains et l'IA collaborent sur le logiciel**. Elle définit les rôles, les frontières d'approbation, la discipline de travail et les preuves qu'un projet doit attendre lorsque des personnes et des agents construisent du logiciel ensemble — sans imposer d'outil, de fournisseur ni d'environnement d'exécution particulier.

Elle existe parce que le développement assisté par l'IA est désormais courant, alors que les *règles d'engagement* restent le plus souvent improvisées. Lithos rend ces règles explicites, révisables et transférables entre équipes.

Lithos se lit sur trois plans :

1. **Marque — Lithos.** Un nom et une identité stables pour la norme, afin qu'un projet puisse dire « nous suivons Lithos » avec un sens précis.
2. **Norme formelle — *Normes de développement logiciel en collaboration avec l'IA*.** Les documents normatifs de [`docs/`](docs/) : rôles, sémantique d'approbation, vérification, gouvernance. Ils sont rédigés pour être cités.
3. **Forme d'adoption locale.** La manière dont un dépôt adopte concrètement la norme : un fichier de flux de travail local (dont le projet choisit le nom), un contrat `AGENTS.md`, une liste de contrôle de PR, ainsi que les modèles et compétences qui rendent la norme opérationnelle au quotidien.

## Ce que Lithos définit

- **Rôles** — un ensemble générique (propriétaire, contrôleur/opérateur, architecte, agent d'implémentation, relecteur, vérificateur) aux frontières d'autorité claires. Voir [`docs/roles.md`](docs/roles.md).
- **Sémantique d'approbation** — des seuils distincts pour la préparation/le contrôle préalable, l'implémentation, les effets destructifs ou externes, et l'exécution en direct/au runtime. Voir [`docs/approval-semantics.md`](docs/approval-semantics.md).
- **Politique d'environnement et de bac à sable** — où un run peut s'exécuter et ce qu'il peut toucher (système de fichiers, réseau, identifiants, effets de bord), distincte de l'approbation. Voir [`docs/environment-and-sandbox-policy.md`](docs/environment-and-sandbox-policy.md).
- **Discipline des arbres de travail et des branches** — l'isolation du travail en cours afin que les changements humains et agentiques restent révisables. Voir [`docs/core-concepts.md`](docs/core-concepts.md).
- **Normes de vérification** — la preuve avant l'assentiment : tests, CI, relectures, artefacts, reproductibilité. Voir [`docs/verification-standards.md`](docs/verification-standards.md).
- **Manifeste d'exécution d'agent** — un enregistrement d'audit par run de ce qui a été autorisé, de ce qui s'est réellement exécuté, ainsi que des preuves et de la frontière en jeu ; un enregistrement, non une autorisation. Voir [`docs/agent-run-manifest.md`](docs/agent-run-manifest.md).
- **Modèles** — des fichiers de flux local prêts à copier dans [`templates/`](templates/), pour une adoption en flux seul ou pleinement gouvernée.
- **Structure de projet gouverné** — une chaîne d'autorité documentaire plus complète pour les dépôts matures : `GOAL.md`, PRD, conception, feuille de route/statut, suivi des fonctionnalités, plans de phase et `docs/AI_FLOW.md`. Voir [`docs/governed-project-structure.md`](docs/governed-project-structure.md).
- **Colonne vertébrale de connaissance** — journaux de développement, leçons, pratiques, index générés limités à `docs/` et rapports de dérive pour les dépôts gouvernés : `docs/dev_log/`, `docs/lessons/`, `docs/practices/` et `tools/`. La manière dont cette connaissance vit, expire par l'usage et reste subordonnée à la chaîne d'autorité est définie dans [`docs/knowledge-governance.md`](docs/knowledge-governance.md).
- **Conformité et manifeste d'adoption** — ce qu'un projet peut revendiquer, déclaré dans un manifeste d'adoption lisible par machine ([`schemas/lithos-adoption-manifest.schema.json`](schemas/lithos-adoption-manifest.schema.json), rempli à partir de [`templates/lithos-adoption-manifest.json`](templates/lithos-adoption-manifest.json)), avec des [fixtures de conformité](fixtures/conformance/) montrant ce qui passe et ce qui doit échouer. Voir [`docs/conformance-and-fixtures.md`](docs/conformance-and-fixtures.md).
- **Politique de PR autonome** — ce qu'un agent peut faire seul avec les pull requests, et ce qu'il ne doit jamais auto-approuver ni auto-fusionner. Voir [`docs/autonomous-pr-policy.md`](docs/autonomous-pr-policy.md).
- **Interopérabilité des outils** — les artefacts qui portent l'état de collaboration sont neutres vis-à-vis des fournisseurs et portables, de sorte qu'un projet peut changer d'outils sans perdre sa gouvernance. Voir [`docs/tooling-interoperability.md`](docs/tooling-interoperability.md).
- **Gouvernance des README bilingues** — le README source et les README localisés restent sémantiquement alignés lorsque les affirmations visibles changent.
- **Compétences** — des procédures opérationnelles réutilisables dans [`skills/`](skills/) pour créer, auditer et adapter un flux IA local.
- **Exemples** — une adoption gouvernée concrète dans [`examples/`](examples/).

## Portée — ce que Lithos n'est pas

Lithos est une **norme et une boîte à outils de collaboration pour le développement logiciel**. Ce n'est **pas** un environnement d'exécution, un cadre d'agents ni un produit d'exécution.

Adopter Lithos **n'autorise pas** l'exécution autonome ou en direct d'une IA. Sa sémantique d'approbation est *organisationnelle* — elle décrit le moment où un humain a sanctionné une catégorie de travail, et non l'octroi d'une permission machine. Toute action en direct, destructive ou visible de l'extérieur requiert toujours l'approbation explicite et contemporaine définie par le projet adoptant. Voir [`docs/approval-semantics.md`](docs/approval-semantics.md).

## Adoption rapide

1. Lire [`docs/philosophy.md`](docs/philosophy.md) et [`docs/core-concepts.md`](docs/core-concepts.md).
2. Choisir où vivront vos règles de collaboration — sélectionnez votre propre nom de fichier de flux local (par ex. `AI_FLOW.md`, `ai-collaborative-development-standards.md`, ou un nom adapté à votre dépôt). Voir [`docs/local-adoption.md`](docs/local-adoption.md).
3. Copier un point de départ : [`templates/governed-ai-flow.md`](templates/governed-ai-flow.md) pour une relecture formelle en flux seul, ou la structure complète [`templates/governed-project/`](templates/governed-project/) pour un dépôt gouverné mature avec journaux de développement, leçons, pratiques, index généré, rapport de dérive et règles de README bilingues.
4. Ajouter le contrat [`templates/AGENTS.md.snippet`](templates/AGENTS.md.snippet) à votre `AGENTS.md`.
5. Adopter [`templates/pr-checklist.md`](templates/pr-checklist.md) et les [normes de vérification](docs/verification-standards.md), et déclarer ce à quoi vous vous conformez dans un [manifeste d'adoption](templates/lithos-adoption-manifest.json).

Une démonstration complète se trouve dans [`examples/governed-project/`](examples/governed-project/).

## Carte du dépôt

```
.
├── README.md                  Page d'accueil canonique (en anglais)
├── README.<lang>.md           Pages d'accueil localisées
├── LICENSE                    MIT
├── AGENTS.md                  Comment les agents contribuent à ce dépôt
├── docs/                      La norme formelle (normative)
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
│   └── versioning-and-governance.md
├── schemas/                   Schéma de manifeste d'adoption lisible par machine
├── skills/                    Procédures opérationnelles réutilisables
│   ├── create-local-ai-flow/
│   ├── audit-local-ai-flow/
│   └── adapt-ai-flow-for-governed-project/
├── templates/                 Fichiers d'adoption locale et structure de projet gouverné prêts à copier
├── fixtures/                  Fixtures de conformité (passantes et rejetantes)
├── examples/                  Adoptions concrètes
└── scripts/                   Vérification du dépôt (Python, bibliothèque standard)
```

## Gouvernance et versionnage

Lithos est versionné et gouverné en tant que norme, et non en tant que base de code mouvante. Voir [`docs/versioning-and-governance.md`](docs/versioning-and-governance.md) et [`AGENTS.md`](AGENTS.md).

## Licence

Publié sous [licence MIT](LICENSE).

Copyright (c) 2026 jovijovi and Lithos Contributors.
