import React from "react";
import ChatBox from "./components/ChatBox";
import Chatbot from "./Chatbot";

function App() {
  return (
    <div className="App">
      <h2 style={{ textAlign: "center" }}>E-commerce Chatbot</h2>
      {/* You can choose which component to show, or both if needed */}
      <ChatBox />
      <Chatbot />
    </div>
  );
}

export default App;
