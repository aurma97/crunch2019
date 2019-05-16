import api from '@/services/api'

export default {
  fetchRecipes() {
    return api.get(`recipes/`)
              .then(response => response.data)
  },
  categories() {
    return api.get(`recipes/categories`)
              .then(response => response.data)
  },
  showRecipe(id) {
    return api.get(`recipes/show/${id}`)
              .then(response => response.data)
  },
  postRecipe(payload) {
    return api.post(`recipes/create`, payload)
              .then(response => response.data)

  },
  updateRecipe(payload) {
    return api.put(`recipes/update-or-delete/${payload.id}`, payload)
              .then(response => response.data)
              .catch(function (error) {
               
              })
  },
  deleteRecipe(id) {
    return api.delete(`recipes/update-or-delete/${id}`)
              .then(response => { 
                
              })  
  }
}