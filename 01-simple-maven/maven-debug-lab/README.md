Here is the `README.md` file for your project. It provides an overview of the project, setup instructions, usage steps, and how to debug using `jdb`.

---

### **README.md**


# Maven Debug Lab

This project demonstrates how to build and debug a simple Java program using Maven and the `jdb` debugger. It includes a factorial calculation program and JUnit 5 test cases to validate its functionality.

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

## **Features**
- **Main Application**: Calculates the factorial of a number using recursion.
- **JUnit 5 Test Cases**: Validates the factorial logic and handles edge cases.
- **Interactive Debugging**: Includes setup for using `jdb` to debug the program.

---

## **Requirements**
- Java 8 or higher (Java 21 recommended for modern features).
- Maven 3.6 or higher.
- Basic understanding of Java and debugging with `jdb`.

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
cd maven-debug-lab
```

### **2. Build the Project**
```bash
mvn clean package
```

This will compile the code, run the tests, and generate a JAR file in the `target/` directory.

### **3. Run the Application**
```bash
java -jar target/maven-debug-lab-1.0-SNAPSHOT.jar
```
<B>Factorial of 5 is: 120</B>


---

## **Debugging with `jdb`**

### **1. Run the Application in Debug Mode**
```bash
mvn clean test
```

- `transport=dt_socket`: Uses a socket for communication.
- `server=y`: The JVM waits for a debugger to attach.
- `suspend=y`: The JVM suspends execution until the debugger connects.
- `address=*:5005`: Listens for debugger connections on port 5005.

### **2. Attach `jdb` to the Debugging Session**
In a new terminal, run:
```bash
jdb -attach 5005
```

### **3. Set Breakpoints and Debug**
- **Set a breakpoint in the factorial method:**
  ```bash
  stop in com.example.App.factorial
  ```
- **Start the application:**
  ```bash
  run
  ```
- **Inspect variables:**
  ```bash
  print n
  ```
- **Step through the code:**
  ```bash
  step
  ```
- **Continue execution:**
  ```bash
  cont
  ```

---

## **Running Tests**

To run the tests, execute:
```bash
mvn test
```

JUnit 5 will validate the factorial logic, including edge cases like `factorial(0)` and handling invalid inputs.

---

## **Contributing**
1. Fork the repository.
2. Create a new branch (`feature/your-feature`).
3. Commit your changes (`git commit -am 'Add a new feature'`).
4. Push the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

---

## **License**
No License :)
---

## **Contact**
For questions or feedback, feel free to reach out:
- **Email**: eyal@levys.co.il
- **GitHub**: [https://github.com/elevy99927](https://github.com/elevy99927)

---

### **Key Features of the README**
- **Project Overview**: Explains what the project does and its purpose.
- **Setup and Debug Instructions**: Step-by-step guide to build, run, and debug using `jdb`.
- **Project Structure**: Visualizes the directory layout.
- **Contribution Guidelines**: Encourages collaboration.
- **Contact Information**: Provides a way for others to reach out.

Would you like me to generate the `LICENSE` file or add more debugging examples?