# Maven Lab and Documentation



## Overview

This section focuses on Maven, a powerful build automation tool primarily used for Java projects. Maven simplifies project management by using a standardized project object model (POM) and a declarative approach to building and managing dependencies.

[Learn more about Maven](https://maven.apache.org/)

---

## What is Maven?

Maven is a build automation tool that simplifies the process of managing a project's lifecycle, dependencies, and configurations. It uses a standardized Project Object Model (POM) file, `pom.xml`, which contains the project’s metadata, dependencies, plugins, and build configurations.

### Key Features of Maven:
1. Dependency Management: Automatically download and manage libraries your project requires.
2. Build Lifecycle Management: Automate tasks like compilation, packaging, testing, and deployment.
3. Repository Management: Retrieve dependencies from central or custom repositories.
4. Extensibility: Use plugins to add functionality to your builds.

---

## Directory Structure

This folder contains two labs to practice and understand Maven:

1. **<A href="./maven-java-lab">maven-java-lab</a>**
   - Covers fundamental Maven usage, including building, testing, and packaging Java projects.

2. **<a href="./maven-debug-lab">maven-debug-lab</a>**
   - Focuses on debugging Java applications with Maven.

# Maven Lab and Documentation

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

Each lab includes detailed step-by-step instructions in their respective subfolder README files. Below is an overview of the labs:

### Lab 1: <A href="./maven-java-lab">Maven Java Lab</a>
   - Focus: Build and package a Java project using Maven while exploring key concepts such as the POM file, dependency management, and running packaged applications.

### Lab 2: <a href="./maven-debug-lab">Maven Debug Lab</a>
   - Focus: Learn to debug a Maven-based Java application by attaching a debugger to the application process and diagnosing runtime issues.

---

## Part 3: Challenge Step

### Challenge
Enhance the `maven-java-lab` project to:

1. Add a new dependency for JSON processing (e.g., `com.fasterxml.jackson.core:jackson-databind`).
2. Create a new class `JsonParser` that uses the library to parse a JSON string.
3. Write a unit test for `JsonParser`.

### <a href="./Part3-Solution.md">Solution</a>

---
## Additional Resources

- [Maven Documentation](https://maven.apache.org/guides/)
- [Maven Central Repository](https://search.maven.org/)
- [SLF4J Documentation](http://www.slf4j.org/)

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## **Contact**
For questions or feedback, feel free to reach out:
- **Email**: eyal@levys.co.il
- **GitHub**: [https://github.com/elevy99927](https://github.com/elevy99927)

---
