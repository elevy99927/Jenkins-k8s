# Node.js Advanced Lab

## Objectives

This lab is designed to introduce students to advanced concepts in Node.js development. By the end of this lab, students will learn:
1. **Using `nodemon`**: Automate server restarts during development.
2. **Debugging Node.js Applications**: Use built-in tools like `--inspect` and `jdb`.
3. **Writing Modular Code**: Create and use custom Node.js modules for better project structure.
4. **Using External APIs**: Fetch and display data using `axios` or `node-fetch`.

---

## Prerequisites

- **Node.js** (installed using NVM is recommended).
- **Basic understanding** of JavaScript, HTTP requests, and prior Node.js concepts.

---

## Lab Instructions

### Step 1: Setup Your Project

1. **Create a new project directory** and navigate into it:
   ```bash
   mkdir nodejs-advanced
   cd nodejs-advanced
   ```

2. **Initialize a new Node.js project**:
   ```bash
   npm init -y
   ```

3. **Install required dependencies**:
   - **express** for creating a server
   - **axios** for making HTTP requests
   - **nodemon** for automated server restarts during development
   ```bash
   npm install express axios
   npm install --save-dev nodemon
   ```

4. **Configure `nodemon`** in `package.json`:
   Add the following under `"scripts"`:
   ```json
   "scripts": {
       "start": "node index.js",
       "dev": "nodemon index.js"
   }
   ```

---

### Step 2: Write a Modular Web Server

#### Project Structure:
Organize your project as follows:
```
nodejs-advanced/
│
├── index.js
├── routes/
│   └── api.js
├── middleware/
│   └── logger.js
└── package.json
```

1. **Create a Logger Middleware**:  
   In `middleware/logger.js`:
   ```javascript
   const logger = (req, res, next) => {
       console.log(`${new Date().toISOString()} - ${req.method} - ${req.url}`);
       next();
   };

   module.exports = logger;
   ```

2. **Set Up Routes to Use External APIs**:  
   In `routes/api.js`:
   ```javascript
   const express = require('express');
   const axios = require('axios');
   const router = express.Router();

   // GET weather data from OpenWeatherMap API
   router.get('/weather', async (req, res) => {
       try {
           const response = await axios.get('https://api.openweathermap.org/data/2.5/weather', {
               params: {
                   q: 'London',
                   appid: 'your_api_key_here'
               }
           });
           res.json(response.data);
       } catch (error) {
           res.status(500).json({ error: 'Unable to fetch weather data' });
       }
   });

   module.exports = router;
   ```

3. **Create the Main Server**:  
   In `index.js`:
   ```javascript
   const express = require('express');
   const logger = require('./middleware/logger');
   const apiRoutes = require('./routes/api');

   const app = express();

   // Middleware
   app.use(logger);

   // Routes
   app.use('/api', apiRoutes);

   // Default Route
   app.get('/', (req, res) => {
       res.send('Welcome to the Node.js Advanced Lab!');
   });

   // Start Server
   const PORT = 3000;
   app.listen(PORT, () => {
       console.log(`Server running at http://localhost:${PORT}/`);
   });
   ```

---

### Step 3: Run and Debug the Server

1. Start the server using **nodemon** for automatic reloads:
   ```bash
   npm run dev
   ```

2. Open the following endpoints in your browser or use `curl`:
   - `http://localhost:3000/` (Main page)
   - `http://localhost:3000/api/weather` (Fetch weather data).

3. Debug the server:
   - Run the application in debug mode:
     ```bash
     node --inspect index.js
     ```
   - Open `chrome://inspect` in your browser to attach to the Node.js debugger.

---

## Part 4: Challenge Step

Add a new route that fetches jokes from the **icanhazdadjoke** API.

1. Update `routes/api.js`:
   ```javascript
   router.get('/jokes', async (req, res) => {
       try {
           const response = await axios.get('https://icanhazdadjoke.com/', {
               headers: { Accept: 'application/json' }
           });
           res.json(response.data);
       } catch (error) {
           res.status(500).json({ error: 'Unable to fetch jokes' });
       }
   });
   ```

2. Restart the server and test the new endpoint:
   ```bash
   curl http://localhost:3000/api/jokes
   ```

---

## Resources

- [Node.js Documentation](https://nodejs.org/)
- [Express.js Documentation](https://expressjs.com/)
- [Using `nodemon`](https://www.npmjs.com/package/nodemon)
- [Axios Documentation](https://axios-http.com/)
- [icanhazdadjoke API](https://icanhazdadjoke.com/)

---

## License

This project is licensed under the MIT License.

---

## **Contact**

For questions or feedback, feel free to reach out:
- **Email**: eyal@levys.co.il
- **GitHub**: [https://github.com/elevy99927](https://github.com/elevy99927)

---