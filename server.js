const express = require('express');
const axios = require('axios');
const cors = require('cors');
const app = express();
const port = 3000;

// Enable CORS
app.use(cors());

// Enable JSON parsing for POST requests
app.use(express.json());

// Endpoint to get the chatbot response
app.post('/get-chatbot-response', async (req, res) => {
  const userMessage = req.body.message;
  console.log('User Message:', userMessage);

  try {
    // URL-encode the user message to safely use it in the query
    const encodedMessage = encodeURIComponent(userMessage);
    console.log('Encoded Message:', encodedMessage); // Log the encoded message

    // Construct the query using `match` for flexible matching
    const query = `*[_type == "message" && text match "${encodedMessage}"]`;
    console.log('Query:', query); // Log the query being sent to Sanity

    // URL encode the entire query to handle special characters
    const encodedQuery = encodeURIComponent(query);
    console.log('Encoded Query:', encodedQuery); // Log the fully encoded query

    // Make the axios request to Sanity with the encoded query
    const response = await axios.get(
      `https://wvz3v2zm.api.sanity.io/v1/data/query/production?query=${encodedQuery}`,
      {
        headers: {
          'Authorization': 'Bearer sk3Z7iiqnBMZdln3Url1nHPUAkTd4clbdEB9ORF9T4f02mK4IwZxF8aIiZBnCd5RsucnWfCDezfinUnNxtlO40dLHDWTaezWppSandCtYlwpPYpxpxFbygTY4sNPF7RqsREJaomyCvIfcSf498vmblFyHmHIwRB9mG9FKA9YUydBtVb3NBEh', // Replace with your API token
        }
      }
    );

    console.log('Sanity Response:', response.data); // Log the full response from Sanity

    // Send back the response from Sanity
    const chatbotResponse = response.data.result[0]
      ? response.data.result[0].response
      : "Sorry, I didn't understand that.";

    res.json({ reply: chatbotResponse });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Failed to fetch data from Sanity" });
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
