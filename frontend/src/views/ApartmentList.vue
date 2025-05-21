<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-4">Квартири</h1>

    <div class="mb-4 grid grid-cols-1 md:grid-cols-4 gap-4">
      <input v-model="filters.search" @input="fetchApartments" type="text" placeholder="Пошук..." class="p-2 border rounded w-full">
      <input v-model.number="filters.price" @input="fetchApartments" type="number" placeholder="Макс. ціна" class="p-2 border rounded w-full">
      <input v-model.number="filters.rooms" @input="fetchApartments" type="number" placeholder="К-сть кімнат" class="p-2 border rounded w-full">
      <select v-model="filters.available" @change="fetchApartments" class="p-2 border rounded w-full">
        <option value="">Будь-який статус</option>
        <option value="true">Доступні</option>
        <option value="false">Недоступні</option>
      </select>
    </div>

    <div v-if="loading" class="text-center">Завантаження...</div>
    <div v-else>
      <div v-if="apartments.length === 0" class="text-gray-500">Нічого не знайдено</div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <router-link
          v-for="apt in apartments"
          :key="apt.id"
          :to="`/apartments/${apt.id}`"
          class="border p-4 rounded shadow hover:shadow-lg transition duration-300"
          :class="{ 'opacity-50 blur-sm pointer-events-none': !apt.availability }"
        >
          <h2 class="text-xl font-semibold">{{ apt.name }}</h2>
          <p class="text-sm text-gray-600">{{ apt.description }}</p>
          <p class="mt-2">Ціна: {{ apt.price }} грн</p>
          <p>Кімнат: {{ apt.number_of_rooms }}</p>
          <p>Площа: {{ apt.square }} м²</p>
        </router-link>
      </div>

      <div class="mt-6 flex justify-center items-center space-x-2">
        <button @click="changePage(page - 1)" :disabled="page === 1" class="px-4 py-2 bg-gray-200 rounded">Назад</button>
        <span>Сторінка {{ page }}</span>
        <button @click="changePage(page + 1)" :disabled="!hasNextPage" class="px-4 py-2 bg-gray-200 rounded">Далі</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import axios from 'axios';

const apartments = ref([]);
const loading = ref(false);
const page = ref(1);
const hasNextPage = ref(false);

const filters = ref({
  search: '',
  price: '',
  rooms: '',
  available: '',
});

const fetchApartments = async () => {
  loading.value = true;
  try {
    const params = {
      page: page.value,
      search: filters.value.search,
      price_max: filters.value.price,
      rooms: filters.value.rooms,
      available: filters.value.available,
    };

    const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/v1/apartments/`, { params });
    apartments.value = response.data.results;
    hasNextPage.value = !!response.data.next;
  } catch (e) {
    console.error('Помилка при отриманні квартир:', e);
  } finally {
    loading.value = false;
  }
};

const changePage = (newPage) => {
  page.value = newPage;
  fetchApartments();
};

onMounted(fetchApartments);
watch(filters, () => {
  page.value = 1;
  fetchApartments();
});
</script>

<style scoped>
</style>
