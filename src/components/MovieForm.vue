<template>
  <form id="movieForm" @submit.prevent="saveMovie">
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input type="text" name="title" v-model="title" class="form-control" required />
    </div>
    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea name="description" v-model="description" class="form-control" required></textarea>
    </div>
    <div class="form-group mb-3">
      <label for="poster" class="form-label">Poster</label>
      <input type="file" name="poster" @change="onFileChange" class="form-control" required />
    </div>
    <button type="submit" class="btn btn-primary">Add Movie</button>
    <div v-if="message" class="alert alert-success mt-3">{{ message }}</div>
    <div v-if="errors.length" class="alert alert-danger mt-3">
      <ul>
        <li v-for="error in errors" :key="error.field">{{ error.message }}</li>
      </ul>
    </div>
  </form>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const title = ref('');
const description = ref('');
const poster = ref(null);
const message = ref('');
const errors = ref([]);
const csrf_token = ref('');

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      console.log('CSRF Token received:', data);
      csrf_token.value = data.csrf_token;
    })
    .catch((error) => {
      console.error('Error fetching CSRF token:', error);
    });
}

onMounted(() => {
  getCsrfToken();
});

const saveMovie = async () => {
  let movieForm = document.getElementById('movieForm');
  let form_data = new FormData(movieForm);

  try {
    const response = await fetch('/api/v1/movies', {
      method: 'POST',
      body: form_data,
      headers: {
        'X-CSRFToken': csrf_token.value
      },
    });
    const data = await response.json();
    if (response.ok) {
      message.value = data.message;
      title.value = '';
      description.value = '';
      poster.value = null;
      errors.value = [];
    } else {
      errors.value = data.errors;
    }
  } catch (error) {
    console.error(error);
    errors.value.push({
      field: 'general',
      message: 'An error occurred while saving the movie.'
    });
  }
};

const onFileChange = (event) => {
  poster.value = event.target.files[0];
};
</script>

<style scoped>
/* Add any necessary styles here */
</style>
