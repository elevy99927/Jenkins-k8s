# Gradle Lab and Documentation

## Overview

This lab focuses on Gradle, a powerful build automation tool used for Java, Kotlin, and Groovy projects. Gradle simplifies dependency management, builds, and testing processes with a declarative approach.

[Learn more about Gradle](https://gradle.org/)

### Preparations
#### Option 1
**Local installation**:
Follow the instruction on Gradle website

#### Option 2 
**Using docker**:
```bash
docker run -it -v $PWD:/home/gradle/lab   gradle:jdk23-jammy bash

cd lab
```

---

## Part 1: Basic Gradle Commands

1. **Initialize a Gradle project**:
   ```bash
   gradle init
   ```
   This sets up a new Gradle project with the necessary directory structure.

   ```
   Directory will be modified and existing files may be overwritten.  Continue? (default: no) [yes, no]  <B>yes</B>
   Enter selection (default: Application) [1..4]  1 
   Enter selection (default: Java) [1..6]  1
   Enter target Java version (min: 7, default: 21): 21
   Project name (default: lab):  lab
   Enter selection (default: Single application project) [1..2] 
   Enter selection (default: Kotlin) [1..2] 2 <B>(Groovy!!!)</B>
   Enter selection (default: JUnit Jupiter) [1..4] 1
   Generate build using new APIs and behavior (some features may change in the next minor release)? (default: no) [yes, no]  no
   ```

2. **View available tasks**:
   ```bash
   gradle tasks
   ```
   Lists all tasks defined in your project, including build and test tasks.

3. **Build the project**:
   ```bash
   gradle build
   ```
   Compiles the code, runs tests, and packages the application.

4. **Run tests**:
   ```bash
   gradle test
   ```
   Executes all unit tests in the `src/test` directory.

5. **Run the application**:
   ```bash
   gradle run
   ```
   Runs the application if the `application` plugin is applied.

---

## Part 2: Understanding Configuration Files

1. **`build.gradle`**
   - Core configuration file for Gradle projects.
   - Contains dependencies, plugins, and custom tasks.

   Example:
   ```groovy
   plugins {
       id 'java'
   }

   repositories {
       mavenCentral()
   }

   dependencies {
       testImplementation 'org.junit.jupiter:junit-jupiter:5.9.3'
   }

   tasks.register('customTask') {
       doLast {
           println 'Executing custom Gradle task!'
       }
   }
   ```

2. **`settings.gradle`**
   - Defines project settings and includes subprojects if applicable.

   Example:
   ```groovy
   rootProject.name = 'GradleLab'
   ```

---

## Part 3: Lab Instructions

### Step 1: Create the Project Directory
1. Open your terminal and create a directory for the project:
   ```bash
   mkdir GradleLab
   cd GradleLab
   ```

2. Initialize the Gradle project:
   ```bash
   gradle init
   ```
   Select the following options during initialization:
   - Type: `application`
   - Language: `Java`
   - Build script DSL: `Groovy`
   - Test framework: `JUnit`

### Step 2: Modify `build.gradle` and Add a Custom Task
1. Open `build.gradle` and add a custom task:
   ```groovy
   tasks.register('hello') {
       doLast {
           println 'Hello from Gradle!'
       }
   }
   ```

2. Save the file and verify the custom task:
   ```bash
   gradle hello
   ```

### Step 3: Write Sample Code
1. Create the following file structure:
   ```
   src/main/java/com/example/App.java
   src/test/java/com/example/AppTest.java
   ```
   **Hint**
   ```bash
   mkdir -p src/main/java/com/example/
   mkdir -p src/test/java/com/example/
   ```

2. Write the sample application in `App.java`:
   ```java
   package com.example;

   public class App {
       public static void main(String[] args) {
           System.out.println("Hello, Gradle!");
       }
   }
   ```

3. Write a unit test in `AppTest.java`:
   ```java
   package com.example;

   import org.junit.jupiter.api.Test;
   import static org.junit.jupiter.api.Assertions.*;

   public class AppTest {
       @Test
       void testMain() {
           assertEquals(1, 1); // Simple test
       }
   }
   ```

4. Run the tests:
   ```bash
   gradle test
   ```

### Step 4: Deploy the Application (Mock Deploy)
1. Create a `deploy` task in `build.gradle`:
   ```groovy
   tasks.register('deploy') {
       doLast {
           println 'Deploying application...'
       }
   }
   ```

2. Execute the deploy task:
   ```bash
   gradle deploy
   ```

---

## Part 4: Challenge Step

### Challenge
Add a custom Gradle task that does the following:
1. Compiles the project.
2. Runs tests.
3. Generates a custom report file in the `build/reports` directory with the text "Build and Test Successful".

### Solution
<A href="Solution.md">[text](Solution.md)</A>

---

## License

This project is licensed under the MIT License.

---
## **Contact**
For questions or feedback, feel free to reach out:
- **Email**: eyal@levys.co.il
- **GitHub**: [https://github.com/elevy99927](https://github.com/elevy99927)


