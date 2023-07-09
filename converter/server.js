const express = require('express');
const dotenv = require('dotenv');
const path = require('path');
const cors = require('cors');
const { Configuration, OpenAIApi } = require("openai");

dotenv.config();

const app = express();
const port = 4000;

app.use(express.json());
app.use(cors());

const configuration = new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);
const model = "text-davinci-003";

async function generateCompletion(prompt) {
    try {
        const response = await openai.createCompletion({
            model,
            prompt,
            max_tokens: 500,
            n: 1
        });

        const { choices } = response.data;
        if (choices && choices.length > 0) {
            const completion = choices[0].text.trim();
            return completion;
        } else {
            return false;
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

app.use(express.static(path.join(__dirname, 'public')));

app.post('/convert', async (req, res) => {
    try {
        const { code, fromLanguage, toLanguage } = req.body;
        const prompt = (fromLanguage && toLanguage) ?
            `Convert the following ${fromLanguage} code to ${toLanguage} code:\n${code}` :
            `Convert the following code:\n${code}`;

        const response = await generateCompletion(prompt);
        console.log(response);
        res.json({ response });
    } catch (error) {
        handleError(res, error);
    }
});

app.post('/debug', async (req, res) => {
    try {
        const { code } = req.body;
        const prompt = `Debug the following code: ${code}. Please check if there are any errors and correct them. Also, if it's correct, provide steps explaining what the code is doing and how we can improve it.`;
        const response = await generateCompletion(prompt);
        res.json({ response });
    } catch (error) {
        handleError(res, error);
    }
});

app.post('/quality', async (req, res) => {
    try {
        const { code } = req.body;
        const prompt = `Check the quality of the following code: ${code}. Please provide detailed information and also provide some tips to improve, in bullet points.`;
        const response = await generateCompletion(prompt);
        res.json({ response });
    } catch (error) {
        handleError(res, error);
    }
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});
