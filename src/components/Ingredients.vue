<template>
  <div class="col-3 px-1">
    <div class="card">
      <h5 class="card-header bg-info"><slot name="header"></slot> Ingredient [{{ingrCount}}]</h5>

      <div v-if="selected" class="card-body">
        <pre>{{selectedAll}}</pre>
        <div class="row">
            <div class="col-md-12 d-flex">
              <h4>{{ selected.Name }}</h4>
              <b-button class="ml-auto" size="sm" variant="danger" @click="onClickDelete">Delete</b-button>
            </div>
        </div>

        <ul class="list-unstyled">
          <li v-for="effect in [selected.Effect1, selected.Effect2, selected.Effect3, selected.Effect4]">
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
            <li v-for="i in [ingr.Effect1, ingr.Effect2, ingr.Effect3, ingr.Effect4]">
              <b-link class="effect" href="#" @click="onClickEffect">{{ i }}</b-link>
            </li>
          </ul>

        </div>
      </li>
    </ul>
  </div>
</template>

<script>
  /*eslint no-console: ["error", { allow: ["warn", "error", "log"] }] */

  // import axios from 'axios';

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
        selected: Object,
        selectedAll: Array,
        id: Number
    },


    computed: {
      ingrCount: function () {
          if (this.ingredients) {
            return this.ingredients.length
          } else {
              return 0
          }
      }
    },

    methods: {
      onClickIngr: function (event) {
          // console.log(event);
          // console.log(event.target.textContent);
          console.log('call onClickIngr');
          console.log(event);

          // console.log(this.ingredients[0]);
          // console.log(this.ingredients.find(x => x.Name === event.target.textContent));
          // deprecated this.choosedIngredient = event.target.textContent;
          this.$emit('clickIngr', event.target.textContent, this.id)
      },
      onClickEffect: function (event) {
          this.$emit('clickEffect', event.target.textContent)
      },
      onClickDelete: function () {
          this.$emit('deleteIngr', this.id)
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
.choosed-effect {
  font-size: 0.9em;
  color: blue;
}
.list-unstyled {
  line-height: 15px;
  margin-block-end: 0;
}
</style>
