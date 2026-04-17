# User Flow — Onboarding
**Atelier — First launch to first value**
Last updated: 2026-04-17

```mermaid
flowchart TD
    START([App Launch]) --> B0

    B0["⬜ Beat 0 — First breath
    Wordmark · 1.5s · auto-advance"]

    B0 --> B1

    B1["🔒 Beat 1 — Age gate
    Enter birth year · BLOCKING"]

    B1 -->|"< 18"| BLOCKED(["❌ Blocked — graceful exit"])
    B1 -->|"18+"| B2

    B2["✨ Beat 2 — The offering
    'Your clothes, finally seen.'"]

    B2 -->|"Scan a photo now"| B3A
    B2 -->|"Start with my wardrobe"| B3B

    subgraph SCAN ["Scan path (immediate value)"]
        B3A["📷 Beat 3a — ScanChooserSheet
        Camera or Photo library"]
        B3A --> SCANRESULT{Scan result}
        SCANRESULT -->|"Match found"| B4A
        SCANRESULT -->|"No match"| B2
        SCANRESULT -->|"Cancelled"| B2
    end

    subgraph IMPORT ["Wardrobe import path (investment)"]
        B3B["🖼 Beat 3b — Photo roll offer
        'Your wardrobe might already be in here'"]
        B3B -->|"Accept"| IMPORT2["Multi-select · up to 10 photos
        AI auto-tags + mandatory size picker"]
        B3B -->|"Skip"| EMPTY["Empty wardrobe grid"]
        IMPORT2 --> GRID["Wardrobe grid · items visible"]
        EMPTY --> SCANPROMPT["Scan button + 'Scan anything.' prompt"]
        GRID --> SCANPROMPT
        SCANPROMPT -->|"Tap scan"| B3A
    end

    B4A["🎯 Beat 4a — Recognition moment
    FIRST VALUE ACHIEVED
    Garment label in display serif
    Product matches visible"]

    B4A --> INTENT{Save intent}

    INTENT -->|"Add to wardrobe"| SIZEPICKER["Size picker
    Brand-aware · one-tap · mandatory"]
    INTENT -->|"Save to wishlist"| B5
    INTENT -->|"Exit / continue browsing"| B6SESSION

    SIZEPICKER --> B5

    B5["🔐 Beat 5 — Account gate
    Bottom sheet · soft prompt
    'Keep what you found.'"]

    B5 -->|"Create account"| B6FULL
    B5 -->|"Maybe later"| B6SESSION

    B6FULL(["🏠 Beat 6 — Home · Full mode
    Wardrobe · Looks · Scan · AI Agent"])
    B6SESSION(["🏠 Beat 6 — Home · Session mode
    Limited · scan results lost on exit"])

    B6FULL --> AGENT["💬 AI Agent prompt bar
    Available from home screen"]
    B6SESSION --> AGENT2["💬 AI Agent prompt bar
    Available · account prompted on save"]

    style BLOCKED fill:#fee2e2,stroke:#ef4444
    style B4A fill:#fef3c7,stroke:#f59e0b
    style B6FULL fill:#d1fae5,stroke:#10b981
    style B6SESSION fill:#e0f2fe,stroke:#0ea5e9
    style AGENT fill:#ede9fe,stroke:#8b5cf6
    style AGENT2 fill:#ede9fe,stroke:#8b5cf6
```

## Legend

| Symbol | Meaning |
|--------|---------|
| 🔒 | Blocking step — cannot skip |
| ✨ | Key emotional beat |
| 🎯 | First value moment |
| 🔐 | Account gate |
| 🏠 | Post-onboarding home |
| 💬 | AI agent surface |

## Key decisions encoded in this flow

- Age gate is the only blocking step
- Account creation deferred to first save action
- Both paths (scan + import) converge at the recognition moment
- Guest mode is permanent — "Maybe later" leads to a real usable state, not a dead end
- AI agent is available from home in both modes
