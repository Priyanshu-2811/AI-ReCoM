import React, { useState } from "react";
import LoginForm from "./components/LoginForm";
import UploadSection from "./components/UploadSection";
import ChatSection from "./components/ChatSection";
import "./styles.css";

export default function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [pdfUploaded, setPdfUploaded] = useState(false);

  return (
    <div className="app-container">
      {!isLoggedIn ? (
        <LoginForm onLoginSuccess={() => setIsLoggedIn(true)} />
      ) : (
        <>
          <h2>Welcome! Choose what you'd like to do:</h2>
          <UploadSection onPdfUpload={() => setPdfUploaded(true)} />
          <ChatSection pdfUploaded={pdfUploaded} />
        </>
      )}
    </div>
  );
}
