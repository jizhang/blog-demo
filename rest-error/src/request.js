import qs from 'qs'
import _ from 'lodash'

export default function request(url, args, form) {
  let config = {
    method: 'GET',
    body: null,
    credentials: 'same-origin',
    headers: {},
  }

  if (!_.isEmpty(args)) {
    url = '?' + qs.stringify(args)
  }

  if (!_.isEmpty(form)) {
    config.method = 'POST'
    config.body = JSON.stringify(form)
    config.headers['Content-Type'] = 'application/json'
  }

  function RequestError(status, message) {
    this.status = status
    this.message = message
  }

  function showError(message) {
    alert(`Error: ${message}`)
  }

  return fetch(url, config)
    .then(response => {
      if (response.ok) {
        return response.json()
      }

      if (response.status === 400) {
        return response.json()
          .then(responseJson => {
            if (responseJson.status === 400) {
              // global error
              showError(responseJson.message)
            }
            throw responseJson
          }, error => {
            throw new RequestError(400)
          })
      }

      switch (response.status) {
        case 401:
          break; // redirect to login
        case 403:
          break; // redirect to forbidden
        case 404:
          break; // redirect to not found
        case 500:
          break; // redirect internal server error
        default:
          showError('HTTP Status Code ' + response.status)
      }

      throw new RequestError(response.status)
    }, error => {
      showError(error.message)
      throw new RequestError(0, error.message)
    })
}
