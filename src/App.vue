<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
    <div id="app">
        <div class="container-fluid">
            <div class="row">

                <!--  todo  использовать v-for для отрисовки этих трех компонетнтов https://ru.vuejs.org/v2/guide/list.html#Компоненты-и-v-for-->

                <Ingredients :ingredients=ingredients1 :selected=selected :id=0
                             @clickIngr="handleIngr" @clickEffect="handleEffect" @deleteIngr="deleteIngr">
                    <template v-slot:header>First</template>
                </Ingredients>

                <Ingredients :ingredients=ingredients2 :selected=selected :id=1
                             @clickIngr="handleIngr" @clickEffect="handleEffect" @deleteIngr="deleteIngr" >
                    <template v-slot:header>Second</template>
                </Ingredients>

                <Ingredients :ingredients=ingredients3 :selected=selected :id=2
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
        // deprecated
        // selected1: null,
        // selected2: null,
        // selected3: null,
        selected: [null, null, null]
      }
    },


      computed: {

          ingredients1: function () {
              console.log('ingr1 start computed...');
              // THIS WORKED return this.ingredients.filter(x => !this.getCurrentSelected().includes(x.Name))
              return this.ingredients.filter(x => !this.isSelected(x.Name))
          },
          ingredients2: function () {
              // let filter_effects = this.ingredients.find(x => x.Name === this.selected1);
              // console.log('Filter by: ', filter_effects);
              console.log('ingr2 start computed...');
              return this.filterByIngredient(this.selected[0])
          },
          ingredients3: function () {
              console.log('ingr3 start computed...');
              return this.filterByIngredient(this.selected[1]);
          },


          // deprecated
          // selectedAll: function () {
          //   return [this.selected1, this.selected2, this.selected[3]]
          // }
      },

    methods: {

      handleIngr: function (ingr_name, id) {
        console.log('click Ingr (msg from parent), Ingr=' + ingr_name + ' INGREDIEN'+id);
        let ingr_obj = this.getIngrByName(ingr_name);

        switch (id) {
          case 0:
            this.$set(this.selected, 0, ingr_obj);
            break;
          case 1:
            this.$set(this.selected, 1, ingr_obj);
            break;
          case 2:
            this.$set(this.selected, 2, ingr_obj);
            break
        }
        console.log('Selected updated:', this.selected)
      },

      deleteIngr: function (id) {
        switch (id) {
          case 0:
            this.$set(this.selected, 0, null);
            this.$set(this.selected, 1, null);
            this.$set(this.selected, 2, null);
            break;
          case 1:
            this.$set(this.selected, 1, null);
            this.$set(this.selected, 2, null);
            break;
          case 2:
            this.$set(this.selected, 2, null);
            break
        }
      },

      handleEffect: function () {
        console.log('click Effect (msg from parent)')
      },

      getIngrByName: function (name) {
        // возвращает ингридиеинт в виде объекта по иго имени (string)
        return this.ingredients.find(x => x.Name === name)
      },


        getCurrentSelected () {
            return this.selected.flatMap(x => x ? x.Name : [])
        },

        isSelected: function (name) {
              if (this.getCurrentSelected()) {
                  return this.getCurrentSelected().includes(name)
              } else {
                  return true
              }
        },


      filterByIngredient: function(inputIngr) {
          // На входе - ингридиент-объект
          // На выходе - отфильтрованый массив ingredients, по признаку, что у каждого ингридиента есть хотя бы один эффект,
          // совпадаюший с одним из эффектов входного ингридиента

          if (!inputIngr) {
              return null
          }

          // эффекты входящего ингридиента
          let ingrEffects = effectsOfIngr(inputIngr);

          // возвращаем отфильтрованный массив
          let arr = this.ingredients.filter(
              function (item) {
                  // возвращает true, если у item есть хоть одно свойство(эффект), имеющееся в ingrEffects

                  return (
                      effectsOfIngr(item).// этот фильтр возвращает массив совпавших эффектов. Так, если хоть один эффект совпал, то длина массива будет более нуля, то есть вернет true
                      filter(value => -1 !== ingrEffects.indexOf(value))
                  ).length;
              }
          );

          console.log('arr=', arr);
          console.log('this.getCurrentSelected()=', this.getCurrentSelected());

          // Так же удаляем из всех трех списков уже выбранные компоненты.
          // todo походу, из ПЕРВОГО списка так не удаляется, потому что к нему не применяется этот метод
          // TODO Сделал хак, теперь фильтруется прямо в функции computed:ingrediant1. Это надо сделать красиво
          // в одном месте.
          return arr.filter(x => !this.isSelected(x.Name))

      }
    }
    // created() {
    //   this.getIngredients();
    // },
  }
</script>

<style>
</style>
