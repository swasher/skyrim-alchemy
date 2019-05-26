module.exports = {
  assetsDir: 'static',
  outputDir: 'dist',
  devServer: {
    proxy: {
      '^/*': {
        target: 'http://localhost:5000/',
        ws: false,
        changeOrigin: true
      },
    },
  },
};
