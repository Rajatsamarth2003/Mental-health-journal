import { useState } from "react";
import axios from "axios";

export default function JournalEditor() {
  const [entry, setEntry] = useState("");
  const [sentiment, setSentiment] = useState(null);

  const saveEntry = async () => {
    const res = await axios.post("http://localhost:5000/journal", { entry });
    setSentiment(res.data.sentiment);
    setEntry("");
  };

  return (
    <div>
      <h2>📔 Journal</h2>
      <textarea value={entry} onChange={(e) => setEntry(e.target.value)} />
      <button onClick={saveEntry}>Save</button>
      {sentiment && (
        <p>Polarity: {sentiment.polarity.toFixed(2)} | Subjectivity: {sentiment.subjectivity.toFixed(2)}</p>
      )}
    </div>
  );
}
