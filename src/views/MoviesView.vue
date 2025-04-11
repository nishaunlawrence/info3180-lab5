<template>
  <div class="container">
    <h1 class="my-4">Movies List</h1>
    <div class="row">
      <div class="col-md-4" v-for="movie in movies" :key="movie.id">
        <div class="card mb-4">
          <img :src="movie.poster" class="card-img-top" alt="Movie Poster" />
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p class="card-text">{{ movie.description }}</p>
          </div>
        </div>
      </div>
    </div>
    <div v-if="movies.length === 0">
      <p>No movies found.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const movies = ref([]);

const fetchMovies = async () => {
  try {
    const response = await fetch('/api/v1/movies');
    const data = await response.json();
    movies.value = data.movies;
  } catch (error) {
    console.error('Error fetching movies:', error);
  }
};

onMounted(fetchMovies);
</script>

<style scoped>
.card {
  border: 1px solid #ccc;
  padding: 16px;
  margin: 16px 0;
}
</style>
