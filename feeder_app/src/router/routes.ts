import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),

    children: [

      { path: '', component: () => import('pages/LandingPage.vue'), meta: { layout: 'LandingLayout' } },

      { path: 'feeder', name: 'feeder', component: () => import('pages/FeederPage.vue') },

      { path : 'landing', name: 'landing', component: () => import('pages/LandingPage.vue') },
    ],
  },


  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
