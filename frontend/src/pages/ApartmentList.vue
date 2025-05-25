<template>
  <div class="p-4 max-w-4xl mx-auto">
    <form @submit.prevent="fetchApartments" class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
      <input v-model="filters.search" type="text" placeholder="Пошук..." class="input" />

      <div class="flex gap-2">
        <input v-model="filters.price_min" type="number" placeholder="Мін. ціна" class="input" />
        <input v-model="filters.price_max" type="number" placeholder="Макс. ціна" class="input" />
      </div>

      <select v-model="filters.rooms" class="input">
        <option value="">Кімнати</option>
        <option v-for="n in 5" :key="n" :value="n">{{ n }}</option>
      </select>

      <select v-model="filters.available" class="input">
        <option value="">Доступність</option>
        <option :value="true">Доступні</option>
        <option :value="false">Недоступні</option>
      </select>

      <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
        Застосувати
      </button>
    </form>

    <div v-if="apartments.length === 0">Квартир не знайдено.</div>

    <div class="grid gap-4">
      <div
        v-for="apartment in apartments"
        :key="apartment.slug"
        class="p-4 border rounded hover:bg-gray-50"
        :class="{ 'opacity-50 blur-sm': apartment.available === false }"
      >
        <router-link :to="`/apartments/${apartment.slug}`" class="font-bold text-lg">
          {{ apartment.name }}
        </router-link>
        <p>{{ apartment.description }}</p>
        <p>{{ apartment.price }} грн / {{ apartment.number_of_rooms }} кімн.</p>
      </div>
    </div>

    <!-- Пагінація -->
    <div class="mt-4 flex justify-between">
      <button @click="page--" :disabled="page === 1" class="btn">Попередня</button>
      <button @click="page++" class="btn">Наступна</button>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import api from '../services/api';

const apartments = ref([]);
const page = ref(1);

const filters = ref({
  search: '',
  price_min: '',
  price_max: '',
  rooms: '',
  available: ''
});

async function fetchApartments() {
  const params = {
    page: page.value,
    ...filters.value
  };
  const res = await api.get('/api/v1/apartments/', { params });
  apartments.value = res.data;
}

watch(page, fetchApartments);
fetchApartments();
</script>

<style scoped>
.input {
  @apply w-full px-3 py-2 border border-gray-300 rounded;
}
.btn {
  @apply px-4 py-2 bg-gray-200 rounded hover:bg-gray-300;
}
</style>
