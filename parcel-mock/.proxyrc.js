const { createProxyMiddleware } = require('http-proxy-middleware')
const { createMockMiddleware } = require('./mock-middleware')
const bodyParser = require('body-parser')

module.exports = function (app) {
  if (process.env.MOCK === 'none') {
    const proxy = createProxyMiddleware('/api', {
      target: 'http://localhost:8000/',
    })
    app.use(proxy)
  } else {
    app.use(bodyParser.json())
    app.use(createMockMiddleware('./mock'))
  }
}
