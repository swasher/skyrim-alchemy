<template>
  <div class="col-3 px-1">
    <div class="card">
      <h5 class="card-header bg-info"><slot name="header"></slot> Ingredient [{{ingrCount}}]</h5>

      <div v-if="selected[id]" class="card-body">

        <div class="row">
            <div class="col-md-12 d-flex">
              <h4>{{ selected[id].Name }}</h4>
              <b-button class="ml-auto" size="sm" variant="danger" @click="onClickDelete">Delete</b-button>
            </div>
        </div>

        <ul class="list-unstyled">
          <li v-for="effect in effectsOfIngr(selected[id])">
            <b-link class="choosed-effect" href="#">{{ effect }}</b-link>
          </li>
        </ul>
      </div>

    </div>

    <ul class="list-group ">
      <li class="list-group-item p-1" v-for="ingr in ingredients" v-bind:key="ingr.FormID">

        <div class="col-4 px-2 pt-1">
          <b-button class="text-left ingr-button" size="sm" variant="outline-dark"
                    v-text="ingr.Name" @click="onClickIngr"></b-button>
        </div>

        <div class="col-8 px-1">

          <ul class="list-unstyled">
            <li v-for="effect in effectsOfIngr(ingr)" >

<!--
              <b-link v-if="checkMatch(effect)" class="effect-match" href="#" @click="onClickEffect">{{ effect }}</b-link>
              <b-link v-else class="effect" href="#" @click="onClickEffect">{{ effect }}</b-link>
-->
              <b-link class="effect" :class="setEffectClass(effect)" @click="onClickEffect">{{ effect }}</b-link>

            </li>
          </ul>

        </div>
      </li>
    </ul>
  </div>
</template>

<script>
/*eslint no-console: ["error", { allow: ["warn", "error", "log"] }] */



export default {
  name: 'Ingredients',


  // deprecated
  // data () {
  //     return{
  //         choosedIngredient: '',
  //     }
  // },

  props: {
    ingredients: Array,
    selected: Array,
    id: Number
  },


  computed: {
    ingrCount: function () {
      if (this.ingredients) {
        return this.ingredients.length
      } else {
        return 0
      }
    },
  },

  methods: {
    onClickIngr: function (event) {
        console.log('call onClickIngr');
        this.$emit('clickIngr', event.target.textContent, this.id)
    },
    onClickEffect: function (event) {
        this.$emit('clickEffect', event.target.textContent)
    },
    onClickDelete: function () {
        this.$emit('deleteIngr', this.id)
    },
    effectsOfIngr(ingr) {
      return [ingr.Effect1, ingr.Effect2, ingr.Effect3, ingr.Effect4]
    },

    setEffectClass: function (effect) {
      if (this.id === 0) {

        // Обрабатываем подсветку на первом ингридиенте.
        // логика такая - если пользователь кликнул на эффекте, то подсвечиваются в этом столбце все такие же эффекты,
        // чтобы пользователь мог заменить ингридиент.
        // todo Эти эффекты при сортировке должны идти сначала
        //
        // Если пользователь кликнул на ингридиенте, то или ничего не
        // подсвечивается, или все четыре эффекта (подумать)

        if (this.selected[this.id]) {
          if (this.effectsOfIngr(this.selected[this.id]).includes(effect)) {
            return {'effect-match': true}
          }
        }

      } else if (this.id === 1) {

        // Обработка второго столбца.
        // Нам нужно подсветить эффекты, имеющиеся в selected[0]
        // todo и вывести их при сортировке вначало, учитывая кол-во совпадающих эффектов в ингридиете

        if (this.selected[0]) {
          if (this.effectsOfIngr(this.selected[0]).includes(effect)) {
            return {'effect-match': true}
          }
        }

      }
    }

  }

};
</script>

<style scoped>
.ingr-button {
  line-height: 1em;
}
.list-group-item {
  display: flex;
  justify-content: space-between;
  width: 100%;
}
.effect {
  font-size: 0.8em;
  color: cadetblue;
}
.effect-match {
  font-size: 0.8em;
  color: red;
  font-weight: bold;
}
.choosed-effect {
  font-size: 0.9em;
  color: blue;
}
.list-unstyled {
  line-height: 15px;
  margin-block-end: 0;
}
</style>
