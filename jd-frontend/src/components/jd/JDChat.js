import React, { useState } from "react";
import LoadingSpinner from "../common/LoadingSpinner";

export default function JDChat({ onQuery, loading, result }) {
  const [query, setQuery] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;
    await onQuery(query.trim());
  };

  return (
    <div>
      <form onSubmit={handleSubmit} style={{ marginBottom: "1rem" }}>
        <input
          type="text"
          value={query}
          placeholder="Ask about job descriptions..."
          onChange={(e) => setQuery(e.target.value)}
          style={{ width: "60%", marginRight: "0.5rem" }}
          required
        />
        <button type="submit" disabled={loading}>
          Ask
        </button>
      </form>

      {loading && <LoadingSpinner />}

      {result && (
        <div style={{ backgroundColor: "#fff", padding: "1rem", borderRadius: "4px" }}>
          <h3>Answer:</h3>
          <p>{result.answer}</p>
          <h4>Sources:</h4>
          <ul>
            {result.sources.map((source, idx) => (
              <li key={idx}>{JSON.stringify(source)}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
