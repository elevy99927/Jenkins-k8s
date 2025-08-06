## Microservices Exercise Solution – Streaming Platform Design

### Chosen Platform: Streamio (Fictional Content Streaming Service)

---

### General System Overview

**Content Type:**

* On-demand video streaming
* TV shows, movies, live events

**Core Components:**

* User Management (authentication, profiles, billing)
* Search Engine (content discovery)
* Recommendation Engine (personalized content)
* Streaming Service (video playback)
* Content Catalog (metadata and indexing)

---

### Identified Microservices

1. **User Service** – manages user accounts, subscriptions, and authentication
2. **Content Service** – holds metadata, availability, and content structure
3. **Recommendation Service** – generates personalized suggestions
4. **Streaming Service** – delivers video content and handles adaptive streaming
5. **Search Service** – indexes content and handles search queries

---

### Design Pattern Mapping

#### 1. **Database per Service**

* **Used in:** All core services (User, Content, Recommendation, etc.)
* **Problem Solved:** Isolation, independent scalability, and technology flexibility
* **Implementation:** Each service uses its own DB (e.g., PostgreSQL for users, Elasticsearch for search, Cassandra for recommendations)

#### 2. **API Gateway Pattern**

* **Used in:** Entry point for mobile/web/TV clients
* **Problem Solved:** Centralizes access control, throttling, and routing
* **Implementation:** NGINX or AWS API Gateway routes traffic to internal services securely

#### 3. **Circuit Breaker Pattern**

* **Used in:** Streaming service when connecting to CDN or user analytics
* **Problem Solved:** Prevents cascading failure during dependency outages
* **Implementation:** Resilience libraries (like Hystrix or Resilience4j) to monitor and break connection on repeated failure

#### 4. **Event Sourcing**

* **Used in:** User activity tracking, billing events, recommendation updates
* **Problem Solved:** Enables audit, state rebuilds, and event-driven updates
* **Implementation:** Kafka or Amazon Kinesis used for capturing events; services consume and act upon them

#### 5. **Saga Pattern**

* **Used in:** Multi-step processes like onboarding or subscription purchase
* **Problem Solved:** Distributed transaction management with compensation logic
* **Implementation:** Orchestrated saga with rollback logic if payment fails, e.g., cancel account creation

---

#### 6. **Log Aggregation**

* **Used in:** All services
* **Problem Solved:** Centralized log analysis and troubleshooting across distributed services
* **Implementation:** Fluentd or Logstash collects logs and ships them to ELK/EFK stack or Loki/Grafana

#### 7. **Health Check**

* **Used in:** All Kubernetes-managed services
* **Problem Solved:** Enables orchestrator to restart failed pods and ensure service readiness
* **Implementation:** Readiness and liveness probes defined in Kubernetes manifests

#### 8. **External Configuration**

* **Used in:** All services requiring environment-specific settings
* **Problem Solved:** Avoids hardcoded configs, supports CI/CD and secrets management
* **Implementation:** Configuration is managed via ConfigMaps, Secrets, or Spring Cloud Config Server

---

###  Summary

This fictional streaming service architecture demonstrates scalable, resilient, and decoupled design using established microservice patterns. Each design pattern addresses a specific challenge in building a real-world platform similar to Netflix.
