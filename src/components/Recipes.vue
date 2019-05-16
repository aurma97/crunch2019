<template>
    <div class="container">
        <br>
                <!-- Breadcrumb -->
                <nav class="breadcrumb has-succeeds-separator" aria-label="breadcrumbs">     
                    <div v-if="!isComponentModalActive">
                        <ul v-if="showRecipe">
                            <li><router-link to="/">Accueil</router-link></li>
                            <li @click="showRecipe = false"><a>Gestion des recettes</a></li>
                            <li class="is-active"><a href="#" aria-current="page">Modification de {{recipe.name}}</a></li>
                        </ul>
                        <ul v-if="!showRecipe">
                            <li><router-link to="/">Accueil</router-link></li>
                            <li class="is-active"><a href="#">Gestion des recettes</a></li>
                        </ul>
                    </div>
                    <ul v-if="isComponentModalActive">
                        <li><router-link to="/">Accueil</router-link></li>
                        <li><a href="#">Gestion des recettes</a></li>
                        <li class="is-active"><a href="#">Ajout d'une recette</a></li>
                    </ul>
                </nav>

                <!-- Ajout d'un équipement -->

                <template v-if="isComponentModalActive">
                    <section>
                        <hr>
                        <div class="modal-card" style="width: auto">
                            <div>
                                <div class="columns">
                                    <div class="column">
                                        <section class="modal-card-body">
                                            <b-field label="Nom de la recette">
                                                <b-input
                                                    type="text"
                                                    v-model="recipe.name"
                                                    required>
                                                </b-input>
                                            </b-field>
                                            <b-field label="Prix">
                                                <b-input
                                                    type="text"
                                                    v-model="recipe.price"
                                                    placeholder="Prix de la recette"
                                                    required>
                                                </b-input>
                                            </b-field>
                                            <b-field label="Ingredient">
                                                <b-input
                                                    type="textarea"
                                                    v-model="recipe.ingredient"
                                                    placeholder="Décrivez la préparation"
                                                    required>
                                                </b-input>
                                            </b-field>
                                            <b-field label="Durée de préparation">
                                                <b-input
                                                    type="text"
                                                    v-model="recipe.duration"
                                                    required>
                                                </b-input>
                                            </b-field>
                                            <b-field label="Categorie" type="is-fullwidth">
                                                <b-select placeholder="Select a character" v-model="recipe.category">
                                                    <option v-for="category in categories" :value="category.id">{{category.name}}</option>
                                                </b-select>
                                            </b-field>
                                        </section>
                                    </div>
                                    <div class="column">
                                        <b-field class="file">
                                            <b-upload v-model="recipe.image_one">
                                                <a class="button is-primary">
                                                    <b-icon icon="upload"></b-icon>
                                                    <span>Uploader votre image</span>
                                                </a>
                                            </b-upload>
                                            <span class="file-name" v-if="recipe.image_one">
                                                {{ recipe.image_one.name }}
                                            </span>
                                        </b-field>
                                    </div>
                                </div>
                                <footer class="modal-card-foot">
                                    <button class="button is-primary" @click="addRecipe">Valider</button>
                                    <b-button @click="isComponentModalActive = false">Annuler</b-button>
                                </footer>
                            </div>
                            <br>
                        </div>
                            
                    </section>
                </template>

                <!-- Modification d'un équipement -->



                <!-- Chargement lors de la sauvegarde -->

                <b-loading :is-full-page="isFullPage" :active.sync="isLoading" :can-cancel="true"></b-loading>
                
                <!-- Affichage du tableau des recettes -->
                

                <section v-if="!showRecipe">
                    <hr>

                    <div class="columns">
                        <div class="column is-2">
                            <b-button
                                v-if="isComponentModalActive == false"
                                icon-left="plus" @click="isComponentModalActive = true">
                                Ajouter une recette
                            </b-button>
                        </div>
                        <div class="column">
                            <!-- Confirmation suppression -->
                            <div class="has-text-right" v-if="isDelete">
                                <span>
                                    <button class="button is-danger" @click="deleteRecipe(idEqToDel)">Confirmation suppression</button>
                                </span>
                                &nbsp;
                                <span>
                                    <button class="button" @click="isDelete = false">Annuler</button>
                                </span>
                            </div>
                        </div>
                    </div>
                    
                    <hr>
                    <b-field label="Filtre par nom de recette" v-if="isComponentModalActive == false">
                        <b-input v-model="search"></b-input>                               
                    </b-field>
                    <b-field grouped group-multiline v-if="isComponentModalActive == false">
                        <b-select v-model="defaultSortDirection">
                            <option value="asc">Tri: Croissant</option>
                            <option value="desc">Tri: Décroissant</option>
                        </b-select>
                        <b-select v-model="perPage" :disabled="!isPaginated">
                            <option value="5">5 par page</option>
                            <option value="10">10 par page</option>
                            <option value="15">15 par page</option>
                            <option value="20">20 par page</option>
                        </b-select>
                        <div class="control">
                            <b-switch v-model="showDetailIcon">Détail des recettes</b-switch>
                        </div>
                    </b-field>

                    <b-table
                        v-if="isComponentModalActive == false"
                        :data="isEmpty ? [] : filterRecipes"
                        :paginated="isPaginated"
                        :per-page="perPage"
                        :opened-detailed="defaultOpenedDetails"
                        ref="table"
                        detailed
                        detail-key="id"
                        @details-open="(row, index) => $toast.open(`Expanded ${row.name}`)"
                        :show-detail-icon="showDetailIcon"
                        :current-page.sync="currentPage"
                        :pagination-simple="isPaginationSimple"
                        :default-sort-direction="defaultSortDirection"
                        default-sort="name"
                        aria-next-label="Page suivante"
                        aria-previous-label="Page précedente"
                        aria-page-label="Page"
                        aria-current-label="Page actuelle">

                        <template slot-scope="props">
                            <b-table-column field="name" label="Libellé" sortable>
                                <template v-if="showDetailIcon">
                                    {{ props.row.name }}
                                </template>
                                <template v-else>
                                    <a @click="toggle(props.row)">
                                        {{ props.row.name }}
                                    </a>
                                </template>
                            </b-table-column>

                            <b-table-column field="price" label="Prix" sortable>
                                {{ props.row.price }} €
                            </b-table-column>

                            <b-table-column field="duration" label="Durée" sortable>
                                {{ props.row.duration }} min
                            </b-table-column>

                            <b-table-column field="category.name" label="Catégorie" sortable>
                                {{ props.row.category.name }}
                            </b-table-column>

                            <b-table-column sortable centered>
                                <b-field grouped group-multiline>
                                    <div class="control is-flex">
                                        <button class="button is-warning" @click="getRecipe(props.row.id); showRecipe = true"><i class="fas fa-edit"></i></button>
                                    </div>
                                    <div>
                                        <button class="button is-danger" @click="callDelete(props.row.id)"><i class="fas fa-trash"></i></button>
                                    </div>
                                </b-field>
                            </b-table-column>
                        </template>

                        <template slot="detail" slot-scope="props">
                            <article class="media">
                                <div class="media-content">
                                    <div class="content">
                                        <p>
                                            <strong>{{ props.row.name }}</strong>
                                            <br>
                                            {{props.row.ingredient}}
                                            <hr>
                                            {{props.row.created_at}}
                                            <br>
                                                <img :src="props.row.image_one" height="200" width="200">
                                            <hr>
                                            Créé par : {{props.row.created_by.username}}
                                        </p>
                                    </div>
                                </div>
                            </article>
                        </template>

                        <!-- isEmpty -->
                        <template slot="empty">
                            <section class="section">
                                <div class="content has-text-grey has-text-centered">
                                    <p>
                                        <b-icon
                                            icon="emoticon-sad"
                                            size="is-large">
                                        </b-icon>
                                    </p>
                                    <p>Rien par ici.</p>
                                </div>
                            </section>
                        </template>
                    </b-table>
                    
                </section>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    data() {
        return {
            data:[],
            idEqToDel:'',
            error: false, 
            isPaginated: true,
            isPaginationSimple: false,
            defaultSortDirection: 'asc',
            currentPage: 1,
            perPage: 5,
            defaultOpenedDetails: [1],
            showDetailIcon: true,
            isDelete: false,
            isComponentModalActive: false,
            showRecipe: false,
            date: new Date(),
            file: null,
            recipe:{
                id: '',
                name: '',
                price: '',
                ingredient: '',
                duration: '',
                created_at: '',
                image_one: '',
                category: '',
                created_by: ''
            },
            isLoading: false,
            isFullPage: true,
            errors:'',
            search:'',
            isEmpty: false,
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
        categories(){
            return this.$store.state.recipes.categories
        },
        recipeOne(){
            return this.$store.state.recipes.recipe
        }
    },
    methods: {
        addRecipe(){
            const formData = new FormData();
       
            formData.append('name', this.recipe.name);
            formData.append('price', this.recipe.price);
            formData.append('ingredient', this.recipe.ingredient);
            formData.append('duration', this.recipe.duration);
            formData.append('created_at', this.recipe.created_at);
            formData.append('category', this.recipe.category);
            formData.append('created_by', 1);

            if (this.recipe.image_one){
                formData.append('image_one', this.recipe.image_one);
            }
            this.$store.dispatch('recipes/addRecipe', formData)

            this.errors = this.$store.dispatch('recipes/getErrors')
            // var error = this.errors.then( body => console.log( JSON.parse( body ) ) )
            // console.log(error)
            if(this.errors == 500){
                this.$notification.open({
                    duration: 500,
                    message: `Un problème est survenu lors de l'ajout, veuillez reessayer`,
                    position: 'is-bottom-right',
                    type: 'is-danger',
                    hasIcon: true
                })
            }
            else{
                this.isLoading = true
                this.recipe = []
                setTimeout(() => {
                    this.$store.dispatch('recipes/getRecipes');
                    //location.reload()
                    this.$el.textContent
                    this.isLoading = false
                    this.showRecipe = false
                    this.isComponentModalActive = false
                    this.$notification.open({
                        duration: 5000,
                        message: `Enregistrement effectué avec succès`,
                        position: 'is-bottom-right',
                        type: 'is-success',
                        hasIcon: true
                    })
                }, 500)   
            }
        },
        getRecipe(payload){
            this.$store.dispatch('recipes/getRecipe', payload)

            this.recipe.id = this.recipeOne.id
            this.recipe.name = this.recipeOne.name
            this.recipe.price = this.recipeOne.price
            this.recipe.ingredient = this.recipeOne.ingredient
            this.recipe.duration = this.recipeOne.duration
            this.recipe.created_at = this.recipeOne.created_at
            this.recipe.image_one = this.recipeOne.image_one
            this.recipe.image_two = this.recipeOne.image_two
            this.recipe.category = this.recipeOne.category.id
            this.recipe.created_by = this.recipeOne.created_by.id
        },
        callDelete(id){
            this.idEqToDel = id
            this.isDelete = true
        },
        deleteRecipe(payload){
            this.$store.dispatch('recipes/deleteRecipe', payload)
            this.isDelete = false
            this.errors = this.$store.dispatch('recipes/getErrors')
            console.log(this.errors)
            if(this.errors != 400 | this.erros != 500){
                setTimeout(() => {
                    this.$store.dispatch('recipes/getRecipes');
                    //location.reload()
                    this.$el.textContent
                    this.isDelete = false
                    this.isLoading = false
                    this.showRecipe = false
                    this.isComponentModalActive = false
                    this.$notification.open({
                        duration: 5000,
                        message: `Suppression effectuée avec succès`,
                        position: 'is-bottom-right',
                        type: 'is-success',
                        hasIcon: true
                    })
                }, 500)   
            }
            else
            {
                this.$notification.open({
                    duration: 5000,
                    message: `Suppression impossible, l'équipement est utilisé par une réservation`,
                    position: 'is-bottom-right',
                    type: 'is-danger',
                    hasIcon: true
                })
            }
        },
        updateRecipe(payload){
            this.$store.dispatch('recipes/updateRecipe', payload)
            this.errors = this.$store.dispatch('recipes/getErrors')
            if(this.errors == 400 | this.errors == 500){
                this.$notification.open({
                    duration: 20000,
                    message: `Un problème est survenu lors de la mise à jour, veuillez reessayer`,
                    position: 'is-bottom-right',
                    type: 'is-danger',
                    hasIcon: true
                })
            }
            else
            {
                this.isLoading = true
                setTimeout(() => {
                    this.$store.dispatch('recipes/getRecipes');
                    //location.reload()
                    this.$el.textContent
                    this.isLoading = false
                    this.showRecipe = false
                    this.$notification.open({
                        duration: 5000,
                        message: `Mise à jour effectuée avec succès`,
                        position: 'is-bottom-right',
                        type: 'is-success',
                        hasIcon: true
                    })
                }, 500)
                
            }
        }
        ,
        //Pour la liste déroulante de ingredient
        toggle(row) {
            this.$refs.table.toggleDetails(row)
        },
    },
    created() {
        this.$store.dispatch('recipes/getRecipes');
        this.$store.dispatch('recipes/getCategories');
    }
}
</script>