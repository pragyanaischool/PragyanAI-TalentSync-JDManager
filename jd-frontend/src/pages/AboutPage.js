import React from "react";

export default function AboutPage() {
  return (
    <div style={{ padding: "2rem" }}>
      <h1>About JD Management App</h1>
      <p>
        This application enables creating, parsing, and querying Job Descriptions (JDs) 
        leveraging AI-powered retrieval and generation.
      </p>
      <p>
        Built with React.js frontend and FastAPI backend, integrated with LangChain, GROQ LLMs,
        HuggingFace embeddings, and MongoDB Atlas vector search.
      </p>
      <p>
        Developed to facilitate efficient administration and intelligent querying of job listings.
      </p>
    </div>
  );
}
