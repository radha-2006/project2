import { useState } from 'react';

 

function Chatbot() {

  const [input, setInput] = useState('');

  const [chatHistory, setChatHistory] = useState([]);

 

  const handleSend = async () => {

    const response = await fetch('/api/query', {

      method: 'POST',

      headers: { 'Content-Type': 'application/json' },

      body: JSON.stringify({ query: input })

    });

    const data = await response.json();

    setChatHistory([...chatHistory, { query: input, response: data.response }]);

    setInput('');

  };

 

  return (

    <div>

      <div>

        {chatHistory.map((entry, index) => (

          <div key={index}>

            <p><strong>You:</strong> {entry.query}</p>

            <p><strong>Agent:</strong> {entry.response}</p>

          </div>

        ))}

      </div>

      <input

        type="text"

        value={input}

        onChange={(e) => setInput(e.target.value)}

        placeholder="Ask about job trends..."

      />

      <button onClick={handleSend}>Send</button>

    </div>

  );

}

 

export default Chatbot;
