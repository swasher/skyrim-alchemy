<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div id="app">
    <div class="container-fluid">
      <div class="row">

        <Ingredients :ingredients=ingredients1 :selected=selected1 :selected-all="selectedAll" :id=1
                     @clickIngr="handleIngr" @clickEffect="handleEffect" @deleteIngr="deleteIngr">
          <template v-slot:header>First</template>
        </Ingredients>

        <Ingredients :ingredients=ingredients2 :selected=selected2 :id=2
                     @clickIngr="handleIngr" @clickEffect="handleEffect" @deleteIngr="deleteIngr" >
          <template v-slot:header>Second</template>
        </Ingredients>

        <Ingredients :ingredients=ingredients3 :selected=selected3 :id=3
                     @clickIngr="handleIngr" @clickEffect="handleEffect" @deleteIngr="deleteIngr" >
          <template v-slot:header>Third</template>
        </Ingredients>
      </div>

    </div>
  </div>
</template>

<script>
/*eslint no-console: ["error", { allow: ["warn", "error", "log"] }] */
import Ingredients from './components/Ingredients.vue'
// import Header from './components/Header.vue'
// import Effect from './components/Effect.vue'
// import Proba from "./components/Proba.vue";
import json from '../ingredient_out.json'

function effectsOfIngr(ingr) {
  return [ingr.Effect1, ingr.Effect2, ingr.Effect3, ingr.Effect4]
}

export default {
  name: 'app',

  components: {
    Ingredients,
  },


  data() {
    return {
      ingredients: json,
      selected1: null,
      selected2: null,
      selected3: null,
    }
  },


  computed: {
    ingredients1: function () {
      return this.ingredients
    },
    ingredients2: function () {
      // let filter_effects = this.ingredients.find(x => x.Name === this.selected1);
      // console.log('Filter by: ', filter_effects);
      console.log('ingr2 start computed...');
      return this.filterByIngredient(this.selected1);
    },
    ingredients3: function () {
      console.log('ingr3 start computed...');
      return this.filterByIngredient(this.selected2);
    },
    selectedAll: function () {
      return [this.selected1, this.selected2, this.selected3]
    }
  },

  methods: {

    handleIngr: function (ingr_name, id) {
      console.log('click Ingr (msg from parent), Ingr=' + ingr_name + ' INGREDIEN'+id);
      let ingr_obj = this.getIngrByName(ingr_name);

      switch (id) {
          case 1:
              this.selected1 = ingr_obj;
              break;
          case 2:
              this.selected2 = ingr_obj;
              break;
          case 3:
              this.selected3 = ingr_obj;
              break
      }
    },

    deleteIngr: function (id) {
      switch (id) {
          case 1:
              this.selected1 = null;
              this.selected2 = null;
              this.selected3 = null;
              break;
          case 2:
              this.selected2 = null;
              this.selected3 = null;
              break;
          case 3:
              this.selected3 = null;
              break
      }
    },



    handleEffect: function () {
      console.log('click Effect (msg from parent)')
    },

    getIngrByName: function (name) {
        return this.ingredients.find(x => x.Name === name);
    },


    filterByIngredient: function(ingrObj) {
      // На входе - ингридиент-объект
      // На выходе - отфильтрованый набор объектов, у каждого из которых есть хотя бы один эффект,
      // совпадаюший с эффектом входного ингридиента

      if (ingrObj) {
        console.log('ingr: ', ingrObj.Name);
        // let ingrEffects = [ingr.Effect1, ingr.Effect2, ingr.Effect3, ingr.Effect4];

        // эффекты входящего ингридиента
        let ingrEffects = effectsOfIngr(ingrObj);

        // this.ingredients.forEach(function (elem, index)  { console.log('eff:', effectsOfIngr(elem)) });

        // нам нужно вернуть true, если у iterIngr есть хоть одно свойство(эффект), имеющееся в ingrEffects
        let filteredIngr = this.ingredients.filter(function (item) {
              // console.log(ingrEffects.indexOf(effectsOfIngr(item)));
              // return false
              // return -1 !== effectsOfIngr(item).indexOf(ingrEffects)
              return  (effectsOfIngr(item).filter(value => -1 !== ingrEffects.indexOf(value))).length
            }
        );
        console.log('filteredIngr:', filteredIngr);
        return filteredIngr
      } else {
        return null
      }
    }

  },
  // created() {
  //   this.getIngredients();
  // },


  filterByEfect: function () {
      // filter by one effect
  }



}
</script>

<style>
</style>
