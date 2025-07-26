import React, { useState } from "react";

function Chatbot() {
  const [messages, setMessages] = useState([{ sender: "bot", text: "Hi! How can I help you?" }]);
  const [input, setInput] = useState("");

  async function sendMessage(e) {
    e.preventDefault();
    const msg = input.trim();
    if (!msg) return;
    setMessages([...messages, { sender: "user", text: msg }]);
    setInput("");

    const resp = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: msg })
    });
    const data = await resp.json();
    setMessages(ds => [...ds, { sender: "bot", text: data.reply }]);
  }

  return (
    <div style={{
      maxWidth: 450, margin: "40px auto", border: "1px solid #999",
      borderRadius: 8, padding: 20, background: "#f9f9f9"
    }}>
      <div style={{ minHeight: 200, marginBottom: 10 }}>
        {messages.map((m, i) => (
          <div key={i} style={{
            textAlign: m.sender === "bot" ? "left" : "right",
            margin: "8px 0"
          }}>
            <span style={{
              background: m.sender === "bot" ? "#e6e6e6" : "#caeaff",
              borderRadius: 12,
              padding: "7px 12px",
              display: "inline-block"
            }}>{m.text}</span>
          </div>
        ))}
      </div>
      <form onSubmit={sendMessage} style={{ display: "flex" }}>
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          style={{ flex: 1, padding: "8px", borderRadius: 8, border: "1px solid #ccc" }}
          placeholder="Type your question about orders or products..."
        />
        <button style={{ marginLeft: 8, padding: "8px 16px", borderRadius: 8 }} type="submit">Send</button>
      </form>
    </div>
  );
}

export default Chatbot;
