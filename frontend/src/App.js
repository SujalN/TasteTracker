import React, { useState } from 'react';
import BrandInput from './components/BrandInput';
import ProfileChart from './components/ProfileChart';
import InsightPanel from './components/InsightPanel';
import { compareBrands } from './services/api';

function App() {
  const [brands, setBrands] = useState([]);
  const [profiles, setProfiles] = useState(null);
  const [insight, setInsight] = useState('');

  const handleCompare = async (selectedBrands) => {
    setBrands(selectedBrands);
    setProfiles(null);
    setInsight('Loading…');
    try {
      const resp = await compareBrands(selectedBrands);
      setProfiles(resp.data.profiles);
      setInsight(resp.data.insight);
    } catch (err) {
      console.error(err);
      setInsight('Error fetching data.');
    }
  };

  return (
    <div style={{ padding: 20, fontFamily: 'sans-serif' }}>
      <h1>TasteTracker</h1>
      <BrandInput onCompare={handleCompare} />
      {profiles && (
        <ProfileChart profiles={profiles} />
      )}
      {insight && (
        <InsightPanel insight={insight} />
      )}
    </div>
  );
}

export default App;
