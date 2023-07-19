import React, { Component } from 'react'
import _ from 'lodash'
import { inject, observer } from 'mobx-react'
import logo from './logo.svg'
import './App.css'
import request from './request'

@inject('userStore')
@observer
class App extends Component {
  state = {
    message: '',
    username: '',
    password: '',
    error: '',
  }

  ping = () => {
    request('/ping')
      .then(payload => {
        this.setState({
          message: payload,
        })
      })
  }

  handleChangeUsername = (event) => {
    this.setState({
      username: event.target.value,
    })
  }

  handleChangePassword = (event) => {
    this.setState({
      password: event.target.value,
    })
  }

  loginUser = () => {
    const form = _.pick(this.state, ['username', 'password'])
    this.props.userStore.loginUser(form)
      .catch(error => {
        if (error.status === 40001) {
          this.setState({
            error: error.message,
          })
        }
      })
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <button onClick={this.ping}>Ping</button>
        <div>{this.state.message}</div>
        <div>
          Username:
          <input
            type="text"
            onChange={this.handleChangeUsername}
            value={this.state.username}
          />
        </div>
        <div>
          Password:
          <input
            type="password"
            onChange={this.handleChangePassword}
            value={this.state.password}
          />
        </div>
        <button onClick={this.loginUser}>Login</button>
        {this.props.userStore.userId ? (
          <div>User ID: {this.props.userStore.userId}</div>
        ) : null}
        {this.state.error ? (
          <div>Error: {this.state.error}</div>
        ) : null}
      </div>
    );
  }
}

export default App
