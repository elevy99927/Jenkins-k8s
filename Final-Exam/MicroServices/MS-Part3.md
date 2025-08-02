## Exercise: Microservices and Decoupling with Kafka

### Step 3: What if B crashes after consuming the message?

#### Problem:

* Kafka marks the message as "read" at the time of pull.
* If B crashes after pulling but before processing – the message may be lost and not processed again.

---

## Advanced Exercise:

### Question:

> Find a way to ensure the message is not lost if Service B crashes after consuming it but before finishing processing.

#### Guiding Questions:

1. What is the difference between at-least-once and exactly-once?

```mermaid
sequenceDiagram
    participant P as Producer
    participant K as Kafka
    participant C as Consumer

    P->>K: Send message
    K->>C: Consume message
    alt at-least-once
        C->>K: Process + Commit (may resend if crash occurs before commit)
    else exactly-once
        C->>K: Process + Safe Commit (Kafka ensures no duplicates)
    end
```

```mermaid
graph TD
    A[Producer sends message] --> B[Kafka stores]
    B --> C1[at-least-once: B may receive it again]
    B --> C2[exactly-once: Kafka ensures full consistency]
```

2. How can offset be controlled manually?

```mermaid
graph LR
    A[Consumer reads message] --> B{Was processing successful?}
    B -- yes --> C[Commit offset]
    B -- no --> D[Do not commit]
    D --> A
```

* The offset is the position of the message in Kafka's topic.
* The consumer can be configured to commit the offset only after successful processing.
* This ensures that if the service crashes, the message remains in Kafka and is reprocessed upon recovery.

3. What mechanisms can help with failed message processing?
4. Can checkpointing or a transactional outbox be used?

