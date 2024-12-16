# Lab 3: Web Server

## Objective
This lab focuses on creating and deploying a basic web server using Node.js. 
By the end of this lab, you will understand how to serve HTML content and handle HTTP requests and responses in Node.js.

---

## What is Node.js?
Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine. 
It is designed for building scalable network applications and can be used to create web servers, APIs, and more.

[Learn more about Node.js](https://nodejs.org/)

## What is nvm?
NVM (Node Version Manager) is a tool that allows you to manage multiple versions of Node.js on a single machine. With NVM, you can easily switch between Node.js versions, making it especially useful for projects requiring specific versions.

To install nvm, follow the instructions on the [official nvm repository](https://github.com/nvm-sh/nvm).

---

## Prerequisites

1. **Node.js**:
   - Install Node.js using nvm or directly from the [official Node.js website](https://nodejs.org/).
   - Verify installation:
     ```bash
     node -v
     npm -v
     ```

2. **Text Editor**: Use a code editor like Visual Studio Code or any editor of your choice.

---

## Lab Instructions

### Step 1: Initialize the Project

1. Create a new directory for the project and navigate to it:
   ```bash
   mkdir web-server-lab
   cd web-server-lab
   ```

2. Initialize a new Node.js project:
   ```bash
   npm init -y
   ```
   This command generates a `package.json` file with default settings.

### Step 2: Install Dependencies

1. Install the `express` package to simplify creating the web server:
   ```bash
   npm install express
   ```

### Step 3: Write the Web Server Code

1. Create a new file `index.js` in the project directory.
2. Add the following code to set up a basic web server:
   ```javascript
   const express = require('express');
   const app = express();

   app.get('/', (req, res) => {
       res.send('Welcome to the Web Server Lab!');
   });

   app.get('/about', (req, res) => {
       res.send('This is a basic web server built with Node.js and Express.');
   });

   app.listen(3000, () => {
       console.log('Server is running on http://localhost:3000');
   });
   ```

### Step 4: Run the Server

1. Start the server:
   ```bash
   node index.js
   ```

2. Open your browser and navigate to:
   - `http://localhost:3000` for the homepage.
   - `http://localhost:3000/about` for the about page.

---

## Challenge Step

Enhance the web server to include:

1. A `/contact` route that returns contact information (e.g., `Contact me at: eyal@levys.co.il`).
2. A `/time` route that dynamically returns the current server time.

**Solution**:
1. Modify `index.js` to include the new routes:
   ```javascript
   app.get('/contact', (req, res) => {
       res.send('Contact me at: eyal@levys.co.il');
   });

   app.get('/time', (req, res) => {
       const currentTime = new Date().toLocaleTimeString();
       res.send(`The current server time is: ${currentTime}`);
   });
   ```
2. Restart the server and test the new routes:
   - `http://localhost:3000/contact`
   - `http://localhost:3000/time`

---

## Additional Resources

- [Node.js Documentation](https://nodejs.org/en/docs/)
- [Express.js Documentation](https://expressjs.com/)
- [nvm GitHub Repository](https://github.com/nvm-sh/nvm)

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
## **Contact**
For questions or feedback, feel free to reach out:
- **Email**: eyal@levys.co.il
- **GitHub**: [https://github.com/elevy99927](https://github.com/elevy99927)

---