<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold mb-4">Квартири</h1>
    <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
      <div
        v-for="apartment in apartments"
        :key="apartment.id"
        class="border rounded p-4 shadow hover:shadow-md"
        :class="!apartment.availability ? 'opacity-50 blur-sm pointer-events-none' : ''"
      >
        <h2 class="text-lg font-semibold">{{ apartment.name }}</h2>
        <p class="text-sm">{{ apartment.description }}</p>
        <router-link :to="`/apartments/${apartment.id}`" class="text-blue-600 underline">Деталі</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from '@/api/axios';

const apartments = ref([]);

onMounted(async () => {
  try {
    const { data } = await api.get('/apartments/');
    apartments.value = data.results || data;
  } catch (err) {
    console.error('Error fetching apartments:', err);
  }
});
</script>
