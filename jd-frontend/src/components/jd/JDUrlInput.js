import React, { useState } from "react";

export default function JDUrlInput({ onSubmit }) {
  const [url, setUrl] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!url.trim()) return alert("URL cannot be empty");
    onSubmit(url.trim());
    setUrl("");
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: "1rem" }}>
      <label>
        Enter JD URL:
        <input
          type="url"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="https://example.com/job-description"
          required
          style={{ width: "300px", marginLeft: "0.5rem" }}
        />
      </label>
      <button type="submit" style={{ marginLeft: "0.5rem" }}>
        Submit
      </button>
    </form>
  );
}
