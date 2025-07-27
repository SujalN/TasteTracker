import React from 'react';

export default function InsightPanel({ insight }) {
  return (
    <div style={{
      border: '1px solid #ddd',
      borderRadius: 4,
      padding: 16,
      maxWidth: 800,
      margin: '20px auto',
      background: '#fafafa'
    }}>
      <h2>Strategic Insight</h2>
      <p style={{ whiteSpace: 'pre-wrap' }}>{insight}</p>
    </div>
  );
}
