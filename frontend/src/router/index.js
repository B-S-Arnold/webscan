import { createRouter, createWebHistory } from 'vue-router';

// Import your components for different views
import Home from '../views/Home.vue';
import Scan from '../views/Scan.vue';
import Results from '../views/Results.vue';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/scan',
        name: 'Scan',
        component: Scan,
    },
    {
        path: '/results',
        name: 'Results',
        component: Results,
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
