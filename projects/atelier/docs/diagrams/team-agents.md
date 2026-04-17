# Team Organisation — AI Product Agents
**Atelier — Rôles, responsabilités et interactions**
Last updated: 2026-04-17 (role: Product Owner → Product Builder)

## Organisation générale

```mermaid
flowchart TD
    HUMAN(["👤 Product Builder\n(Human)"])

    subgraph TEAM ["🏢 AI Product Team"]
        direction TB

        LEAD["🧑‍💼 product-lead\nOrchestrator"]

        subgraph CRAFT ["Craft agents"]
            DESIGN["🎨 product-design\nDesign & UX"]
            TECH["⚙️ product-tech\nEngineering"]
        end
    end

    subgraph MEMORY ["🧠 Memory (Tier 1 — Git)"]
        direction LR
        CTX["context.md"]
        BKL["backlog.yaml"]
        SESS["sessions.md"]
        DEC["decisions.md"]
    end

    subgraph TIER2 ["🧠 Memory (Tier 2 — shared)"]
        direction LR
        ML["agent-memory/\nproduct-lead.md"]
        MD["agent-memory/\nproduct-design.md"]
        MT["agent-memory/\nproduct-tech.md"]
    end

    subgraph GITHUB ["📋 GitHub"]
        ISSUES["Issues / Kanban"]
    end

    HUMAN -->|"Requirements\nValidations\nDecisions"| LEAD
    LEAD -->|"User stories\nAcceptance criteria\nPriority"| DESIGN
    LEAD -->|"User stories\nAcceptance criteria\nPriority"| TECH
    DESIGN -->|"Mockups\nSpecs\nTokens"| TECH
    DESIGN -->|"Deliverable for validation"| LEAD
    TECH -->|"Feasibility assessment\nImplementation"| LEAD
    TECH -->|"Implementation for review"| DESIGN
    LEAD -->|"Decisions\nArbitration"| HUMAN

    LEAD <-->|"Read/Write"| BKL
    LEAD <-->|"Read/Write"| DEC
    LEAD <-->|"Write"| SESS
    DESIGN <-->|"Read/Write"| CTX
    TECH <-->|"Read/Write"| CTX

    LEAD -->|"sync_github_issues"| ISSUES
    TECH -->|"on_story_started\non_story_completed"| ISSUES

    LEAD -.->|"Cross-project patterns"| ML
    DESIGN -.->|"Cross-project patterns"| MD
    TECH -.->|"Cross-project patterns"| MT

    style HUMAN fill:#dbeafe,stroke:#3b82f6
    style LEAD fill:#fef3c7,stroke:#f59e0b
    style DESIGN fill:#fce7f3,stroke:#ec4899
    style TECH fill:#ecfdf5,stroke:#10b981
```

## Responsabilités par agent

```mermaid
mindmap
  root((AI Product Team))
    product-lead 🧑‍💼
      Décompose les requirements
      Priorise le backlog
      Définit les acceptance criteria
      Lance les spikes de discovery
      Arbitre les conflits Design ↔ Tech
      Valide les livrables
      Met à jour roadmap + changelog
      Synchronise GitHub issues
    product-design 🎨
      Direction esthétique
      User journey maps
      Mockup specs état par état
      Motion specs
      Design system tokens + composants
      Audit accessibilité WCAG AA
      Review implémentation vs specs
    product-tech ⚙️
      Évalue la faisabilité
      Implémente les features
      Écrit les tests unitaires + e2e
      Review de code
      Gère les déploiements
      Documente techniquement
      Met à jour le statut GitHub
```

## Cycle de vie d'une user story

```mermaid
sequenceDiagram
    actor H as 👤 Product Builder
    participant L as 🧑‍💼 Lead
    participant D as 🎨 Design
    participant T as ⚙️ Tech
    participant G as 📋 GitHub

    H->>L: Requirement
    L->>L: decompose_requirement
    L->>G: Create issue [US-XXX]
    L->>D: User story + acceptance criteria
    L->>T: Story (feasibility check)

    T->>L: Feasibility assessment
    L->>D: Go — design the story

    D->>D: mockup_spec + motion_spec
    D->>L: Mockup for validation
    L->>D: Approved ✅

    D->>T: Full spec package
    T->>G: Update issue → status: in-progress
    T->>T: implement + test + review
    T->>D: Implementation for visual review
    D->>T: Visual review ✅
    T->>L: Implementation for validation
    L->>T: Approved ✅

    T->>T: deploy to staging → production
    T->>G: Close issue ✅
    T->>L: Shipped
    L->>H: Story delivered
```

## Skills disponibles

```mermaid
flowchart LR
    subgraph SKILLS ["⚡ Slash commands"]
        SS["/session-start\n[project]\nCharge le contexte\nen début de session"]
        SE["/session-end\n[project]\nÉcrit mémoire\ncommit + push"]
        SR["/spike-results\n[project] [id]\nCapture résultats\nmaj backlog + GitHub"]
    end

    SS -->|"loads"| CTX2["context.md\nsessions.md\ndecisions.md\nbacklog.yaml"]
    SE -->|"writes"| MEM["sessions.md\ndecisions.md\nagent-memory/"]
    SR -->|"updates"| BKL2["backlog.yaml\nexperiments/\nGitHub issues"]
```
