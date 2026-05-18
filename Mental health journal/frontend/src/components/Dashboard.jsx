import { useEffect, useState } from "react";
import axios from "axios";

export default function Dashboard() {
  const [entries, setEntries] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/journals").then((res) => {
      setEntries(res.data);
    });
  }, []);

  return (
    <div>
      <h2>📊 Dashboard</h2>
      {entries.map((e) => (
        <div key={e.id}>
          <p>{e.entry}</p>
          <small>Polarity: {e.polarity.toFixed(2)} | Subjectivity: {e.subjectivity.toFixed(2)}</small>
        </div>
      ))}
    </div>
  );
}
