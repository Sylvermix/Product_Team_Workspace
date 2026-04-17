# Architecture Technique
**Atelier — Stack MVP**
Last updated: 2026-04-17

## Vue d'ensemble

```mermaid
flowchart TB
    subgraph CLIENTS ["📱 Clients"]
        IOS["iOS 16+"]
        AND["Android 10+"]
    end

    subgraph FRONTEND ["📱 Frontend — React Native + Expo"]
        direction LR
        UI["UI Layer\nNativeWind\n(Tailwind for RN)"]
        STATE["State\nZustand / Jotai"]
        ANIM["Animations\nReanimated 3 + Moti"]
        CAM["Camera\nExpo Camera"]
    end

    subgraph CDN ["🌐 CDN"]
        CF["Cloudflare\nImages + Assets"]
    end

    subgraph AUTH ["🔐 Auth"]
        CLERK["Clerk / Auth0"]
    end

    subgraph API ["⚙️ Backend — Python FastAPI"]
        direction TB
        GATEWAY["API Gateway\nFastAPI"]
        WORKERS["Worker queues\nCelery + Redis"]
    end

    subgraph AI ["🤖 AI Pipeline"]
        direction TB
        SEG["Garment segmentation\nGroundingDINO"]
        VISION["Classification\nClaude Vision"]
        SEARCH["Product search\nSerpAPI → Google Shopping"]
        EMBED["Embeddings\nCLIP fine-tuned"]
    end

    subgraph DB ["🗄️ Data layer"]
        direction LR
        PG["PostgreSQL\nUsers · Wardrobes\nLooks · Wishlists"]
        S3["S3-compatible\nObject Storage\nPhotos · Videos"]
        VDB["Vector DB\nPinecone / Qdrant\n/ pgvector\nEmbeddings"]
    end

    subgraph OBS ["📊 Observability"]
        direction LR
        PH["PostHog\nAnalytics + Flags"]
        SENTRY["Sentry\nErrors"]
    end

    subgraph CICD ["🔄 CI/CD"]
        direction LR
        GHA["GitHub Actions"]
        EAS["EAS Build\n(Expo)"]
        DEPLOY["Backend deploy\nAWS / GCP"]
    end

    IOS & AND --> CF
    CF --> FRONTEND
    FRONTEND --> AUTH
    FRONTEND --> GATEWAY
    GATEWAY --> WORKERS
    WORKERS --> AI
    WORKERS --> DB
    AI --> DB
    SEG --> VISION --> SEARCH
    SEARCH --> EMBED --> VDB

    FRONTEND --> PH
    GATEWAY --> SENTRY

    GHA --> EAS
    GHA --> DEPLOY

    style FRONTEND fill:#dbeafe,stroke:#3b82f6
    style AI fill:#fef3c7,stroke:#f59e0b
    style DB fill:#ecfdf5,stroke:#10b981
    style OBS fill:#fae8ff,stroke:#a855f7
    style CICD fill:#f1f5f9,stroke:#64748b
```

## Pipeline AI — Scan d'un produit

```mermaid
sequenceDiagram
    actor U as 📱 User
    participant APP as React Native
    participant API as FastAPI
    participant Q as Celery Queue
    participant GDINO as GroundingDINO
    participant CV as Claude Vision
    participant SERP as SerpAPI
    participant S3 as Object Storage
    participant DB as PostgreSQL

    U->>APP: Selects photo
    APP->>S3: Upload photo
    S3-->>APP: photo_url
    APP->>API: POST /scan {photo_url}
    API->>Q: Enqueue scan job
    API-->>APP: job_id (streaming SSE)

    Note over Q,SERP: Worker pipeline (async)

    Q->>GDINO: Detect garments in photo
    GDINO-->>Q: Bounding boxes + labels

    loop For each detected garment
        Q->>CV: Classify garment\n(category, color, style, brand)
        CV-->>Q: Attributes + confidence score
        Q->>SERP: Search Google Shopping\n(attributes as query)
        SERP-->>Q: Product matches (3-5 per garment)
        Q-->>APP: Stream: garment detected\n+ products (SSE)
    end

    Q->>DB: Save scan result
    APP->>U: Progressive reveal\n(markers + product cards)

    Note over APP,U: < 6s total · $0.018/scan avg
```

## Modèle de données simplifié

```mermaid
erDiagram
    USER {
        uuid id
        string email
        string username
        boolean is_public
        timestamp created_at
    }

    GARMENT {
        uuid id
        uuid user_id
        string photo_url
        string category
        string color
        string season
        string brand
        string size
        jsonb ai_tags
        boolean is_public
    }

    LOOK {
        uuid id
        uuid user_id
        string name
        string occasion
        string season
        boolean is_public
    }

    LOOK_GARMENT {
        uuid look_id
        uuid garment_id
        int position
    }

    WISHLIST_ITEM {
        uuid id
        uuid user_id
        string product_url
        string product_image
        string retailer
        decimal price
        string currency
        jsonb metadata
    }

    SCAN {
        uuid id
        uuid user_id
        string photo_url
        jsonb results
        decimal cost_usd
        timestamp created_at
    }

    SIZE_PROFILE {
        uuid user_id
        string brand
        string category
        string size
        int sample_count
    }

    FOLLOW {
        uuid follower_id
        uuid following_id
        timestamp created_at
    }

    USER ||--o{ GARMENT : owns
    USER ||--o{ LOOK : creates
    USER ||--o{ WISHLIST_ITEM : saves
    USER ||--o{ SCAN : runs
    USER ||--o{ SIZE_PROFILE : has
    USER ||--o{ FOLLOW : follows
    LOOK ||--o{ LOOK_GARMENT : contains
    GARMENT ||--o{ LOOK_GARMENT : appears_in
```

## Budgets de performance

| Metric | Cible MVP |
|--------|-----------|
| App launch → home | < 2s cold / < 500ms warm |
| Photo upload → first result visible | < 6s |
| Wardrobe grid scroll (500+ items) | 60fps (virtualisé) |
| Image LQIP → full (4G) | < 300ms |
| AI inference cost / scan | < $0.02 |
| Infra cost / MAU (10k MAU) | < $0.50 |
| Daily scan limit | 10 scans/user |

## Contraintes légales & compliance

```mermaid
flowchart LR
    subgraph LEGAL ["⚖️ Compliance"]
        GDPR["GDPR (EU)\nExport + delete\nphotos = données perso"]
        CCPA["CCPA (California)\nMêmes droits"]
        AGE["No minors\nBirthdate gate 18+"]
        AFF["Affiliate disclosure\nFTC — conspicuous\nnear affiliate links"]
        PHOTO["Photos utilisateur\nPrivées par défaut\nPublic = opt-in"]
    end
```
