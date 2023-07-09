const express = require('express');
const axios = require('axios');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// ChatGPT API endpoint
const chatGptApiUrl = 'https://api.openai.com/v1/chat/completions';

// ChatGPT API configuration
const chatGptApiKey = '<YOUR_CHATGPT_API_KEY>';
const chatGptModelId = 'gpt-3.5-turbo';

// Code Conversion Service
app.post('/convert', (req, res) => {
    const code = req.body.code;
    const targetLanguage = req.body.targetLanguage;

    // Make API request for code conversion and handle the response
    // Return the converted code in the response
    const convertedCode = `Converted code in ${targetLanguage}:\n ...`;
    res.send(convertedCode);
});

// Code Debugging Service
app.post('/debug', (req, res) => {
    const code = req.body.code;

    // Make API request for code debugging and handle the response
    // Return the debugging output in the response
    const debuggingOutput = `Debugging output:\n ...`;
    res.send(debuggingOutput);
});

// Code Quality Check Service
app.post('/qualitycheck', (req, res) => {
    const code = req.body.code;

    // Make API request for code quality check and handle the response
    // Return the quality assessment in the response
    const qualityAssessment = `Quality Assessment:\n ...`;
    res.send(qualityAssessment);
});

// ChatGPT API endpoint
app.post('/chat', async (req, res) => {
    const message = req.body.message;

    try {
        // Make API request to ChatGPT API
        const response = await axios.post(chatGptApiUrl, {
            messages: [{ role: 'system', content: 'You are a user' }, { role: 'user', content: message }],
            model: chatGptModelId,
            key: chatGptApiKey,
        });

        // Extract and return the model's response
        const chatResponse = response.data.choices[0].message.content;
        res.send(chatResponse);
    } catch (error) {
        console.error('Error:', error.message);
        res.status(500).send('An error occurred.');
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
