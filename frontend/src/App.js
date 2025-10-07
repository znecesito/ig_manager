import React, { useState } from "react";

function App() {
  const [followers, setFollowers] = useState(null);
  const [following, setFollowing] = useState(null);
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!followers || !following) {
      alert("Please upload both files");
      return;
    }

    const formData = new FormData();
    formData.append("followers", followers);
    formData.append("following", following);

    const res = await fetch("http://127.0.0.1:8000/upload", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Upload Followers/Following JSON files</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Followers JSON:</label>
          <input
            type="file"
            accept=".json"
            onChange={(e) => setFollowers(e.target.files[0])}
          />
        </div>
        <div>
          <label>Following JSON:</label>
          <input
            type="file"
            accept=".json"
            onChange={(e) => setFollowing(e.target.files[0])}
          />
        </div>
        <button type="submit">Upload & Analyze</button>
      </form>

      {result && (
        <div style={{ marginTop: "2rem" }}>
          <h2>Results</h2>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
