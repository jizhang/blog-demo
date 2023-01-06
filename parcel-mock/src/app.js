fetch('/api/current-user')
  .then(response => response.json())
  .then(responseJson => {
    document.querySelector('#nickname').textContent = responseJson.payload.nickname
  })
