import React, { useState } from "react";
import { useJdApi } from "../hooks/useJdApi";
import JDUrlInput from "../components/jd/JDUrlInput";
import JDUpload from "../components/jd/JDUpload";
import JDChat from "../components/jd/JDChat";

export default function HomePage() {
  const { loading, error, createFromUrl, createFromFile, queryJDs } = useJdApi();

  const [queryResult, setQueryResult] = useState(null);

  // Handle form submission for URL
  const handleUrlSubmit = async (url) => {
    try {
      await createFromUrl(url);
      alert("Job description added from URL!");
    } catch (err) {
      alert("Failed to add JD from URL: " + err.message);
    }
  };

  // Handle file upload
  const handleFileUpload = async (file) => {
    try {
      await createFromFile(file);
      alert("Job description added from file!");
    } catch (err) {
      alert("Failed to add JD from file: " + err.message);
    }
  };

  // Handle querying JDs
  const handleQuery = async (query) => {
    try {
      const result = await queryJDs(query);
      setQueryResult(result);
    } catch (err) {
      alert("Error querying JDs: " + err.message);
    }
  };

  return (
    <div>
      <h1>Job Description Management</h1>
      <JDUrlInput onSubmit={handleUrlSubmit} />
      <JDUpload onUpload={handleFileUpload} />
      <JDChat onQuery={handleQuery} loading={loading} result={queryResult} />
      {error && <p style={{ color: "red" }}>Error: {error}</p>}
    </div>
  );
}
