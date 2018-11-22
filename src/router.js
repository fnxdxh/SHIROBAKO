import OrganizerPage from './components/organizer.vue'

const routers = [
  {
    path: '/organizer',
    name: 'organizer',
    component: OrganizerPage
  },
  {
    path: '/',
    component: OrganizerPage
  },
]
export default routers