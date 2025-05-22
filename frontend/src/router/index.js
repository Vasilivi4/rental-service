import { createRouter, createWebHistory } from 'vue-router'
import ApartmentList from '@/views/ApartmentList.vue'
import ApartmentDetail from '@/views/ApartmentDetail.vue'

const routes = [
  { path: '/', component: ApartmentList },
  { path: '/apartment/:id', component: ApartmentDetail },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
