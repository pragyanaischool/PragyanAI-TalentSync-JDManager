import React, { useState } from "react";

export default function JDForm({ onSubmit }) {
  const [title, setTitle] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (title.trim() === "") return alert("Title is required");
    onSubmit({ title });
    setTitle("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Job Title:
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Enter job title"
          required
        />
      </label>
      <button type="submit">Create JD</button>
    </form>
  );
}
