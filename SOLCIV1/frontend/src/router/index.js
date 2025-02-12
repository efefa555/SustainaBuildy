import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Simulation from '../views/Simulation.vue';
import Results from '../views/Results.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/simulation',
    name: 'Simulation',
    component: Simulation,
  },
  {
    path: '/results',
    name: 'Results',
    component: Results,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;