<template>
  <ul class="list-group ">
    <li class="list-group-item" v-for="ingr in ingredients" v-bind:key="ingr.id">
      <div class="flex-column">
        <b-button variant="outline-dark" v-on:click="onClick">{{ ingr.name }}</b-button>

        <div>
          <span class="badge badge-primary mr-1">{{ ingr.effect1.name }}</span>
          <span class="badge badge-primary mr-1">{{ ingr.effect2.name }}</span>
          <span class="badge badge-primary mr-1">{{ ingr.effect3.name }}</span>
          <span class="badge badge-primary mr-1">{{ ingr.effect4.name }}</span>
        </div>

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
    methods: {
      getSameIngredients() {
        const path = 'http://localhost:5000/getsameingredients';
        axios.get(path)
          .then((res) => {
            this.ingredients = res.data.ingredients;
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      },
      onClick: function () {
          console.log('tratata')
      }
    },
    created() {
      this.getSameIngredients();
    },
  };
</script>

<style scoped>
.list-group-item {
  display: flex;
  justify-content: space-between;
  width: 100%;
}
</style>
