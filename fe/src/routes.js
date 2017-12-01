/**
 * vue router definitions
 */
const home = resolve => require(['./pages/home/index.vue'], resolve)

export default [
    {
        path: '/',
        component: home,
        meta: {title: '首页'}
    }
]
