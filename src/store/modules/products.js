import productsService from '../../services/productsService'

const state = {
  products: [],
  product: [],
  errors: ''
}

const getters = {
  products: state => {
    return state.products
  }
}

const actions = {
  getProducts ({ commit }) {
    productsService.fetchProducts()
    .then(products => {
      commit('setProducts', products)
    })
  },
  getErrors () {
    return state.errors
  },
  getProduct ({ commit }, id) {
    productsService.showProduct(id)
    .then(id => {
      commit('getProduct', id)
    })
  },
  addProduct({ commit }, Equipment) {
    productsService.postProduct(Equipment)
    .catch(err => state.errors = err.response.status)
    .then(() => {
      commit('addProduct', Equipment)
    })
  },
  updateProduct({ commit }, payload) {
    productsService.updateProduct(payload)
    .catch(err => state.errors = err.response.data)
    .then(() => {
      commit('addProduct', payload)
    })
  },
  deleteProduct( { commit }, id) {
    productsService.deleteProduct(id)
    .catch(err => state.errors = err.response.data)
    commit('deleteProduct', id)
  }
}

const mutations = {
  setProducts (state, products) {
    state.products = products
  },
  getProduct(state, id) {
    state.equipment = id
  },
  addProduct(state, equipment) {
    state.products.push(equipment)
  },
  updateProduct(state, id, payload) {
    state.products = state.products.filter(obj => obj.pk !== id)
    state.products.push(payload)
  },
  deleteProduct(state, id) {
    state.products = state.products.filter(obj => obj.pk !== id)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}