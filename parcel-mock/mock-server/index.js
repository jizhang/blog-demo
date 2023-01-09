const express = require('express')

const app = express()
app.use(express.json())

app.post('/api/login', (req, res) => {
  let { username, password } = req.body
  res.json({
    id: 1,
    nickname: 'Jerry',
  })
})

const server = app.listen(8080, () => {
  console.log('Mock server listening on port ' + server.address().port)
})
