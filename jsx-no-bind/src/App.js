import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Parent from './components/Parent'
import NoArgument from './components/NoArgument'
import Lists from './components/Lists'


class App extends Component {
  render() {
    console.log(this.state)
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>

        <div style={{ textAlign: 'left', padding: '15px 30px' }}>
          <Parent />
          <NoArgument />
          <Lists />
        </div>
      </div>
    );
  }
}

export default App;
