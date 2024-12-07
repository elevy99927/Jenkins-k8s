// Import required modules
const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');

// Initialize environment variables
dotenv.config();

// Initialize express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.get('/', (req, res) => {
    res.send('Welcome to the Node.js App!');
});

app.get('/api/hello', (req, res) => {
    res.json({ message: 'Hello, World!' });
});

app.post('/api/data', (req, res) => {
    const { data } = req.body;
    res.json({ message: `You sent: ${data}` });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
