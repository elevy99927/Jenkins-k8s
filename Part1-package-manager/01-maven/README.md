# Maven Lab and Documentation

## Overview

This section focuses on Maven, a powerful build automation tool primarily used for Java projects. Maven simplifies project management by using a standardized project object model (POM) and a declarative approach to building and managing dependencies.

[Learn more about Maven](https://maven.apache.org/)

---

## Directory Structure

This folder contains two labs to practice and understand Maven:

1. **<A href="./maven-java-lab">maven-java-lab</a>**
   - Covers fundamental Maven usage, including building, testing, and packaging Java projects.

2. **<a href="./maven-debug-lab">maven-debug-lab</a>**
   - Focuses on debugging Java applications with Maven.

---

## Part 1: Basic Maven Commands

1. **Check Maven version**:
   ```bash
   mvn -v
   ```
   Ensures Maven is installed and displays the version.

2. **Build the project**:
   ```bash
   mvn clean install
   ```
   Cleans the `target` directory, compiles code, runs tests, and packages the application.

3. **Run tests**:
   ```bash
   mvn test
   ```
   Executes unit tests in the `src/test` directory.

4. **Generate project from archetype**:
   ```bash
   mvn archetype:generate
   ```
   Creates a new Maven project using predefined templates.

5. **Dependency management**:
   ```bash
   mvn dependency:tree
   ```
   Displays the dependency hierarchy of the project.

6. **Run the application** (if configured):
   ```bash
   mvn exec:java -Dexec.mainClass="com.example.App"
   ```

---

## Part 2: Lab Instructions

### Lab 1: Maven Java Lab

#### Objective
Understand basic Maven functionality by building, testing, and packaging a Java project.

#### Steps
1. **Setup**:
   Navigate to the `maven-java-lab` directory:
   ```bash
   cd maven-java-lab
   ```

2. **Inspect the POM file**:
   Open `pom.xml` and review the project configuration, including dependencies and plugins.

3. **Run Maven commands**:
   - Compile the code:
     ```bash
     mvn compile
     ```
   - Run tests:
     ```bash
     mvn test
     ```
   - Package the application:
     ```bash
     mvn package
     ```

4. **Explore the target directory**:
   Inspect the `target` folder to find the generated `.jar` or `.war` file.

5. **Run the application**:
   ```bash
   java -jar target/maven-java-lab-1.0-SNAPSHOT.jar
   ```

---






### Lab 2: Maven Debug Lab

#### Objective
Learn how to debug a Maven-based Java application.

#### Steps
1. **Setup**:
   Navigate to the `maven-debug-lab` directory:
   ```bash
   cd maven-debug-lab
   ```

2. **Run the application**:
   ```bash
   mvn compile exec:java -Dexec.mainClass="com.example.App"
   ```

3. **Debug the application**:
   Use Maven's debugging options to troubleshoot issues:
   ```bash
   mvnDebug exec:java -Dexec.mainClass="com.example.App"
   ```

4. **Attach a debugger**:
   Connect your IDE or a command-line debugger to the specified port.

5. **Verify the fix**:
   Update the code if needed and rerun the application.

---

## Part 3: Challenge Step

### Challenge
Enhance the `maven-java-lab` project to:
1. Add a new dependency for JSON processing (e.g., `com.fasterxml.jackson.core:jackson-databind`).
2. Create a new class `JsonParser` that uses the library to parse a JSON string.
3. Write a unit test for `JsonParser`.

### Solution
1. **Update `pom.xml`**:
   ```xml
   <dependency>
       <groupId>com.fasterxml.jackson.core</groupId>
       <artifactId>jackson-databind</artifactId>
       <version>2.15.0</version>
   </dependency>
   ```

2. **Create `JsonParser.java`**:
   ```java
   package com.example;

   import com.fasterxml.jackson.databind.ObjectMapper;
   import java.io.IOException;

   public class JsonParser {
       public static String parse(String json) throws IOException {
           ObjectMapper mapper = new ObjectMapper();
           return mapper.readTree(json).toString();
       }
   }
   ```

3. **Write `JsonParserTest.java`**:
   ```java
   package com.example;

   import org.junit.jupiter.api.Test;
   import static org.junit.jupiter.api.Assertions.*;

   public class JsonParserTest {
       @Test
       void testParse() throws Exception {
           String json = "{\"key\":\"value\"}";
           assertEquals("{"key":"value"}", JsonParser.parse(json));
       }
   }
   ```

4. **Run the tests**:
   ```bash
   mvn test
   ```

---




