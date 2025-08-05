# Professional Guide to Microservices Architecture Design Patterns

Below is a classification and evaluation of architectural design patterns relevant to microservices.

---

## Pattern Summary Table

| Pattern Name                     | Suitable for Microservices | Notes                                                  |
| -------------------------------- | -------------------------- | ------------------------------------------------------ |
| Shared Database per Service      | ❌ No                       | Creates dependency; not recommended for MSA            |
| **Database per Service**         | ✅ Yes                      | Isolates DB per service; enables scaling and autonomy  |
| **Event Sourcing**               | ✅ Yes                      | Traceability, transparency, and state recovery         |
| **Decompose by Subdomain (DDD)** | ✅ Yes                      | Split by domain context and bounded contexts           |
| **Bulkhead Pattern**             | ✅ Yes                      | Isolates components/resources to prevent total failure |
| **Log Aggregation**              | ✅ Yes                      | Central log collection for search and analysis         |
| **Performance Metrics**          | ✅ Yes                      | Tracks performance and detects bottlenecks             |
| **Health Check**                 | ✅ Yes                      | Availability check for orchestrators                   |
| **External Configuration**       | ✅ Yes                      | Externalized configuration management                  |
| **Circuit Breaker Pattern**      | ✅ Yes                      | Prevents repeated failures by breaking connection      |
| **Saga**                          | ✅ Yes                      | Manages distributed transactions by breaking them into local steps. |
| **Decorator Pattern**                | ✅ Yes                  | Dynamically adds functionality to content such as tags, ratings, or overlays |  
| **Observer Pattern**                 | ✅ Yes                  | Notifies components about content updates or user preference changes         | 
| **Algorithm Pattern**                | ✅ Yes                    | Encapsulates algorithms to allow selection and replacement at runtime|
|  |  |  |
|  |  |  |
| API Gateway Pattern              | ✅ Yes                      | Central layer for routing and security                 |
| CQRS                             | ✅ Yes                      | Separates reads and writes; improves performance       |
| Decompose by Business Capability | ✅ Yes                      | Split by distinct business functions                   |
| Decompose by Transactions        | ✅ Yes                      | Split based on isolated transactional boundaries       |
| Strangler Pattern                | ✅ Yes                      | Gradual migration from monolith to microservices       |
| Sidecar Pattern                  | ✅ Yes                      | Side container for infrastructure concerns             |
| Aggregator Pattern               | ✅ Yes                      | Combines results from multiple services                |
| Proxy Pattern                    | ✅ Yes                      | Acts as a facade between clients and services          |
| Gateway Routing Pattern          | ✅ Yes                      | Routes smartly based on URI or parameters              |
| Chained Microservice Pattern     | ✅ Yes                      | Sequential calls between services                      |
| Branch Pattern                   | ✅ Yes                      | Parallel requests to multiple services                 |
| Distributed Tracing              | ✅ Yes                      | Full trace between services                            |
| Service Discovery Pattern        | ✅ Yes                      | Dynamic discovery of services                          |
| Client-Side UI Composition       | ✅ Yes                      | Micro Frontends – UI split across teams                |
| Blue-Green Deployment        | ✅ Yes                      | Enables zero-downtime deployment                       |
|  |  |  |

---


## Design Patterns

### 1. Database per Service

**Description:**
Each microservice has its own dedicated database, fully isolated from others.

**When to Use:**
When you want data isolation, service autonomy, and independent scalability or technology choice.

**Advantages:**

* Independent services
* Freedom to use different DB tech per service
* Enables scaling per service

**Disadvantages:**

* Cross-service transactions are hard
* Complex distributed queries
* Requires CQRS/Event Sourcing

---

### 2. Event Sourcing

**Description:**
Every data change is saved as an event rather than just storing the current state.

**When to Use:**
For full change traceability, audit logs, or event-driven systems.

**Advantages:**

* Complete event history
* Enables state rebuilds
* Kafka-friendly architecture

**Disadvantages:**

* Complex logic and tooling
* Requires event storage and processing infra

---

### 3. Decompose by Subdomain (DDD)

**Description:**
Split services based on domain boundaries using Domain-Driven Design principles.

**When to Use:**
In complex systems with distinct domain contexts and ownership boundaries.

**Advantages:**

* Aligns architecture with business structure
* Promotes service ownership
* Encourages modular design

**Disadvantages:**

* Requires good understanding of business domains
* May be hard to enforce boundaries across teams

---

### 4. Bulkhead Pattern

**Description:**
Separates resources or service areas so that failure in one doesn't affect others.

**When to Use:**
In multi-tenant or shared-infrastructure environments.

**Advantages:**

* Fault isolation
* Maintains partial system availability
* Resilient under stress

**Disadvantages:**

* Increased resource usage
* Requires careful partitioning

---

### 5. Log Aggregation

**Description:**
Collects logs from multiple services into a centralized location for searching, filtering, and correlation.

**When to Use:**
In systems with many distributed services where troubleshooting requires unified logging.

**Advantages:**

* Simplifies debugging across services
* Enables alerting and auditing
* Works well with ELK/EFK stacks or Loki

**Disadvantages:**

* Requires setup of log collectors and storage
* May introduce latency or storage overhead

---

### 6. Performance Metrics

**Description:**
Gathers key performance indicators (KPIs) such as response time, throughput, memory usage, and error rates.

**When to Use:**
To enable observability, performance tuning, and SLA tracking in production environments.

**Advantages:**

* Identifies bottlenecks and regressions
* Enables auto-scaling decisions
* Supports SLO/SLA monitoring

**Disadvantages:**

* Needs integration with metric collection tools (e.g., Prometheus)
* Requires careful selection of relevant metrics

---

### 7. Health Check

**Description:**
Provides endpoints or mechanisms for the orchestrator (like Kubernetes) to check if a service is alive and ready to receive traffic.

**When to Use:**
In orchestrated environments to enable self-healing, autoscaling, and service restarts.

**Advantages:**

* Ensures high availability
* Allows automated failover and recovery
* Supports readiness/liveness probes

**Disadvantages:**

* Needs to be correctly implemented and tested
* Can trigger unnecessary restarts if thresholds are too strict

---

### 8. External Configuration

**Description:**
Separates configuration settings from code by storing them in external sources such as environment variables, config servers, or secrets managers.

**When to Use:**
In any system that needs to support multiple environments (dev, staging, production) or dynamic reconfiguration.

**Advantages:**

* Enables configuration per environment without code changes
* Improves security by separating secrets
* Simplifies deployment pipelines

**Disadvantages:**

* Adds dependency on external config providers
* Requires synchronization between services and config sources

---

### 9. Circuit Breaker Pattern

**Description:**
Blocks access to failing services temporarily to avoid cascading failures.

**When to Use:**
When dependencies are unstable or under failure.

**Advantages:**

* Protects system stability
* Supports fallback behavior

**Disadvantages:**

* Needs precise tuning
* Can mistakenly block working services

---

### 10. [Saga](./Saga.md)

**Description:**
Manages distributed transactions by breaking them into local steps and compensation actions.

**When to Use:**
In place of ACID transactions across services where eventual consistency is acceptable.

**Advantages:**

* Eventually consistent across services
* Microservices-friendly
* Supports rollback via compensation

**Disadvantages:**

* Logic is complex
* Error handling is tricky

---

### 11. Decorator Pattern

**Description:**
Dynamically adds functionality to content or objects (e.g., tags, ratings, overlays) without modifying the original structure.

**When to Use:**
When additional behavior needs to be layered onto a component without altering its core logic.

**Advantages:**

* Flexible and reusable wrappers
* Follows Open-Closed principle

**Disadvantages:**

* Can lead to many small classes
* May be harder to trace behavior

---

### 12. Observer Pattern

**Description:**
Notifies subscribed components automatically when the observed object changes.

**When to Use:**
For real-time updates or loosely coupled publish/subscribe communication.

**Advantages:**

* Promotes decoupling
* Supports reactive design

**Disadvantages:**

* Harder to debug and test
* Risk of memory leaks if observers aren’t cleaned up

---

### 13. Algorithm Pattern

**Description:**
Encapsulates algorithms to allow them to be interchanged dynamically at runtime.

**When to Use:**
When the behavior of an object needs to vary depending on context or strategy.

**Advantages:**

* Promotes reusability and testability
* Adheres to Strategy Pattern principles

**Disadvantages:**

* Adds complexity with more classes/abstractions
* Choosing and managing strategies can be challenging


---

## MicroServices Exercise (30 minutes)
Design Pattern Analysis in a Microservices-Based Content Platform (e.g., Netflix)

### Background:
A service like Netflix delivers video content to millions of users simultaneously, across various devices, with personalized experiences, high performance, and fault tolerance. Such a system is typically built on DevOps principles and a microservices architecture.

### Task:
Choose any content streaming service (real or fictional – such as Netflix, Disney+, or one you invent), and answer the following:

### Steps:
**General System Overview:**
- What type of content does it provide?
- What core components does it include (search, recommendations, streaming, user management)?

**Identifying Microservices:**

List 3–5 possible microservices in the system (e.g., content service, recommendation engine, user service).

**Design Pattern Mapping:**

Select at least 5 design patterns from the course document.

For each pattern, answer:
- In which component will you use it?
- What problem does it solve?
- How will it be implemented in practice?