const Vue = require("vue");

Vue.component('hello-world', require('./components/HelloWorld.vue').default)

const app = new Vue({
    el: '#app'
})