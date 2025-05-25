import { createRouter, createWebHistory } from 'vue-router';
import ApartmentList from '../pages/ApartmentList.vue';
import ApartmentDetail from '../pages/ApartmentDetail.vue';
import LoginPage from '../pages/LoginPage.vue';

const routes = [
  { path: '/', component: ApartmentList },
  { path: '/apartments/:slug', component: ApartmentDetail },
  { path: '/login', component: LoginPage },
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});
