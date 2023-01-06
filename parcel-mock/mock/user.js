const sendJson = require('send-data/json')

function getCurrentUser(req, res) {
  sendJson(req, res, {
    payload: {
      id: 1,
      nickname: 'Jerry',
    },
  })
}

function login(req, res) {
  const { username, password } = req.body
  if (username === 'admin' && password === '888888') {
    sendJson(req, res, {
      payload: {
        id: 1,
        nickname: 'Jerry',
      },
    })
  } else {
    res.statusCode = 400
    sendJson(req, res, {
      code: 400,
      payload: {
        message: 'Invalid username or password.',
      },
    })
  }
}

module.exports = {
  'GET /api/current-user': getCurrentUser,
  'POST /api/login': login,
}
