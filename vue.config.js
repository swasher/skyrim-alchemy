module.exports = {
  assetsDir: 'static',
  outputDir: 'dist',
  devServer: {
    proxy: {
      '^/*': {
        target: 'http://localhost:5000/',
      },
    },
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
      'Access-Control-Allow-Headers': 'X-Requested-With, content-type, Authorization'
    },
  },
};
