window.addEventListener('load', () => {
  fetch('/api/current-user')
    .then((response) => response.json())
    .then((payload) => {
      document.getElementById('nickname').textContent = payload.nickname
    })
})

const form = document.getElementById('login')
form.addEventListener('submit', (event) => {
  event.preventDefault()

  const { username, password } = form.elements
  const json = {
    username: username.value,
    password: password.value,
  }

  post('/api/login', json).then(
    (payload) => alert(`Welcome, ${payload.nickname}!`),
    (error) => alert(error)
  )
})

async function post(url, json) {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(json),
  })

  if (response.ok) return response.json()

  const payload = await response.json()
  throw new Error(payload.message)
}
