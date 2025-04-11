<template>
  <nav>
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/movies/create">Create Movie</router-link></li>
      <li><router-link to="/movies">Movies</router-link></li>
    </ul>
  </nav>
</template>

<script setup>
import { RouterLink } from "vue-router";
</script>

<style>
/* Add any component specific styles here */
</style>
