<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div id="app">
    <div class="container-fluid">
      <div class="row">

        <Header>
          <template v-slot:header>First</template>
        </Header>
        <Header>
          <template v-slot:header>Second</template>
        </Header>
        <Header>
          <template v-slot:header>Third</template>
        </Header>

      </div>
      <p></p>

      <div class="row">
        <div class="col-3">
          <Ingredients :ingredients=ingredients />
        </div>
        <div class="col-3">
<!--          <Ingredients2/>-->
        </div>
        <div class="col-3">
<!--          <Ingredients2/>-->
        </div>
      </div>
    <!--    <Effect/>-->
    </div>

  </div>
</template>

<script>
/*eslint no-console: ["error", { allow: ["warn", "error", "log"] }] */
import axios from 'axios';
import Ingredients from './components/Ingredients.vue'
// import Ingredients2 from './components/Ingredients2.vue'
import Header from './components/Header.vue'
// import Effect from './components/Effect.vue'

export default {
  name: 'app',

  components: {
    Ingredients,
    // Ingredients2,
    Header,
  },

  data() {
    return {
      ingredients: [],
    };
  },

  methods: {
    getIngredients() {
      const path = 'http://localhost:5000/ingredients';
      axios.get(path)
        .then((res) => {
          this.ingredients = res.data.ingredients;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    onClick: function (id) {
        console.log(id)
    },
    effectMatch: function(eff1, eff2, eff3, eff4) {
        // function containsAny(source,target)
      var source = [eff1, eff2, eff3, eff4];
      // var target = ['Опустошение здоровья', 'Опустошение магии'];
      var target = [];
      if (target.length > 0) {
        var result = source.filter(function(item){ return target.indexOf(item) > -1});
        return (result.length > 0);
      } else {
        return 1
      }
    }
  },
  created() {
    this.getIngredients();
  },


}
</script>

<style>
/*#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}*/
</style>
