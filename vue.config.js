module.exports = {
  assetsDir: 'static',
  outputDir: 'dist',
  mode: 'production',
  devServer: {
    proxy: {
      '^/*': {
        target: 'http://localhost:5000/',
      },
    },
  },
};
