import React from 'react'
import ReactDOM from 'react-dom'
import './index.css'
import App from './App'
import registerServiceWorker from './registerServiceWorker'
import { configure } from 'mobx'
import { Provider } from 'mobx-react'
import UserStore from './user'

configure({ enforceActions: true })
const userStore = new UserStore()

ReactDOM.render(
  <Provider userStore={userStore}>
    <App />
  </Provider>
, document.getElementById('root'));
registerServiceWorker();
