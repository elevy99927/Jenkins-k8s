# Lab 1: Node.js Basics

## Overview

In this lab, you'll learn how to set up a Node.js project, understand the structure and role of `package.json` and `package-lock.json`, and explore basic npm commands. By the end of this lab, you'll have a simple Node.js application ready to build upon.

[Learn more about Node.js](https://nodejs.org/)

---

## Objectives

1. Understand the purpose of `package.json` and `package-lock.json`.
2. Create a new Node.js project.
3. Add dependencies using npm.
4. Run your application.

---

## Instructions

### Step 1: Set Up Your Environment

1. Ensure you have Node.js installed:

   ```bash
   node -v
   npm -v
   ```

   If not installed, download and install Node.js from the [official website](https://nodejs.org/).

2. Create a new project folder:

   ```bash
   mkdir nodejs-basics-lab
   cd nodejs-basics-lab
   ```

### Step 2: Initialize a Node.js Project

1. Initialize a new Node.js project:

   ```bash
   npm init -y
   ```

   This will create a `package.json` file with default values.

2. Open the `package.json` file and observe its contents. It contains metadata about your project, including dependencies and scripts.

### Step 3: Install a Dependency

1. Add the `express` package to your project:

   ```bash
   npm install express
   ```

2. Observe the changes:

   - The `package.json` file now includes `express` under `dependencies`.
   - A new file, `package-lock.json`, is created to lock the dependency tree for your project.

3. Explore the `node_modules` folder, which contains the installed packages.

### Step 4: Write a Simple Node.js Application

1. Create a new file named `app.js`:

   ```bash
   touch app.js
   ```

2. Add the following code to `app.js`:

   ```javascript
   const express = require('express');
   const app = express();
   const port = 3000;

   app.get('/', (req, res) => {
       res.send('Hello, Node.js!');
   });

   app.listen(port, () => {
       console.log(`Server is running at http://localhost:${port}`);
   });
   ```

### Step 5: Run the Application

1. Start the server:

   ```bash
   node app.js
   ```

2. Open your browser and navigate to `http://localhost:3000`. You should see the message "Hello, Node.js!".

---

## Challenge Step

1. Modify `app.js` to include two additional routes:

   - `/hi`: Returns "Hi there!"
   - `/bye`: Returns "Goodbye!"

2. Update your `package.json` to include a custom script to start your application:

   ```json
   "scripts": {
       "start": "node app.js"
   }
   ```

3. Run the application using npm:

   ```bash
   npm start
   ```

4. Test all routes in your browser:

   - `http://localhost:3000/`
   - `http://localhost:3000/hi`
   - `http://localhost:3000/bye`

---

## Additional Resources

- [Node.js Documentation](https://nodejs.org/docs/latest-v20.x/)
- [npm Documentation](https://docs.npmjs.com/)

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## **Contact**
For questions or feedback, feel free to reach out:
- **Email**: eyal@levys.co.il
- **GitHub**: [https://github.com/elevy99927](https://github.com/elevy99927)

---
