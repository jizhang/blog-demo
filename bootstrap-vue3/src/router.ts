import { createRouter, createWebHashHistory } from 'vue-router'
import Demo1 from './views/Demo1.vue'
import Demo2 from './views/Demo2.vue'
import Demo3 from './views/Demo3.vue'
import FormDemo from './views/FormDemo.vue'

export default createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/demo1', component: Demo1 },
    { path: '/demo2', component: Demo2 },
    { path: '/demo3', component: Demo3 },
    { path: '/form-demo', component: FormDemo },
    { path: '/', redirect: '/demo1' },
  ],
})
