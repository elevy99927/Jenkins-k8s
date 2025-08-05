## Saga Design Pattern – Exercise Example

**Scenario background:**
User places an order on an e-commerce platform (similar to Amazon)

---
### 1. New User Registration (Saga Example 1)

1. **User submits registration form**
   * Input: name, email, password

2. **Service A: Check if user exists**
   * If user exists → Abort and notify

3. **Service B: Create user record**
   * Saves initial user profile in DB

4. **Service C: Send email confirmation**
   * Triggers email verification with token
   * If fails → Compensation: delete user record from step 3

5. **Service D: Assign default preferences**
   * Sets initial settings (language, theme, etc.)

6. **User confirms email**
   * Final activation step

**Exmaple 1:**
```mermaid
graph TD
    A[User Submits Registration] --> B{Check if User Exists?}
    B -->|Exists| C[Stop Process & Notify]
    B -->|New User| D[Send Confirmation Email]
    D -->|Email Sent| E[Wait for Confirmation]
    D -->|Email Failed| F[Stop Process]
    E -->|Confirmed| G[Activate Account]
    E -->|Not Confirmed| H[Cancel or Remind]

```
---
**Exmaple 2:**
```mermaid
graph TD
    A[Start User Registration] --> B[Check if User Exists]
    B -->|Exists| X[Abort & Notify]
    B -->|New User| C[Create User Record]
    C --> D[Send Email Confirmation]
    D -->|Success| E[Assign Default Preferences]
    E --> F[User Confirms Email]
    F --> G[Finish Registration]
    D -->|Fail| Y[Compensate: Delete User Record]
```

---
### 1. Submit New Order (Saga Example 2)

1. **User submits an order**

   * Input: list of items, delivery address, payment method

2. **Service A: Payment Authorization**

   * Checks card validity and blocks amount
   * If fails → stop process and notify user

3. **Service B: Inventory Reservation**

   * Checks product availability and reserves items
   * If fails → Compensation: release payment block from step 2

4. **Service C: Shipping Preparation**

   * Allocates shipping slot and label
   * If fails → Compensation:

     * Release inventory from step 3
     * Release payment from step 2

5. **Service D: Confirmation Notification**

   * Sends confirmation email to user

6. **Saga completes**

   * All steps succeed → order finalized and committed

---

### Compensation Logic

Saga ensures that if any of the steps fails, the previous steps will be compensated in reverse order, ensuring eventual consistency across services.

---

### Example with Mermaid Diagram

```mermaid
graph TD
    A[Start Order Saga] --> B[Authorize Payment]
    B -->|Success| C[Reserve Inventory]
    C -->|Success| D[Prepare Shipping]
    D -->|Success| E[Send Confirmation]
    E --> F[Finish Order]
    B -->|Fail| X[Abort: Notify User]
    C -->|Fail| Y[Compensate: Release Payment]
    D -->|Fail| Z[Compensate: Release Inventory + Payment]
```

---
### Next Step:
* Analyze real-world use of Saga in microservice architecture
