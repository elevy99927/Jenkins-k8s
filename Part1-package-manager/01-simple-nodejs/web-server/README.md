### **README.md**

# Simple Node.js Web Server

This is a simple Node.js web server application that serves different responses based on the accessed URL. The server includes the following endpoints:
- `/` -> Displays: "This is a test page"
- `/hi` -> Displays: "Hello"
- `/bye` -> Displays: "Bye Bye"
- Any other route returns a 404 with: "Page not found"

## Prerequisites

1. Install **nvm** (Node Version Manager) to manage Node.js versions.
2. Install **Node.js 20** using nvm.

## Installing nvm

To install nvm, run the following command:

### Linux/macOS:
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
```

After installation, restart your terminal and verify:
```bash
nvm --version
```

### Windows:
Download and install [nvm for Windows](https://github.com/coreybutler/nvm-windows/releases).

## Installing Node.js

Using nvm, install Node.js version 20:
```bash
nvm install 20
```

Set Node.js 20 as the default version:
```bash
nvm use 20
nvm alias default 20
```

Verify Node.js installation:
```bash
node -v
npm -v
```

## Running the Application

1. Clone this repository or copy the `server.js` file into your project directory.

2. Navigate to the directory containing the `server.js` file:
```bash
cd /path/to/directory
```

3. Start the server:
```bash
node server.js
```

4. The server will start and listen on `http://localhost:3000`.

## Testing the Application
Use your browser or any HTTP client (e.g., [Postman](https://www.postman.com/) or `curl`) to test the endpoints:
<I>Please refer to the 'install-node.txt' file </I>

### Endpoints:
- Access `/`:
  ```bash
  curl http://localhost:3000/
  ```
  Response: `This is a test page`

- Access `/hi`:
  ```bash
  curl http://localhost:3000/hi
  ```
  Response: `Hello`

- Access `/bye`:
  ```bash
  curl http://localhost:3000/bye
  ```
  Response: `Bye Bye`

- Access an unknown route:
  ```bash
  curl http://localhost:3000/unknown
  ```
  Response: `Page not found`

## Future Enhancements

- Add JSON responses.
- Use the Express framework for more advanced route handling.
- Implement unit tests for the application.

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