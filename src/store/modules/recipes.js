import recipesService from '../../services/recipesService'

const state = {
  recipes: [],
  recipe: [],
  categories:[],
  errors: ''
}

const getters = {
  recipes: state => {
    return state.recipes
  }
}

const actions = {
  getRecipes ({ commit }) {
    recipesService.fetchRecipes()
    .then(products => {
      commit('setRecipes', products)
    })
  },
  getCategories ({ commit }) {
    recipesService.categories()
    .then(categories => {
      commit('setCategories', categories)
    })
  },
  getErrors () {
    return state.errors
  },
  getRecipe ({ commit }, id) {
    recipesService.showRecipe(id)
    .then(id => {
      commit('getRecipe', id)
    })
  },
  addRecipe({ commit }, Recipe) {
    recipesService.postRecipe(Recipe)
    .catch(err => state.errors = err.response.status)
    .then(() => {
      commit('addRecipe', Recipe)
    })
  },
  updateRecipe({ commit }, payload) {
    recipesService.updateRecipe(payload)
    .catch(err => state.errors = err.response.data)
    .then(() => {
      commit('addRecipe', payload)
    })
  },
  deleteRecipe( { commit }, id) {
    recipesService.deleteRecipe(id)
    .catch(err => state.errors = err.response.data)
    commit('deleteRecipe', id)
  }
}

const mutations = {
  setRecipes (state, recipes) {
    state.recipes = recipes
  },
  setCategories (state, categories) {
    state.categories = categories
  },
  getRecipe(state, id) {
    state.recipe = id
  },
  addRecipe(state, recipe) {
    state.recipes.push(recipe)
  },
  updateRecipe(state, id, payload) {
    state.recipes = state.recipes.filter(obj => obj.pk !== id)
    state.recipes.push(payload)
  },
  deleteRecipe(state, id) {
    state.recipes = state.recipes.filter(obj => obj.pk !== id)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}