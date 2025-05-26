<template>

    
    <!-- Прозрачный контейнер -->
    <div class="fon">
      <div class="bg-white/60 rounded-xl p-4">
        <h1 class="text-3xl font-bold text-gray-800 mb-4">Список Квартир</h1>
        <p class="text-gray-600 mb-6">Знайдіть ідеальну квартиру для себе!</p>
        </div>
      <!-- Фильтр -->
      <form
        @submit.prevent="fetchApartments"
        class="grid md:grid-cols-4 gap-4 mb-6 bg-white bg-opacity-80 p-4 rounded-xl shadow"
      >
        <input v-model="filters.search" type="text" placeholder="🔍 Пошук..."
          class="input col-span-2 md:col-span-1" />

        <input v-model="filters.price_min" type="number" placeholder="💰 Мін. ціна"
          class="input" />
        <input v-model="filters.price_max" type="number" placeholder="💸 Макс. ціна"
          class="input" />

        <select v-model="filters.rooms" class="input">
          <option value="">🛏️ Кімнати</option>
          <option v-for="n in 5" :key="n" :value="n">{{ n }}</option>
        </select>

        <select v-model="filters.available" class="input">
          <option value="">📦 Доступність</option>
          <option :value="true">✅ Доступні</option>
          <option :value="false">❌ Недоступні</option>
        </select>

        <button
          type="submit"
          class="bg-blue-600 text-white font-semibold rounded-lg py-2 px-4 col-span-full md:col-span-1 hover:bg-blue-700 transition"
        >
          🔍 Застосувати
        </button>
      </form>

      <!-- Список квартир -->
      <div v-if="apartments.length === 0" class="text-gray-800 text-center py-6">
        Квартир не знайдено.
      </div>

      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="apartment in apartments"
          :key="apartment.slug"
          class="p-5 bg-white bg-opacity-80 rounded-xl shadow hover:shadow-lg transition duration-300 relative"
          :class="{ 'opacity-50 grayscale blur-sm': apartment.availability === false }"
        >
          <router-link
            :to="`/apartments/${apartment.slug}`"
            class="block text-xl font-bold text-blue-700 hover:underline mb-2"
          >
            {{ apartment.name }}
          </router-link>
          <p class="text-gray-700 line-clamp-3 mb-3">{{ apartment.description }}</p>
          <p class="text-green-700 font-semibold">{{ apartment.price }} грн</p>
          <p class="text-sm text-gray-600">{{ apartment.number_of_rooms }} кімнат</p>

          <span
            class="absolute top-3 right-3 text-xs px-2 py-1 rounded-full"
            :class="apartment.availability ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'">
            {{ apartment.availability ? 'Доступна' : 'Недоступна' }}
          </span>
        </div>
      </div>

      <!-- Пагінация -->
      <div class="mt-8 flex justify-center gap-4">
        <button
          @click="page--"
          :disabled="page === 1"
          class="btn"
          :class="{ 'opacity-50 cursor-not-allowed': page === 1 }"
        >
          ⬅️ Попередня
        </button>
        <button @click="page++" class="btn">Наступна ➡️</button>
      </div>

    </div>
</template>


<style scoped>
.input {
  @apply w-full px-3 py-2 border border-gray-300 rounded;
}
.btn {
  @apply px-4 py-2 bg-gray-200 rounded hover:bg-gray-300;
}
</style>

<script setup>
import { ref, watch } from 'vue'
import api from '../services/api' // путь поправь, если другой

const apartments = ref([])
const page = ref(1)
const filters = ref({
  search: '',
  price_min: '',
  price_max: '',
  rooms: '',
  available: ''
})

async function fetchApartments() {
  const params = {
    page: page.value,
    search: filters.value.search,
    price_min: filters.value.price_min,
    price_max: filters.value.price_max,
    rooms: filters.value.rooms,
    available: filters.value.available,
  }

  try {
    const response = await api.get('/api/v1/apartments/', { params })
    apartments.value = response.data
  } catch (error) {
    console.error('Помилка при завантаженні квартир:', error)
  }
}

// Перезагрузка при изменении страницы
watch(page, fetchApartments)

// Начальная загрузка
fetchApartments()

</script>
