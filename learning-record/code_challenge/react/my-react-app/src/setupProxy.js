const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target: 'http://127.0.0.1:8088',
      changeOrigin: true,
      pathRewrite: {
        '^/api': ''
      },
      onProxyRes: function (proxyRes, req, res) {
        proxyRes.headers['Access-Control-Allow-Origin'] = '*';
      },
      secure: false,
      logLevel: 'debug'  // Add logging for debugging
    })
  );
};