<template>
  <a v-bind:href="url" class="nav-link" >
    SLOT:
    <slot></slot>
  </a>
</template>


<script>
  export default {
      name: 'Navigation',
      data() {
          return {
          };
      },
  }
</script>
