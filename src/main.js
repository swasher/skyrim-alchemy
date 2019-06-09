import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'

Vue.config.productionTip = false;
Vue.config.devtools = true;


// This is the event hub we'll use in every
// component to communicate between them.
// var eventHub = new Vue();


new Vue({
  render: h => h(App),
}).$mount('#app');
