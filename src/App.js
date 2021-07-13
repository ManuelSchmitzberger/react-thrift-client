import React from 'react';
import logo from './logo.svg';
import './App.css';
import { runHello } from './services/thrift';

function App() {

  var hello = runHello()

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
    </div>
  );
}

export default App;
