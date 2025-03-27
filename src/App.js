// src/App.js
import React, { useState, useEffect } from 'react';
import UnitDisplay from './UnitDisplay'; // <-- Import the new component


const API_URL = 'http://localhost:5001';

function App() {
  const [conversionTypes, setConversionTypes] = useState([]);
  const [units, setUnits] = useState({});
  const [selectedType, setSelectedType] = useState('');
  const [fromUnit, setFromUnit] = useState('');
  const [toUnit, setToUnit] = useState('');
  const [inputValue, setInputValue] = useState(1.0);
  const [result, setResult] = useState(null);
  const [explanation, setExplanation] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const [isFetchingUnits, setIsFetchingUnits] = useState(true);
  const [showResult, setShowResult] = useState(false); // State for result animation

  // Fetch available units and types
  useEffect(() => {
    const fetchUnits = async () => {
      setIsFetchingUnits(true);
      setError('');
      try {
        const response = await fetch(`${API_URL}/units`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setUnits(data);
        const types = Object.keys(data);
        setConversionTypes(types);
        if (types.length > 0) {
           handleTypeChange(types[0], data);
        } else {
           setIsFetchingUnits(false);
        }
      } catch (e) {
        console.error("Error fetching units:", e);
        setError('Failed to load units from the server. Is the backend running?');
        setIsFetchingUnits(false);
      }
    };
    fetchUnits();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Handle type change
  const handleTypeChange = (type, unitsData = units) => {
    const availableUnits = unitsData[type] || [];
    setSelectedType(type);
    setResult(null);
    setExplanation('');
    setError('');
    setShowResult(false); // Hide result on type change
    setFromUnit(availableUnits[0] || '');
    setToUnit(availableUnits.length > 1 ? availableUnits[1] : (availableUnits[0] || ''));
    setInputValue(1.0);
    setIsFetchingUnits(false);
  };

  // Conversion Function
  const handleConvert = async () => {
    if (!selectedType || !fromUnit || !toUnit || inputValue === '') {
      setError('Please select conversion type, units, and enter a value.');
      setShowResult(false); // Hide any previous result
      return;
    }
    setIsLoading(true);
    setError('');
    setResult(null);
    setExplanation('');
    setShowResult(false); // Hide result initially

    try {
      const response = await fetch(`${API_URL}/convert`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          type: selectedType,
          value: parseFloat(inputValue),
          fromUnit: fromUnit,
          toUnit: toUnit,
        }),
      });
      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.error || `HTTP error! status: ${response.status}`);
      }
      setResult(data.result);
      setExplanation(data.explanation || '');
      setShowResult(true); // Show result after successful conversion

    } catch (e) {
      console.error("Conversion error:", e);
      setError(e.message || 'An error occurred during conversion.');
      setResult(null);
      setExplanation('');
      setShowResult(false); // Ensure result area is hidden on error
    } finally {
      setIsLoading(false);
    }
  };

  const currentUnits = units[selectedType] || [];

  return (
    // Centering container, increased padding
    <div className="min-h-screen flex items-center justify-center p-6 bg-base-200">
      {/* Wider card, increased padding */}
      <div className="card w-full max-w-4xl bg-base-100 shadow-xl">
        <div className="card-body p-8 md:p-10"> {/* Increased padding */}
          {/* Larger title, more margin */}
          <h1 className="card-title text-4xl justify-center mb-8">Universal Unit Converter</h1>

          {/* Initial Loading State */}
          {isFetchingUnits && (
            <div className="text-center p-6">
               <span className="loading loading-lg loading-spinner text-primary"></span>
               <p className="mt-4 text-lg">Loading available units...</p>
            </div>
          )}

          {/* Error during initial load */}
          {!isFetchingUnits && error && conversionTypes.length === 0 && (
            <div role="alert" className="alert alert-error">
               <svg xmlns="http://www.w3.org/2000/svg" className="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 14l2-2m0 0l2-2m-2 2l-2 2m2-2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
               <span>{error}</span>
            </div>
          )}

          {/* Main Converter UI */}
          {!isFetchingUnits && conversionTypes.length > 0 && (
            <>
              {/* Type Selection - Increased bottom margin */}
              <div className="form-control w-full mb-8">
                <label className="label" htmlFor="conversionType">
                  <span className="label-text text-md mb-1">Conversion Type:</span> {/* Spacing below label */}
                </label>
                <select
                  id="conversionType"
                  value={selectedType}
                  onChange={(e) => handleTypeChange(e.target.value)}
                  // Added select-md for slightly larger size and focus styles
                  className="select select-bordered select-md w-full focus:ring-2 focus:ring-primary focus:border-primary transition-colors duration-200"
                  disabled={isLoading}
                >
                  {conversionTypes.map((type) => (
                    <option key={type} value={type}>{type}</option>
                  ))}
                </select>
              </div>

              {/* Input / Output Grid - Increased gap */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-6">

                {/* Input Column - Increased padding and gap */}
                <div className="flex flex-col gap-6 p-6 border border-base-300 rounded-xl">
                   <h2 className="text-2xl font-semibold text-center mb-2">Input</h2>
                   {/* Input Value */}
                   <div className="form-control w-full">
                      <label className="label" htmlFor="inputValue">
                         <span className="label-text text-md mb-1">Value:</span>
                      </label>
                      <input
                         type="number"
                         id="inputValue"
                         value={inputValue}
                         onChange={(e) => setInputValue(e.target.value)}
                         step="any"
                         // Added input-md for slightly larger size and focus styles
                         className="input input-bordered input-md w-full focus:ring-2 focus:ring-primary focus:border-primary transition-colors duration-200"
                         disabled={isLoading}
                      />
                   </div>
                   {/* From Unit */}
                   <div className="form-control w-full">
                     <label className="label" htmlFor="fromUnit">
                       <span className="label-text text-md mb-1">From Unit:</span>
                     </label>
                     <select
                       id="fromUnit"
                       value={fromUnit}
                       onChange={(e) => setFromUnit(e.target.value)}
                       // Added select-md for slightly larger size and focus styles
                       className="select select-bordered select-md w-full focus:ring-2 focus:ring-primary focus:border-primary transition-colors duration-200"
                       disabled={isLoading || currentUnits.length === 0}
                     >
                       {currentUnits.map((unit) => (
                         <option key={`from-${unit}`} value={unit}>
                           <UnitDisplay unit={unit} />
                         </option>
                       ))}
                     </select>
                   </div>
                </div>

                {/* Output Column - Increased padding and gap */}
                <div className="flex flex-col gap-6 p-6 border border-base-300 rounded-xl">
                  <h2 className="text-2xl font-semibold text-center mb-2">Output</h2>
                  {/* To Unit */}
                  <div className="form-control w-full">
                     <label className="label" htmlFor="toUnit">
                       <span className="label-text text-md mb-1">To Unit:</span>
                     </label>
                     <select
                       id="toUnit"
                       value={toUnit}
                       onChange={(e) => setToUnit(e.target.value)}
                       // Added select-md for slightly larger size and focus styles
                       className="select select-bordered select-md w-full focus:ring-2 focus:ring-primary focus:border-primary transition-colors duration-200"
                       disabled={isLoading || currentUnits.length === 0}
                     >
                       {currentUnits.map((unit) => (
                         <option key={`to-${unit}`} value={unit}>
                           <UnitDisplay unit={unit} />
                         </option>
                       ))}
                     </select>
                   </div>
                   {/* Result Display Area */}
                   <div className="mt-2 min-h-[100px] flex flex-col justify-center items-center"> {/* Increased min-height */}
                     {/* Loading during conversion */}
                     {isLoading && !isFetchingUnits && (
                         <span className="loading loading-dots loading-lg text-info"></span>
                     )}
                     {/* Error during conversion */}
                     {!isLoading && error && conversionTypes.length > 0 && (
                       <div role="alert" className="alert alert-error text-sm p-3 w-full">
                          <svg xmlns="http://www.w3.org/2000/svg" className="stroke-current shrink-0 h-5 w-5" fill="none" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 14l2-2m0 0l2-2m-2 2l-2 2m2-2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                          <span>{error}</span>
                       </div>
                     )}
                     {/* Successful Conversion Result with Fade-in Animation */}
                     <div
                        className={`w-full transition-opacity duration-500 ease-in-out ${showResult ? 'opacity-100' : 'opacity-0'}`}
                     >
                        {result !== null && (
                            <div role="alert" className="alert alert-success shadow-md">
                                <div>
                                    <h3 className="font-bold text-xl"> {/* Larger result text */}
                                        {Number(result).toLocaleString(undefined, { maximumFractionDigits: 6 })}{' '}
                                        <UnitDisplay unit={toUnit} />
                                    </h3>
                                    {explanation && <div className="text-sm mt-1">{explanation}</div>} {/* Smaller explanation */}
                                </div>
                            </div>
                        )}
                     </div>
                   </div>
                 </div>
              </div>

              {/* Convert Button */}
              <div className="card-actions justify-center mt-8"> {/* Increased margin-top */}
                <button
                  onClick={handleConvert}
                  disabled={isLoading || !selectedType || !fromUnit || !toUnit}
                  // Added btn-md for slightly larger button and focus styles
                  className="btn btn-primary btn-md px-8 gap-2 focus:ring-2 focus:ring-offset-2 focus:ring-primary transition-all duration-200"
                >
                  {isLoading && <span className="loading loading-spinner loading-xs"></span>}
                  Convert
                </button>
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;