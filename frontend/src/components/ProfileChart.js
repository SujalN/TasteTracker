import React from 'react';
import { Radar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
} from 'chart.js';

ChartJS.register(
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
);

export default function ProfileChart({ profiles }) {
  const domains = Object.keys(profiles[Object.keys(profiles)[0]]);
  const datasets = Object.entries(profiles).map(([brand, data], i) => ({
    label: brand,
    data: domains.map((d) => data[d].length), // simplistic score = count
    fill: true,
    backgroundColor: `rgba(${50 * i}, ${100 + 30 * i}, ${150 - 20 * i}, 0.2)`,
    borderColor: `rgba(${50 * i}, ${100 + 30 * i}, ${150 - 20 * i}, 1)`,
    pointBackgroundColor: `rgba(${50 * i}, ${100 + 30 * i}, ${150 - 20 * i}, 1)`
  }));

  const chartData = {
    labels: domains,
    datasets
  };

  return (
    <div style={{ maxWidth: 600, margin: '20px auto' }}>
      <Radar data={chartData} />
    </div>
  );
}
