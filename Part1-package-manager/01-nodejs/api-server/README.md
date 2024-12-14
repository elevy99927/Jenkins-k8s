
# Node.js Application Example

This is a simple Node.js application built using **Express**, designed to demonstrate basic functionality such as handling GET and POST requests. The app also utilizes **dotenv** for managing environment variables, **cors** for handling cross-origin requests, and includes **nodemon** as a development dependency for easier debugging.

---

## **Features**
- Serves a welcome message at the root endpoint (`/`).
- Handles GET requests at `/api/hello` to return a JSON message.
- Handles POST requests at `/api/data` to receive and respond with JSON data.

---

## **Prerequisites**
Ensure you have the following installed on your system:
- **Node.js** (Version 22 or later)
- **npm** (Node Package Manager, included with Node.js)

---

## **Project Structure**
```
node-app/
├── app.js          # Main application file
├── package.json    # Dependency and script definitions
├── math.js         # A simple js script to sum 2 numbers
├── app.test.js     # A test script for 'npm test' example
├── .env            # Environment variables (create manually)
└── README.md       # Documentation
```

---


## **Installation**

### Step 1: Clone the Repository
```bash
git clone https://github.com/elevy99927/Jenkins-k8s.git
cd ./Part1-package-manager/01-simple-nodejs/api-server
```

### Step 2: Install Dependencies
Install all required dependencies listed in the `package.json` file:
```bash
npm install
```

### Step 3: Configure Environment Variables
Create a `.env` file in the root of the project and add the following:
```env
PORT=3000
```
This allows you to define the port the application will run on.

---

## **Running the Application**

### To Start the Application:
Run the following command:
```bash
npm start
```
The server will start and listen on the port defined in your `.env` file (default is `3000`).

### To Run in Development Mode:
Use `nodemon` to automatically restart the server upon file changes:
```bash
npm run dev
```

---

## **Endpoints**

### 1. **GET /** 
- **URL:** `http://localhost:3000/`
- **Description:** Returns a welcome message.
- **Response:** 
  ```
  Welcome to the Node.js App!
  ```

### 2. **GET /api/hello**
- **URL:** `http://localhost:3000/api/hello`
- **Description:** Returns a JSON message.
- **Response:**
  ```json
  {
    "message": "Hello, World!"
  }
  ```

### 3. **POST /api/data**
- **URL:** `http://localhost:3000/api/data`
- **Description:** Accepts JSON data and returns it as part of the response.
- **Request Body:**
  ```json
  {
    "data": "your input data"
  }
  ```
- **Response:**
  ```json
  {
    "message": "You sent: your input data"
  }
  ```
---


## **Dependencies**
### Production:
- **express**: Handles routing and server responses.
- **dotenv**: Loads environment variables from a `.env` file.
- **cors**: Enables Cross-Origin Resource Sharing.

### Development:
- **nodemon**: Restarts the server automatically when changes are made.

---

## **Example Usage**

1. **Testing GET Request**:
   Use a browser or a tool like `curl`:
   ```bash
   curl http://localhost:3000/api/hello
   ```
   Response:
   ```json
   {
     "message": "Hello, World!"
   }
   ```

2. **Testing POST Request**:
   Send a POST request with JSON data:
   ```bash
   curl -X POST http://localhost:3000/api/data -H "Content-Type: application/json" -d '{"data":"test data"}'
   ```
   Response:
   ```json
   {
     "message": "You sent: test data"
   }
   ```
---

## Unit Test Example

### Definition of Unit Test
A <b>unit test</b> is a test that checks the functionality of a specific, small "unit" of code in isolation, typically a function or a method. Unit tests focus on:

<b>Isolated testing:</b> No dependencies on external systems (e.g., databases, file systems, or APIs).
<b>Targeted scope:</b> Only the logic of the unit being tested is verified.


### Update Package.json
Add this to your `package.json`
```bash
"scripts": {
  "test": "jest"
}
```
### Install Jest
Run the following command to install Jest:
```bash
npm install --save-dev jest

```

### Create a Test File

Create a test file named `app.test.js` in the root directory:
```bash
// app.test.js
const { add } = require('./math'); 

test('adds 1 + 2 to equal 3', () => {
    expect(add(1, 2)).toBe(3);
});

test('adds -1 + -1 to equal -2', () => {
    expect(add(-1, -1)).toBe(-2);
});

```
 
### Run Tests
Run the tests using the command:
```bash
npm test

```

Expected output:
```bash
PASS  ./npm.test.js
✓ adds 1 + 2 to equal 3 (5 ms)
✓ adds -1 + -1 to equal -2 (1 ms)

Test Suites: 1 passed, 1 total
Tests:       2 passed, 2 total
Snapshots:   0 total
Time:        1.2 s
Ran all test suites.

```

### Summary
<li>Jest is used as the testing framework.
<li>A simple function add is tested for correctness.
<li>You can expand this approach to test more complex functionalities.


---

## **Development**
- To edit the application, make changes in `app.js`.
- Use `npm run dev` to watch for changes and restart the server automatically.

---


## License

This project is licensed under the MIT License.

---
## **Contact**
For questions or feedback, feel free to reach out:
- **Email**: eyal@levys.co.il
- **GitHub**: [https://github.com/elevy99927](https://github.com/elevy99927)

---

### **How to Use**
1. Copy and save this content as `README.md` in the root directory of your project.
2. Share it with your project repository or include it with your codebase.

Let me know if you'd like additional sections or details!

