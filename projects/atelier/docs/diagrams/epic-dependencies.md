# Epic & Story Dependencies
**Atelier — Full backlog map**
Last updated: 2026-04-17

```mermaid
flowchart TD

    subgraph DISC ["🔬 Discovery (gates)"]
        SP1["SPIKE-001\nAI feasibility\n🔴 Critical"]
        SP2["SPIKE-002\nLegal & API review\n🔴 Critical"]
        D1["DISC-001\nOnboarding research\n⏸ Deferred"]
    end

    subgraph WARDROBE ["👗 Epic 1 — Wardrobe core"]
        US001["US-001\nAdd via camera\n🔴 Critical"]
        US060["US-060\nMandatory size capture\n🔴 Critical"]
        US002["US-002\nAdd via upload\n🔴 Critical"]
        US003["US-003\nWardrobe grid\n🔴 Critical"]
        US004["US-004\nEdit garment details\n🟠 High"]
    end

    subgraph SCAN ["📷 Epic 2 — Scan"]
        US010["US-010\nScan → identify → products\n🔴 Critical\n⚠️ Blocked"]
        US011["US-011\nSave to wishlist\n🟠 High"]
        US032["US-032\nInspiration scan → wishlist\n🟠 High"]
    end

    subgraph LOOKS ["✨ Epic 3 — Looks"]
        US020["US-020\nCreate a look\n🔴 Critical"]
        US021["US-021\nBrowse looks\n🔴 Critical"]
    end

    subgraph PROFILES ["👤 Epic 4 — Profiles"]
        US030["US-030\nPublic profile\n🟠 High"]
        US031["US-031\nLike → wishlist\n🟠 High"]
    end

    subgraph AGENT ["💬 Epic 5 — AI Agent"]
        US040["US-040\nPersistent prompt bar\n🟠 High"]
    end

    subgraph DETAIL ["🏷 Epic 6 — Product detail"]
        US050["US-050\nPrice comparison\n🟠 High"]
        US051["US-051\nReview summary\n🟠 High"]
        US052["US-052\nSize social proof\n🟠 High"]
    end

    subgraph SOCIAL ["🤝 Epic 7 — Social discovery"]
        US070["US-070\nFollow recommendations\n🟠 High"]
    end

    subgraph V2 ["🧊 V2 — Creator economy"]
        US200["US-200\nCreator commissions\n🟠 High"]
    end

    %% Discovery gates
    SP1 -->|"gates"| US010
    SP2 -->|"gates"| US010

    %% Wardrobe chain
    US001 --> US060
    US001 --> US002
    US001 --> US003
    US003 --> US004
    US003 --> US020

    %% Scan chain
    US010 --> US011
    US010 --> US032
    US010 --> US040
    US010 --> US050

    %% Looks chain
    US020 --> US021
    US021 --> US030

    %% Profiles chain
    US003 --> US030
    US030 --> US031
    US011 --> US031

    %% Product detail chain
    US050 --> US051
    US050 --> US052
    US060 --> US052

    %% Social chain
    US030 --> US070
    US060 --> US070

    %% V2
    US030 -.->|"V2"| US200

    %% Styling
    style SP1 fill:#fee2e2,stroke:#ef4444
    style SP2 fill:#fee2e2,stroke:#ef4444
    style D1 fill:#f3f4f6,stroke:#9ca3af
    style US010 fill:#fef3c7,stroke:#f59e0b
    style US200 fill:#f3f4f6,stroke:#9ca3af
```

## Reading this diagram

- **Red border** = critical priority
- **Orange border** = high priority
- **Yellow fill** = currently blocked (waiting for spike results)
- **Grey fill** = deferred (V2 or paused)
- **Solid arrow** = hard dependency (cannot build without)
- **Dashed arrow** = soft dependency (can build independently but related)

## Critical path to MVP launch

```mermaid
flowchart LR
    SP1["SPIKE-001\n✅ Unblocked"] --> US010["US-010\nScan"]
    SP2["SPIKE-002\n⚠️ Not started"] --> US010
    US001["US-001\nCamera"] --> US003["US-003\nGrid"]
    US001 --> US060["US-060\nSize"]
    US003 --> US020["US-020\nLooks"]
    US010 --> US011["US-011\nWishlist"]
    US020 --> US021["US-021\nBrowse"]
    US021 --> US030["US-030\nProfiles"]
    US030 --> LAUNCH(["🚀 MVP Beta\n2026-07-09"])
    US011 --> LAUNCH
    US060 --> LAUNCH

    style LAUNCH fill:#d1fae5,stroke:#10b981
    style SP1 fill:#d1fae5,stroke:#10b981
    style SP2 fill:#fee2e2,stroke:#ef4444
```
