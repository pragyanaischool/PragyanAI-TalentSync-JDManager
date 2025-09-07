import React, { useRef } from "react";

export default function JDUpload({ onUpload }) {
  const fileInputRef = useRef();

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const supportedTypes = [
      "application/pdf",
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ];
    if (!supportedTypes.includes(file.type)) {
      alert("Only PDF and DOCX files are supported.");
      fileInputRef.current.value = "";
      return;
    }

    onUpload(file);
    fileInputRef.current.value = ""; // reset to allow re-upload of same file if needed
  };

  return (
    <div style={{ marginBottom: "1rem" }}>
      <label htmlFor="file-upload">Upload JD File (PDF or DOCX): </label>
      <input
        id="file-upload"
        type="file"
        accept=".pdf,.docx"
        ref={fileInputRef}
        onChange={handleFileChange}
      />
    </div>
  );
}
