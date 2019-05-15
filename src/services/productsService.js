import api from '@/services/api'

export default {
  fetchProducts() {
    return api.get(`products/`)
              .then(response => response.data)
  },
  showProduct(id) {
    return api.get(`products/show/${id}`)
              .then(response => response.data)
  },
  postProduct(payload) {
    return api.post(`products/create`, payload)
              .then(response => response.data)

  },
  updateProduct(payload) {
    return api.put(`products/update-or-delete/${payload.id}`, payload)
              .then(response => response.data)
              .catch(function (error) {
               
              })
  },
  deleteProduct(id) {
    return api.delete(`products/update-or-delete/${id}`)
              .then(response => { 
                
              })  
  }
}