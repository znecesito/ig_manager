import React, { useState } from "react";

function App() {
  const [followers, setFollowers] = useState(null);
  const [following, setFollowing] = useState(null);
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResult(null);

    if (!followers || !following) {
      alert("Please upload both files");
      return;
    }

    const formData = new FormData();
    formData.append("followers", followers);
    formData.append("following", following);

    try {
      const res = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await res.json().catch(() => {
        throw new Error("Response was not valid JSON");
      });

      if (!res.ok || data.error) {
        throw new Error(data.error || "Server returned an error");
      }
      //console.log(data)
      setResult(data);
    } catch (err) {
      console.error("Upload failed:", err);
      alert("Something went wrong. Please make sure you uploaded the correct files.");
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Follower Analyzer</h1>
      <p style={styles.subtitle}>Upload your followers and following JSON files to compare.</p>

      <form onSubmit={handleSubmit} style={styles.form}>
        <div style={styles.inputGroup}>
          <label style={styles.label}>Followers JSON</label>
          <input
            type="file"
            accept=".json"
            onChange={(e) => setFollowers(e.target.files[0])}
            style={styles.input}
          />
        </div>
        <div style={styles.inputGroup}>
          <label style={styles.label}>Following JSON</label>
          <input
            type="file"
            accept=".json"
            onChange={(e) => setFollowing(e.target.files[0])}
            style={styles.input}
          />
        </div>
        <button type="submit" style={styles.button}>
          Upload & Analyze
        </button>
      </form>

      {result && (
        <div style={styles.results}>
          {/* Render any array fields */}
          {Object.entries(result).map(([key, value]) => {
            if (Array.isArray(value)) {
              return (
                <div key={key} style={{ marginBottom: "1.5rem" }}>
                  <h3 style={{ textTransform: "capitalize", marginBottom: "0.5rem" }}>
                    {key.replace(/_/g, " ")} ({value.length})
                  </h3>
                  <ul style={styles.list}>
                    {value.map((username, index) => (
                      <li key={index} style={styles.listItem}>
                        <a
                          href={`https://www.instagram.com/${username}`}
                          target="_blank"
                          rel="noopener noreferrer"
                          style={styles.link}
                        >
                          instagram.com/{username}
                        </a>
                      </li>
                    ))}
                  </ul>
                </div>
              );
            }
            return null;
          })}
        </div>
      )}
    </div>
  );
}

// 💄 Inline style objects for simplicity
const styles = {
  container: {
    maxWidth: "600px",
    margin: "4rem auto",
    padding: "2rem",
    borderRadius: "12px",
    background: "#f9f9fb",
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
    fontFamily: "Inter, system-ui, sans-serif",
    color: "#333",
  },
  title: {
    fontSize: "1.8rem",
    marginBottom: "0.5rem",
    textAlign: "center",
  },
  subtitle: {
    fontSize: "1rem",
    textAlign: "center",
    color: "#666",
    marginBottom: "2rem",
  },
  form: {
    display: "flex",
    flexDirection: "column",
    gap: "1.5rem",
  },
  inputGroup: {
    display: "flex",
    flexDirection: "column",
  },
  label: {
    marginBottom: "0.5rem",
    fontWeight: "600",
  },
  input: {
    padding: "0.5rem",
    borderRadius: "6px",
    border: "1px solid #ccc",
    cursor: "pointer",
  },
  button: {
    padding: "0.8rem",
    background: "#007BFF",
    color: "#fff",
    border: "none",
    borderRadius: "6px",
    cursor: "pointer",
    fontSize: "1rem",
    fontWeight: "600",
    transition: "background 0.2s",
  },
  results: {
    marginTop: "2.5rem",
    background: "#fff",
    borderRadius: "8px",
    padding: "1.5rem",
    boxShadow: "0 2px 8px rgba(0,0,0,0.05)",
  },
  resultTitle: {
    fontSize: "1.3rem",
    marginBottom: "1rem",
    borderBottom: "1px solid #eee",
    paddingBottom: "0.5rem",
  },
  list: {
    listStyle: "none",
    padding: 0,
    margin: 0,
  },
  listItem: {
    padding: "0.6rem 0",
    borderBottom: "1px solid #eee",
  },
  noResults: {
    color: "#999",
    fontStyle: "italic",
  },
};

export default App;
