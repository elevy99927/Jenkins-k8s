# Lab: Introduction to Gradle

Gradle is a powerful build tool for Java and other JVM-based languages, as well as other platforms. It is known for its flexibility, performance, and ease of use. Gradle uses a domain-specific language (DSL) based on Groovy or Kotlin for its configuration scripts.

## Resources
- Official Gradle Website: [https://gradle.org/](https://gradle.org/)

---

## Objective
This lab focuses on:
1. Setting up and exploring Gradle.
2. Understanding and using basic Gradle commands.
3. Learning about the `build.gradle` and `settings.gradle` files.
4. Completing a challenge task to enhance learning.

---

## Part 1: Basic Gradle Commands

Navigate to the `Part1-package-manager/01-Gradle` folder to complete this lab.

### Commands
1. **Initialize a Gradle Project**:
   ```bash
   gradle init
   ```
   - Creates a new Gradle project with basic configuration files.

2. **List Available Tasks**:
   ```bash
   gradle tasks
   ```
   - Displays all the tasks available in the project.

3. **Build the Project**:
   ```bash
   gradle build
   ```
   - Compiles the code, runs tests, and generates build artifacts.

4. **Run the Project**:
   ```bash
   gradle run
   ```
   - Executes the main class of the application.

5. **Test the Project**:
   ```bash
   gradle test
   ```
   - Runs all the tests defined in the project.

6. **Clean the Project**:
   ```bash
   gradle clean
   ```
   - Removes all build artifacts.

---

## Part 2: Understanding the Configuration Files

### `build.gradle`
This file contains the build configuration for the project, including:
- Dependencies: Libraries or tools the project relies on.
- Plugins: Add functionalities like Java support or application support.
- Tasks: Custom tasks that define specific actions in the build lifecycle.

#### Example Snippet:
```groovy
plugins {
    id 'application'
}

application {
    mainClass = 'com.example.App'
}

dependencies {
    implementation 'org.apache.commons:commons-lang3:3.12.0'
    testImplementation 'junit:junit:4.13.2'
}

tasks.register('hello') {
    doLast {
        println 'Hello Gradle!'
    }
}
```

### `settings.gradle`
This file configures the Gradle project itself, including:
- Project name.
- Subprojects (if it's a multi-module project).

#### Example Snippet:
```groovy
rootProject.name = 'GradleExample'
```

---

## Part 3: Lab Instructions

### Step-by-Step Instructions (in terminal)

#### Project Setup
1. **Create the Project Directory**:
   ```bash
   mkdir GradleLab && cd GradleLab
   ```

2. **Initialize a Gradle Project**:
   ```bash
   gradle init
   ```
   Select the application project type and default configurations.

3. **Modify `build.gradle` and Add a Custom Task**:
   Open the `build.gradle` file and add the following custom task:
   ```groovy
   tasks.register('customTask') {
       doLast {
           println 'Executing Custom Task!'
       }
   }
   ```

4. **Write Sample Code**:
   Create a sample application file:
   ```bash
   mkdir -p src/main/java/com/example
   ```
   Add the following code to `src/main/java/com/example/App.java`:
   ```java
   package com.example;

   public class App {
       public static void main(String[] args) {
           System.out.println("Hello, Gradle Lab!");
       }
   }
   ```

5. **Write Test Code**:
   Create a test file:
   ```bash
   mkdir -p src/test/java/com/example
   ```
   Add the following code to `src/test/java/com/example/AppTest.java`:
   ```java
   package com.example;

   import org.junit.Test;
   import static org.junit.Assert.*;

   public class AppTest {
       @Test
       public void testApp() {
           assertTrue(true);
       }
   }
   ```

6. **Run Gradle Commands**:
   - Build the project: `gradle build`
   - Run the application: `gradle run`
   - Execute custom task: `gradle customTask`

7. **Deploy the Application (Mock Deploy)**:
   Simulate deployment by creating a `build/distributions` directory:
   ```bash
   mkdir -p build/distributions
   cp -r src/main/java/com/example build/distributions/
   echo "Application deployed to mock server!"
   ```

---

## Part 4: Challenge Step

Extend the lab with the following challenge:

1. **Add Another Custom Task**:
   - Create a task called `deployTask` in `build.gradle`:
     ```groovy
     tasks.register('deployTask') {
         doLast {
             println 'Deploying Application...'
         }
     }
     ```

2. **Enhance the Sample Application**:
   - Add a new feature in `App.java` that calculates and prints the factorial of a number.

3. **Write Tests for the New Feature**:
   - Extend `AppTest.java` to test the factorial function.

4. **Run and Validate**:
   - Build, test, and deploy the updated application using Gradle.

---

## Submission
- Provide the updated `build.gradle` and all Java files.
- Share screenshots of the terminal commands and outputs.
- Document any challenges faced during the process.

---

## Additional Reading
<a href="https://docs.gradle.org/current/userguide/gradle_basics.html">Gradle Basics</a>
 
---

## License

This project is licensed under the MIT License.

---
## **Contact**
For questions or feedback, feel free to reach out:
- **Email**: eyal@levys.co.il
- **GitHub**: [https://github.com/elevy99927](https://github.com/elevy99927)
