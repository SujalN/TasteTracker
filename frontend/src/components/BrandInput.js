import React, { useState } from 'react';

export default function BrandInput({ onCompare }) {
  const [input, setInput] = useState('');
  const [list, setList] = useState([]);

  const addBrand = () => {
    const name = input.trim();
    if (name && !list.includes(name)) {
      setList([...list, name]);
      setInput('');
    }
  };

  const removeBrand = (name) =>
    setList(list.filter((b) => b !== name));

  const submit = () => {
    if (list.length >= 2) onCompare(list);
  };

  return (
    <div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Enter brand name"
      />
      <button onClick={addBrand}>Add</button>
      <div style={{ margin: '8px 0' }}>
        {list.map((b) => (
          <span key={b} style={{ marginRight: 8 }}>
            {b}{' '}
            <button onClick={() => removeBrand(b)}>×</button>
          </span>
        ))}
      </div>
      <button onClick={submit} disabled={list.length < 2}>
        Compare {list.length} brands
      </button>
    </div>
  );
}
