<template>
  <div class="col-sm-3">
    <div class="card">
      <h5 class="card-header bg-info"><slot name="header"></slot> Ingredient</h5>
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
</template>

<script>
  export default {
    name: 'Header',
  }
</script>
