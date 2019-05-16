<template>
<section class="notification is-medium is-light is-bold">
  <div class="hero-body">
      <div class="container">
        <div class="columns">
          <div class="column" v-for=" recipe in filterRecipes">
            <div class="card">
              <div class="card-image">
                <figure class="image is-4by3">
                  <img :src="recipe.image_one" alt="Placeholder image">
                </figure>
              </div>
              <div class="card-content">
                <div class="media">
                  <div class="media-left">
                    <figure class="image is-48x48">
                      <img :src="recipe.image_one" alt="Placeholder image">
                    </figure>
                  </div>
                  <div class="media-content">
                    <p class="title is-4">{{recipe.name}}</p>
                    <p class="subtitle is-6">@{{recipe.created_by.username}}</p>
                  </div>
                </div>

                <div class="content">
                  {{recipe.ingredient.slice(0,200)}}...
                  <br>
                  <br>
                  <div class="level">
                    <div class="level-left">
                        <button><i class="fas fa-shopping-cart"></i> Ajouter au panier</button>
                    </div>
                    <div class="level-right">
                        <p><i class="fas fa-hourglass-start"></i>&nbsp;{{recipe.duration}} min</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      <br>
      <h1 class="title">
        Résumé de la semaine
      </h1>
      <div>
        <hr>
        <b-message type="is-info" has-icon>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce id fermentum quam. Proin sagittis, nibh id hendrerit imperdiet, elit sapien laoreet elit
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce id fermentum quam. Proin sagittis, nibh id hendrerit imperdiet, elit sapien laoreet elit
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce id fermentum quam. Proin sagittis, nibh id hendrerit imperdiet, elit sapien laoreet elit
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce id fermentum quam. Proin sagittis, nibh id hendrerit imperdiet, elit sapien laoreet elit
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce id fermentum quam. Proin sagittis, nibh id hendrerit imperdiet, elit sapien laoreet elit
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce id fermentum quam. Proin sagittis, nibh id hendrerit imperdiet, elit sapien laoreet elit
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce id fermentum quam. Proin sagittis, nibh id hendrerit imperdiet, elit sapien laoreet elit
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce id fermentum quam. Proin sagittis, nibh id hendrerit imperdiet, elit sapien laoreet elit
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce id fermentum quam. Proin sagittis, nibh id hendrerit imperdiet, elit sapien laoreet elit
        </b-message>
      </div>
    </div>
  </div>
</section>
</template>

<script>
export default {
  data(){
    return {
      calc:{
        n1:null,
        n2:null,
        total:null
      }
    }
  },
  computed:{
        filterRecipes(){
            if (!this.recipes){
                this.isEmpty = true
            }
            return this.recipes.filter((recipe)=>{
                return recipe.name.match(this.search)
            })
        }, 
        recipes(){
            return this.$store.state.recipes.recipes
        },
        recipeOne(){
            return this.$store.state.recipes.recipe
        }
    },
  methods:{
    calcul(){
      this.calc.total = parseInt(this.calc.n1) + parseInt(this.calc.n2)
    }
  }
 
}
</script>