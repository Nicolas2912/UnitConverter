// src/UnitDisplay.js
import React from 'react';

// Simple parser to convert units like 'm2', 's2', 'm3' to use <sup> tags
// Handles division symbol '/'
function formatUnit(unitString) {
  if (!unitString) return '';

  // Split by division symbol to handle parts separately
  const parts = unitString.split('/');
  const formattedParts = parts.map(part => {
    // Use regex to find a letter followed by one or more digits at the end
    // e.g., matches '2' in 'm2', '3' in 'cm3'
    // Does NOT match 'h' in 'km/h'
    const match = part.match(/([a-zA-Z]+|\))(\d+)$/); // Match letters or ')' followed by digits at the end

    if (match) {
      const base = part.substring(0, match.index + match[1].length); // Part before the number
      const exponent = match[2]; // The number part
      // Return JSX with <sup> tag
      return (
        <React.Fragment key={part}>
          {base}<sup>{exponent}</sup>
        </React.Fragment>
      );
    }
    // If no exponent found, return the part as is
    return part;
  });

  // Join the parts back with the division symbol if needed
  return formattedParts.map((part, index) => (
    <React.Fragment key={index}>
      {part}
      {index < formattedParts.length - 1 ? '/' : ''}
    </React.Fragment>
  ));
}


const UnitDisplay = ({ unit }) => {
  return <>{formatUnit(unit)}</>;
};

export default UnitDisplay;