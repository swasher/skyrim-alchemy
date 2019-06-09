<template>
  <div id="app">
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-3">
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
        <div class="col-sm-3">
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
        <div class="col-sm-3">
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
      <p></p>

      <div class="row">
        <div class="col-3">
          <Ingredients/>
        </div>
        <div class="col-3">
          <Ingredients2/>
        </div>
        <div class="col-3">
          <Ingredients2/>
        </div>
      </div>
    <!--    <Effect/>-->
    </div>



  </div>
</template>

<script>
import Ingredients from './components/Ingredients.vue'
import Ingredients2 from './components/Ingredients2.vue'
// import Effect from './components/Effect.vue'

export default {
  name: 'app',
  components: {
    Ingredients,
    Ingredients2,
  }
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
