import React, { useState } from "react";

export default function UploadSection({ onPdfUpload }) {
  const [file, setFile] = useState(null);

  const handleUpload = () => {
    if (file) {
      // Call backend upload API here
      onPdfUpload();
    }
  };

  return (
    <div className="upload-card">
      <h2>Upload Research PDF</h2>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleUpload} disabled={!file}>
        Upload & Summarize
      </button>
    </div>
  );
}
