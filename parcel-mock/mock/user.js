const sendJson = require('send-data/json')

function getCurrentUser(req, res) {
  sendJson(req, res, {
    id: 1,
    nickname: 'Jerry',
  })
}

function login(req, res) {
  const { username, password } = req.body
  if (username === 'admin' && password === '888888') {
    sendJson(req, res, {
      id: 1,
      nickname: 'Jerry',
    })
  } else {
    sendJson(req, res, {
      statusCode: 400,
      body: {
        code: 40001,
        message: 'Invalid username or password',
      },
    })
  }
}

module.exports = {
  'GET /api/current-user': getCurrentUser,
  'POST /api/login': login,
}
