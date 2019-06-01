<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-6">
        <div class="card">
          <h5 class="card-header bg-info">First Ingredient</h5>
          <div class="card-body">
            <h5 class="card-title">Special title treatment</h5>
            <span class="badge badge-primary">Primary</span>
            <span class="badge badge-secondary">Secondary</span>
            <span class="badge badge-success">Success</span>
            <span class="badge badge-danger">Danger</span>
            <a href="#" class="card-link text-danger">Remove</a>
          </div>
        </div>
      </div>
      <div class="col-sm-6">
        <div class="card">
          <h5 class="card-header bg-info">Second Ingredient</h5>
          <div class="card-body">
            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
            <span class="badge badge-primary">Primary</span>
            <span class="badge badge-secondary">Secondary</span>
            <span class="badge badge-success">Success</span>
            <span class="badge badge-danger">Danger</span>
            <a href="#" class="card-link text-danger">Remove</a>
          </div>
        </div>
      </div>
    </div>
    <p>


    <div class="row">
      <div class="col-6">

        <ul class="list-group " v-for="ingr in ingredients" :key="ingr.name">
          <li class="list-group-item">
            <div class="flex-column">
              {{ ingr.name }}
              <div>
                <span class="badge badge-primary mr-1">{{ ingr.effect1.name }}</span>
                <span class="badge badge-primary mr-1">{{ ingr.effect2.name }}</span>
                <span class="badge badge-primary mr-1">{{ ingr.effect3.name }}</span>
                <span class="badge badge-primary mr-1">{{ ingr.effect4.name }}</span>
              </div>
            </div>
            <div class="flex-column">
              <div class="btn-group btn-group-sm" role="group">
                <button type="button" class="btn btn-warning">1</button>
                <button type="button" class="btn btn-info">2</button>
              </div>
            </div>
          </li>
        </ul>
      </div>
      11
<!--      <ol>
        &lt;!&ndash; Создаём экземпляр компонента todo-item &ndash;&gt;
        <todo-item></todo-item>
      </ol>-->
      333
    </div>
  </div>
</template>


Vue.component('todo-item', {
  template: '<li>Это одна задача в списке</li>'
})

Vue.component('prop', {
  template: '<li></li>'
})

<script>
import axios from 'axios';

export default {
  name: 'Ingredients',
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
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getIngredients();
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
