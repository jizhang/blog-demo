import { createRouter, createWebHashHistory } from 'vue-router'
import Demo1 from './views/Demo1.vue'

export default createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/demo1', component: Demo1 },
    { path: '/', redirect: '/demo1' },
  ],
})
