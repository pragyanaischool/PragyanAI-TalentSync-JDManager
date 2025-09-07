const API_BASE_URL = process.env.REACT_APP_API_URL || "http://localhost:8000/api";

export async function createJDFromUrl(url) {
  const response = await fetch(`${API_BASE_URL}/jds/create-from-url`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ url }),
  });

  if (!response.ok) {
    throw new Error(`Error creating JD from URL: ${response.statusText}`);
  }
  return response.json();
}

export async function createJDFromFile(file) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${API_BASE_URL}/jds/create-from-file`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error(`Error creating JD from file: ${response.statusText}`);
  }
  return response.json();
}

export async function queryJDs(query) {
  const response = await fetch(`${API_BASE_URL}/jds/query`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ query }),
  });

  if (!response.ok) {
    throw new Error(`Error querying JDs: ${response.statusText}`);
  }
  return response.json();
}
