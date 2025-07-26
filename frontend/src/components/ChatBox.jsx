import React, { useState } from "react";

function ChatBox() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const handleSend = async () => {
    const res = await fetch("http://localhost:5000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: input })
    });
    const data = await res.json();
    setMessages([...messages, { user: input, bot: data.response }]);
    setInput("");
  };

  return (
    <div>
      <h2>Chat with Support Bot</h2>
      <div>
        {messages.map((msg, idx) => (
          <div key={idx}>
            <b>You:</b> {msg.user} <br />
            <b>Bot:</b> {JSON.stringify(msg.bot)}
            <hr />
          </div>
        ))}
      </div>
      <input value={input} onChange={(e) => setInput(e.target.value)} />
      <button onClick={handleSend}>Send</button>
    </div>
  );
}

export default ChatBox;
