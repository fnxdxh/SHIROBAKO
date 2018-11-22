import OrganizerPage from './components/organizer.vue'
import CreateMatch from './components/creatematch.vue'
import Home from './components/home.vue'

const routers = [
  {
    path: '/organizer',
    name: 'organizer',
    component: OrganizerPage
  },
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
      path: '/creatematch',
      name: 'creatematch',
      component: CreateMatch
  }
]
export default routers