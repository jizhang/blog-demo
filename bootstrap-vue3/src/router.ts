import { createRouter, createWebHashHistory } from 'vue-router'
import Demo1 from './views/Demo1.vue'
import Demo2 from './views/Demo2.vue'

export default createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/demo1', component: Demo1 },
    { path: '/demo2', component: Demo2 },
    { path: '/', redirect: '/demo1' },
  ],
})
