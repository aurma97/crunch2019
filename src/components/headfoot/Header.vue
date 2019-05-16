<template>
    <header>
        <!-- <nav class="navbar" role="navigation" aria-label="main navigation">
            <div class="container">
                <nav class="navbar is-link is-bold is-fixed-top has-shadow" role="navigation" aria-label="main navigation">
            <div id="vue-app" class="container">
                <div class="navbar-brand">
                    <router-link to="/">
                        <img src="https://www.utbm.fr/wp-content/uploads/2015/04/logo_utbm.png" width="170" height=700 alt="Menu">
                    </router-link>
                </div>

                <div id="navMenu" class="navbar-menu" v-bind:class="{'is-active': active}">
                    <div class="navbar-start">
                    </div>
                    <div class="navbar-end">
                        <router-link class="navbar-item" to="/equipements" exact>
                            <i class="fas fa-hamburger"></i>&nbsp;&nbsp;Produits
                        </router-link>
                        <router-link class="navbar-item" to="/permissions" exact>
                            <i class="fas fa-concierge-bell"></i>&nbsp;&nbsp;Recettes
                        </router-link>
                        <router-link class="navbar-item" to="/support" exact>
                            <i class="fas fa-file-invoice"></i>&nbsp;&nbsp;Commandes
                        </router-link>
                    </div>     
                </div>
            </div>
        </nav>
        <hr>
        </div>
        </nav> -->
        <section class="hero is-light is-bold">
    <!-- Hero head: will stick at the top -->
        <div class="hero-head">
            <header class="navbar">
            <div class="container">
                <div class="navbar-brand">
                    <router-link to="/">
                        <img src="http://innovation-crunch.utbm.fr/wp-content/uploads/2019/02/CRUNCHTIME-QUADRI.png" height="200" width="200" alt="Logo">
                    </router-link>
                <span class="navbar-burger burger" data-target="navbarMenuHeroC">
                    <span></span>
                    <span></span>
                    <span></span>
                </span>
                </div>
                <div id="navbarMenuHeroC" class="navbar-menu">
                <div class="navbar-end">
                    <router-link class="navbar-item" to="/products" exact>
                        <i class="fas fa-hamburger"></i>&nbsp;&nbsp;Produits
                    </router-link>
                    <router-link class="navbar-item" to="/recipes" exact>
                        <i class="fas fa-concierge-bell"></i>&nbsp;&nbsp;Recettes
                    </router-link>
                    <router-link class="navbar-item" to="/commands" exact>
                        <i class="fas fa-file-invoice"></i>&nbsp;&nbsp;Commandes
                    </router-link>
                    <span class="navbar-item">
                        <a class="button is-light">
                            <span class="icon">
                            <i class="fas fa-shopping-cart"></i>
                            </span>
                            <span>Panier</span>
                        </a>
                    </span>
                    <span class="navbar-item">
                        <a class="button is-light is-inverted">
                            <span class="icon">
                            <i class="fas fa-user"></i>
                            </span>
                            <span>Connexion</span>
                        </a>
                    </span>
                </div>
                </div>
            </div>
            </header>
        </div>

        <!-- Hero content: will be in the middle -->
        <div class="hero-body">
            <div class="container has-text-centered">
            <h1 class="title">
                <div class="control has-icons-left is-fullwidth">
                    <input class="input is-medium" type="text" placeholder="Rechercher...">
                    <span class="icon is-left">
                        <i class="fas fa-search"></i>
                    </span>
                </div>
            </h1>
            <h2 class="subtitle">
             
            </h2>
            </div>
        </div>
        </section>
    </header>
</template>

<script>

export default {
    data(){
        return{
            active: false,
            username: 'Marcel'
        }
    },
    computed : {

    },
    created(){
    },
    mounted(){
     
    },
    methods: {
    
    }
}
</script>