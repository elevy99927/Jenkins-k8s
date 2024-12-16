# Maven Java Lab

## Overview

This lab is designed as an introduction to Maven, a powerful build automation tool used primarily for Java projects. By completing this lab, you will gain an understanding of Maven commands, the purpose of the `pom.xml` configuration file, and the optional `settings.xml` file.

[Learn more about Maven](https://maven.apache.org/)

---

## Objectives

1. Understand what Maven is and why it is used.
2. Learn about `pom.xml` and `settings.xml`.
3. Create a new Maven project.
4. Build the project and run tests.

---


## Lab Instructions

### Step 1: Setup and Installation

1. Ensure Maven is installed on your system:
   ```bash
   mvn -v
   ```
   If not installed, follow the [installation guide](https://maven.apache.org/install.html).

2. Navigate to the `maven-java-lab` folder:
   ```bash
   cd Part1-package-manager/01-maven/maven-java-lab
   ```

### Step 2: Create a New Maven Project

1. Use the Maven archetype to generate a new project:
   ```bash
   mvn archetype:generate -DgroupId=com.example -DartifactId=maven-java-lab -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
   ```
   - **groupId**: A unique identifier for your project’s package.
   - **artifactId**: The name of your project.

2. Navigate to the newly created project directory:
   ```bash
   cd maven-java-lab
   ```

3. Open the `pom.xml` file and review its structure. Notice the dependencies and plugins.

### Step 3: Build the Project

1. Clean and compile the project:
   ```bash
   mvn clean compile
   ```

2. Package the project:
   ```bash
   mvn package
   ```

   This creates a `.jar` file in the `target` directory.
   <BR>Verify you can see the file `maven-java-lab-1.0-SNAPSHOT.jar` in the `maven-java-lab-1.0-SNAPSHOT.jar` directory
   
   ```bash
   ls -la target/maven-java-lab-1.0-SNAPSHOT.jar
   ```


### Step 4: Run Tests

1. Run the unit tests included in the project:
   ```bash
   mvn test
   ```

2. Review the test results in the console output or the `target/surefire-reports` directory.

### Step 5: Run the Application

1. Execute the packaged `.jar` file (it will fail. why?):
   ```bash
   java -jar target/maven-java-lab-1.0-SNAPSHOT.jar
   ```


### Step 6: Fix your Application and re-run
1. Create a file named `App.java` under `src/main/java/com/example/` with the following content:
   ```java
   package com.example;

   public class App {
       public static void main(String[] args) {
           System.out.println("Hello, Maven!");
       }
   }
   ```

2. Clean and compile the project:
   ```bash
   mvn clean compile
   ```

3. Package the project:
   ```bash
   mvn package
   ```
   This creates a `.jar` file in the `target` directory.


4. Run the unit tests included in the project:
   ```bash
   mvn test
   ```

5. Execute the packaged `.jar` file:
   ```bash
   java -cp target/maven-java-lab-1.0-SNAPSHOT.jar com.example.App
   ```




---

## Key Files in Maven Projects

1. **`pom.xml`**:
   - Central configuration file for your project.
   - Defines dependencies, build plugins, and project metadata.

2. **`settings.xml`** (Optional):
   - Found in the Maven home directory or user-specific directory (`~/.m2/`).
   - Used to customize repository paths, authentication, and global configurations.

---

## Challenge Step

1. Add a dependency for logging (e.g., SLF4J):
   ```xml
   <dependency>
       <groupId>org.slf4j</groupId>
       <artifactId>slf4j-api</artifactId>
       <version>2.0.0</version>
   </dependency>
   ```

2. Modify the `App.java` file to use SLF4J for logging.

3. Write a unit test for your changes and verify:
   ```bash
   mvn test
   ```



