import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Products from '@/components/Products'
import Recipes from '@/components/Recipes'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Index
    },
    {
      path: '/products',
      name: 'products',
      component: Products
    },
    {
      path: '/recipes',
      name: 'recipes',
      component: Recipes
    }
  ]
})
