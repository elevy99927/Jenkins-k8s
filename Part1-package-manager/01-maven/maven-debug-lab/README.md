
# Maven Debug Lab

## Overview

This lab focuses on using the `jdb` debugger to debug a Java application. `jdb` is a command-line debugger for Java programs, part of the Java Development Kit (JDK). It allows you to debug Java programs interactively by setting breakpoints, inspecting variables, and stepping through code execution.

[Learn more about `jdb`](https://docs.oracle.com/en/java/javase/11/tools/jdb.html)

---
## **Project Structure**
```
maven-debug-lab/
├── src/
│   ├── main/
│   │   └── java/
│   │       └── com/
│   │           └── example/
│   │               ├── App.java       # Main application
│   ├── test/
│   │   └── java/
│   │       └── com/
│   │           └── example/
│   │               ├── AppTest.java   # JUnit test cases
├── pom.xml                            # Maven configuration
└── README.md                          # Project documentation
```
---
## Objective

By completing this lab, you will:

1. Understand what `jdb` is and why it is useful.
2. Learn how to run a Java application in debug mode.
3. Attach `jdb` to a running Java application.
4. Set breakpoints, inspect variables, and debug the application.

---

## What is `jdb`?

`jdb` is the Java Debugger, a tool provided with the JDK to debug Java applications. It enables developers to:

- Set breakpoints to pause execution at specific lines of code.
- Inspect variables and objects during runtime.
- Step through code to understand program flow.
- Diagnose and fix issues in the application.

Debugging with `jdb` is especially useful when graphical IDEs are unavailable or when working in server environments (for example in kubernetes pods).

---

## Lab Instructions

### Step 1: Prepare the Project

1. Ensure you have the JDK installed on your system:
   ```bash
   java -version
   ```
   If not installed, download and install the JDK from the [official site](https://www.oracle.com/java/technologies/javase-downloads.html).

2. Navigate to the `maven-debug-lab` folder:
   ```bash
   cd Part1-package-manager/01-maven/maven-debug-lab
   ```

3. Review the provided `App.java` file in `src/main/java/com/example/`:
   ```java
   package com.example;

   public class App {
       public static void main(String[] args) throws InterruptedException {
           System.out.println("Starting application...");
           for (int i = 0; i < 5; i++) {
               System.out.println("Count: " + i);
               Thread.sleep(1000);
           }
           System.out.println("Application completed.");
       }
   }
   ```

### Step 2: Compile the Application

1. Compile the application using Maven:
   ```bash
   mvn clean compile
   ```

2. Package the application:
   ```bash
   mvn package
   ```

### Step 3: Run the Application in Debug Mode

1. Start the application with debugging enabled:
   ```bash
   java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=5005 -cp target/maven-debug-lab-1.0-SNAPSHOT.jar com.example.App
   ```
   - `-agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=5005`: Enables remote debugging on port `5005`.
   - `suspend=y`: Ensures the program pauses until a debugger is attached.

2. The console should display:
   ```
   Listening for transport dt_socket at address: 5005
   ```

### Step 4: Attach `jdb` to the Application

1. Open a new terminal and run the following command to attach `jdb`:
   ```bash
   jdb -attach 5005
   ```

2. Once attached, you can interact with the application:
   - Set breakpoints:
     ```
     stop at com.example.App:7
     ```
     This sets a breakpoint at line 7 in `App.java`.

   - Continue execution:
     ```
     cont
     ```

   - Step through the code:
     ```
     step
     ```

   - Inspect variables:
     ```
     print i
     ```

   - Exit the debugger:
     ```
     exit
     ```

### Step 5: Debugging Exercise

1. Set breakpoints at different lines of the application.
2. Inspect the value of the `i` variable during each iteration of the loop.
3. Modify the application to include additional logging and re-run the debugger.

---

## Challenge Step

1. Modify `App.java` to include a division operation that could result in an `ArithmeticException`. Example:
   ```java
   int result = 10 / (i - 2);
   ```

2. Use `jdb` to:
   - Set a breakpoint at the line with the division operation.
   - Inspect the value of `i` before the operation.
   - Catch and diagnose the exception using the `catch` command in `jdb`.

3. Write down your observations and steps to resolve the issue.

---

## Additional Resources

- [Official JDB Documentation](https://docs.oracle.com/en/java/javase/11/tools/jdb.html)
- [Maven Documentation](https://maven.apache.org/guides/)

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## **Contact**
For questions or feedback, feel free to reach out:
- **Email**: eyal@levys.co.il
- **GitHub**: [https://github.com/elevy99927](https://github.com/elevy99927)

---
