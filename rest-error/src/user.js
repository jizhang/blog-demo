import { observable, flow } from 'mobx'
import request from './request'

export default class UserStore {
  @observable userId = null
  @observable loading = false

  loginUser = flow(function* loginUser(form) {
    this.loading = true
    try {
      this.userId = yield request('/login', null, form)
    } finally {
      this.loading = false
    }
  })
}
