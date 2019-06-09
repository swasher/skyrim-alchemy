<template>
  <ul class="list-group ">
    <li class="list-group-item px-0" v-for="ingr in ingredients" v-bind:key="ingr.id"
        v-show="effectMatch(ingr.effect1.name, ingr.effect2.name, ingr.effect3.name, ingr.effect4.name)">


      <div class="col-5">
        <b-button class="text-left ingr-button" size="sm"
                  variant="outline-dark" v-text="ingr.name" v-on:click="onClick(ingr.formid)"></b-button>
      </div>

      <div class="col-7">
        <ul class="list-unstyled">
          <li>
            <b-link class="effect" href="#">{{ ingr.effect1.name }}</b-link>
          </li>
          <li>
            <b-link class="effect" href="#">{{ ingr.effect2.name }}</b-link>
          </li>
          <li>
            <b-link class="effect" href="#">{{ ingr.effect3.name }}</b-link>
          </li>
          <li>
            <b-link class="effect" href="#">{{ ingr.effect4.name }}</b-link>
          </li>
        </ul>
      </div>
    </li>
  </ul>
</template>

<script>
  /*eslint no-console: ["error", { allow: ["warn", "error", "log"] }] */
  import axios from 'axios';

  export default {
    name: 'Ingredients',
    data() {
      return {
        ingredients: [],
      };
    },
    // computed: {
    //   eff: ['Опустошение здоровья', 'Опустошение магии']
    // },
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
  };
</script>

<style scoped>
.ingr-button {
  line-height: 0.9em;
}
.list-group-item {
  display: flex;
  justify-content: space-between;
  width: 100%;
}
.effect {
  font-size: 0.8em;

}
.list-unstyled {
  line-height: 15px;
}
</style>
