import Vue from 'vue'
import Vuex from 'vuex'
import products from './modules/products'
import recipes from './modules/recipes'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    products,
    recipes
  }
})