// src/index.js
import React from 'react'; // Keep this line for React 18
import ReactDOM from 'react-dom/client'; // Keep this line
import './index.css';
import App from './App'; // This import is NEEDED
// Remove reportWebVitals if you are not using it
// import reportWebVitals from './reportWebVitals';

// This is the crucial part to create the root
const root = ReactDOM.createRoot(document.getElementById('root'));

// This is the crucial part to render your App component
root.render(
  <React.StrictMode>
    <App /> {/* This line USES the imported App */}
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();