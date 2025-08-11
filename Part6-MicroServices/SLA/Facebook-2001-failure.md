


```mermaid
sequenceDiagram
    autonumber
    participant NetEng as Network Engineer
    participant Cfg as Config System
    participant BGP as BGP Routers (FB AS)
    participant DNS as Facebook Authoritative DNS
    participant IGW as Internet (Other AS / ISPs)
    participant User as Users/Clients
    participant Internal as Internal Tools & Access

    Note over NetEng,Cfg: Maintenance window — apply network config change
    NetEng->>Cfg: Push config change
    Cfg-->>BGP: Update BGP/Control-plane configuration
    BGP-->>IGW: Withdraw BGP routes for FB prefixes

    Note over IGW,BGP: Internet no longer sees routes to Facebook IP ranges
    IGW-->>User: FB prefixes unreachable

    User->>DNS: Resolve facebook.com / whatsapp.com
    DNS-->>User: ❌ Unreachable (DNS hosted on same network)

    Note over User,DNS: DNS timeouts + no route to FB IPs

    User->>IGW: Connect to Facebook services (HTTPS)
    IGW-->>User: ❌ Connection fails (no route)

    Note over Internal,BGP: Internal control & tools rely on same network
    Internal->>BGP: Attempt rollback / access
    BGP-->>Internal: ❌ No access (mgmt path impacted)

    Note over NetEng,Internal: Engineers escalate; need out-of-band (OOB) access and physical presence
    NetEng->>BGP: OOB/physical access — restore baseline config
    BGP-->>IGW: Announce routes for FB prefixes

    IGW-->>DNS: Paths restored; authoritative DNS reachable
    User->>DNS: Resolve domains
    DNS-->>User: ✅ IPs returned

    User->>IGW: Connect to services
    IGW-->>User: ✅ Traffic flows to FB infra

    Note over NetEng,User: Postmortem — guardrails for config, change validation, mgmt-plane isolation, multi-provider DNS
```