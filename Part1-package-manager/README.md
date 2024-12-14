# Part 1: Package Manager 

## Overview
This section focuses on introducing popular package managers and build tools used in modern development and CI/CD pipelines. The goal is to provide hands-on exercises for setting up and managing projects using Maven, Gradle, Node.js, and Python.

## Contents
- **Maven**: Demonstrates Java project management with `pom.xml`.
- **Gradle**: Explores build automation with `build.gradle`.
- **Node.js**: Covers dependency management using `package.json`.
- **Python**: Utilizes `requirements.txt` and virtual environments.

---

### <a href="./01-simple-maven/">Maven</A>
- **Description**:
  Maven is a build automation tool primarily used for Java projects. It uses `pom.xml` for dependency management and build configurations.

- **Setup Instructions**:
  1. Ensure Maven is installed: `mvn -v`
  2. Navigate to the Maven folder.
  3. Run `mvn clean install` to build the project.

- **Key Commands**:
  - `mvn clean install`: Cleans and builds the project.
  - `mvn test`: Runs tests using the Surefire plugin.

---

### Gradle
- **Description**:
  Gradle is a flexible build tool that supports Java, Kotlin, and more. It uses `build.gradle` for configurations and tasks.

- **Setup Instructions**:
  1. Ensure Gradle is installed: `gradle -v`
  2. Navigate to the Gradle folder.
  3. Run `gradle build` to build the project.

- **Key Commands**:
  - `gradle build`: Assembles and tests the project.
  - `gradle clean`: Cleans the project directory.

---

### Node.js
- **Description**:
  Node.js is a JavaScript runtime often paired with `npm` or `yarn` for dependency management.

- **Setup Instructions**:
  1. Install Node.js using `nvm`: `nvm install node`
  2. Navigate to the Node.js folder.
  3. Run `npm install` to install dependencies.
  4. Use `npm start` to start the application.

- **Key Commands**:
  - `npm install`: Installs project dependencies.
  - `npm test`: Runs test scripts defined in `package.json`.

---

### Python
- **Description**:
  Python projects use `requirements.txt` to specify dependencies. Virtual environments ensure isolated development setups.

- **Setup Instructions**:
  1. Create a virtual environment: `python3 -m venv venv`
  2. Activate the environment:
     - Linux/Mac: `source venv/bin/activate`
     - Windows: `venv\Scripts\activate`
  3. Install dependencies: `pip install -r requirements.txt`
  4. Run the script: `python app.py`

- **Key Commands**:
  - `pip install -r requirements.txt`: Installs dependencies.
  - `deactivate`: Deactivates the virtual environment.

---

## Suggested Workflow
1. **Start with Maven**:
   - Learn the basics of dependency and build management.
2. **Move to Gradle**:
   - Understand the differences and explore advanced features.
3. **Practice with Node.js**:
   - Explore package management and JavaScript tooling.
4. **Experiment with Python**:
   - Work with virtual environments and pip for dependency management.

---

## Troubleshooting
- **Common Issues**:
  - Missing dependencies: Ensure `pom.xml`, `build.gradle`, or `requirements.txt` are properly configured.
  - Version mismatches: Verify installed versions of Maven, Gradle, Node.js, and Python.

- **Useful Commands**:
  - `mvn -v`, `gradle -v`, `node -v`, `python3 --version`: Verify installations.
  - Clear caches: `npm cache clean --force`, `gradle --stop`.

---

## Conclusion
This directory serves as a foundational guide for understanding and using package managers effectively in modern software development. Follow the exercises to gain hands-on experience with each tool and their integration into CI/CD pipelines.

---

## License

This project is licensed under the MIT License.

---
## **Contact**
For questions or feedback, feel free to reach out:
- **Email**: eyal@levys.co.il
- **GitHub**: [https://github.com/elevy99927](https://github.com/elevy99927)
