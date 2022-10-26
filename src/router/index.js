import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import EmployeesManager from "@/views/EmployeesManager";
import AddEmployee from "@/views/AddEmployee";
import EditEmployee from "@/views/EditEmployee";
import ViewEmployee from "@/views/ViewEmployee";
import PageNotFound from "@/views/PageNotFound";

const routes = [
  {
    path: '/',
    name: 'home',
    redirect: "/employees",
    component: HomeView
  },
  {
    path: '/employees',
    name: 'EmployeesManager',
    component: EmployeesManager
  },
  {
    path: '/employees/add',
    name: 'AddEmployee',
    component: AddEmployee
  },
  {
    path: '/employees/edit/:employeeId',
    name: 'EditEmployee',
    component: EditEmployee
  },
  {
    path: '/employees/view/:employeeId',
    name: 'ViewEmployee',
    component: ViewEmployee
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'PageNotFound',
    component: PageNotFound
  }
  
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
