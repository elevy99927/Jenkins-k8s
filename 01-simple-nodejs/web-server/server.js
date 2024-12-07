// Import the built-in HTTP module
const http = require('http');

// Define the server logic
const server = http.createServer((req, res) => {
    // Set the response header
    res.setHeader('Content-Type', 'text/plain');

    // Route handling
    if (req.url === '/') {
        res.statusCode = 200; // OK
        res.end('This is a test page');
    } else if (req.url === '/hi') {
        res.statusCode = 200; // OK
        res.end('Hello');
    } else if (req.url === '/bye') {
        res.statusCode = 200; // OK
        res.end('Bye Bye');
    } else {
        res.statusCode = 404; // Not Found
        res.end('Page not found');
    }
});

// Start the server
const PORT = 3000; // You can change this port
server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
});
