
# Lab: Node.js API Server

## Objective

This lab focuses on creating and testing a simple API server using **Node.js** and **Express**. By the end of this lab, you will:

1. Understand how to set up a Node.js project with **Express**.
2. Learn how to handle **GET** and **POST** requests.
3. Use **curl** to test your API endpoints.

---

## Prerequisites

1. **Node.js** installed on your system.
   - [Download Node.js](https://nodejs.org/en/)
2. A code editor (e.g., VSCode).
3. Basic understanding of the command line and HTTP requests.

---

## Step 1: Set Up the Project

1. Create a project directory:
   ```bash
   mkdir api-server-lab
   cd api-server-lab
   ```

2. Initialize a new Node.js project:
   ```bash
   npm init -y
   ```

3. Install **Express**:
   ```bash
   npm install express
   ```

---

## Step 2: Create the API Server

1. Create a file named `server.js` in the root directory and add the following code:
<BR><B>Don't forget to check the `.env` file.</B> 

   ```javascript
   const express = require('express');
   const app = express();
   const PORT = 5000;

   // Middleware to parse JSON data
   app.use(express.json());

   // GET endpoint
   app.get('/', (req, res) => {
       res.send('Welcome to the API Server Lab!');
   });

   app.get('/api/hello', (req, res) => {
       res.json({ message: 'Hello, World!' });
   });

   // POST endpoint
   app.post('/api/data', (req, res) => {
       const inputData = req.body.data;
       res.json({ message: `You sent: ${inputData}` });
   });

   // Start the server
   app.listen(PORT, () => {
       console.log(`Server is running on http://localhost:${PORT}`);
   });
   ```

---

## Step 3: Run the Server

1. Start the server:
   ```bash
   node server.js
   ```

2. The server will run on `http://localhost:3000`.

---

## Step 4: Test the API Using `curl`

Use the following `curl` commands to test the endpoints.

### 1. Test the Root Endpoint (`GET /`)

Run:
```bash
curl http://localhost:3000/
```
Response:
```
Welcome to the API Server Lab!
```

### 2. Test the `GET /api/hello` Endpoint

Run:
```bash
curl http://localhost:3000/api/hello
```
Response:
```json
{
  "message": "Hello, World!"
}
```

### 3. Test the `POST /api/data` Endpoint

Run:
```bash
curl -X POST http://localhost:3000/api/data -H "Content-Type: application/json" -d '{"data": "test input"}'
```
Response:
```json
{
  "message": "You sent: test input"
}
```

---

## Challenge Step

1. Modify the API server to include the following endpoints:
   - **GET /api/time**: Returns the current server time.
   - **POST /api/echo**: Returns the same JSON data sent in the request.

2. Test the new endpoints using `curl`:
   ```bash
   curl http://localhost:3000/api/time
   curl -X POST http://localhost:3000/api/echo -H "Content-Type: application/json" -d '{"key": "value"}'
   ```

**Solution Example**:

Add these routes to `server.js`:

```javascript
app.get('/api/time', (req, res) => {
    const currentTime = new Date().toISOString();
    res.json({ time: currentTime });
});

app.post('/api/echo', (req, res) => {
    res.json(req.body);
});
```

---

## Additional Resources

- [Node.js Documentation](https://nodejs.org/en/docs/)
- [Express.js Documentation](https://expressjs.com/)
- [curl Command Reference](https://curl.se/docs/manual.html)

---

## License

This project is licensed under the **MIT License**.

---
## **Contact**
For questions or feedback, feel free to reach out:
- **Email**: eyal@levys.co.il
- **GitHub**: [https://github.com/elevy99927](https://github.com/elevy99927)

---

