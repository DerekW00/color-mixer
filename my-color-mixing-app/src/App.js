import React, { useState } from 'react';

function App() {
  const [paintName, setPaintName] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await fetch('http://localhost:5000/api/add_paint', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name: paintName }),
    });
    const data = await response.json();
    setMessage(data.message);
  };

  return (
    <div className="App">
      <h1>Acrylic Color Mixing Assistant</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={paintName}
          onChange={(e) => setPaintName(e.target.value)}
          placeholder="Enter paint name"
        />
        <button type="submit">Add Paint</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default App;