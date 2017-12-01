import Vue from 'vue'
import VueRouter from 'vue-router'
import routes from './routes'

Vue.use(VueRouter)

// dev tools
if (process.env.NODE_ENV === 'development') {
    Vue.config.devtools = true
}

// create router
const router = new VueRouter({routes})

// start
new Vue({router}).$mount('#app')
