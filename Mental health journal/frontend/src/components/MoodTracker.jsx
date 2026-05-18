import { useState } from "react";

export default function MoodTracker() {
  const [mood, setMood] = useState(5);

  return (
    <div>
      <h2>😊 Mood Tracker</h2>
      <input
        type="range"
        min="1"
        max="10"
        value={mood}
        onChange={(e) => setMood(e.target.value)}
      />
      <p>Current Mood: {mood}/10</p>
    </div>
  );
}
