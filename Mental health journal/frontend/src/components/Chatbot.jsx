import { useState } from 'react';
import axios from 'axios';

export default function Chatbot() {
  const [msg, setMsg] = useState("");
  const [chat, setChat] = useState([]);

  const sendMsg = async () => {
    const res = await axios.post('http://localhost:5000/chat', { message: msg });
    setChat([...chat, { user: msg, bot: res.data.reply }]);
    setMsg("");
  };

  return (
    <div>
      <h2>🤖 Chatbot</h2>
      {chat.map((c, i) => (
        <div key={i}>
          <p><b>You:</b> {c.user}</p>
          <p><b>Bot:</b> {c.bot}</p>
        </div>
      ))}
      <input value={msg} onChange={e => setMsg(e.target.value)} />
      <button onClick={sendMsg}>Send</button>
    </div>
  );
}
