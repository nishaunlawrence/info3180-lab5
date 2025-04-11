import { createRouter, createWebHistory } from 'vue-router';
import AddMovieFormView from '../views/AddMovieFormView.vue';
import MoviesView from '../views/MoviesView.vue';

const routes = [
  {
    path: '/movies/create',
    name: 'AddMovie',
    component: AddMovieFormView,
  },
  {
    path: '/movies',
    name: 'Movies',
    component: MoviesView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
