document.getElementById("send-btn").addEventListener("click", async () => {
    const userInput = document.getElementById("user-input").value;
    if (!userInput) return;
  
    // Display user's message
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
  
    // Clear input field
    document.getElementById("user-input").value = "";
  
    // Call the backend to fetch a chatbot response
    const response = await fetch("http://localhost:3000/get-chatbot-response", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: userInput })
    });
  
    const data = await response.json();
  
    // Display chatbot's response
    chatBox.innerHTML += `<p><strong>Chatbot:</strong> ${data.reply}</p>`;
  });
  