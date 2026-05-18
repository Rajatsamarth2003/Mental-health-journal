import Chatbot from "./components/Chatbot";
import JournalEditor from "./components/JournalEditor";
import MoodTracker from "./components/MoodTracker";
import Dashboard from "./components/Dashboard";

function App() {
  return (
    <div>
      <h1>🧠 AI Mental Health Journal & Chatbot</h1>
      <JournalEditor />
      <MoodTracker />
      <Chatbot />
      <Dashboard />
    </div>
  );
}
export default App;
