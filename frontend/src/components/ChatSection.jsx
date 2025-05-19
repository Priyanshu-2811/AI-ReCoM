import React, { useState } from "react";

export default function ChatSection({ pdfUploaded }) {
  const [question, setQuestion] = useState("");

  const handleAsk = () => {
    if (question) {
      // send question to backend
      console.log("Asked:", question);
    }
  };

  return (
    <div className="chat-card">
      <h2>Ask a Question</h2>
      <input
        type="text"
        value={question}
        placeholder="Ask something about your research paper..."
        onChange={e => setQuestion(e.target.value)}
      />
      <button onClick={handleAsk} disabled={!pdfUploaded || !question}>
        Ask
      </button>
    </div>
  );
}
