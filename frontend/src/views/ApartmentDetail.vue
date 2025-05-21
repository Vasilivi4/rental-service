<template>
  <div class="p-4 max-w-4xl mx-auto">
    <div v-if="loading" class="text-center text-gray-500">Loading...</div>
    <div v-else-if="apartment" class="space-y-4">
      <h1 class="text-2xl font-bold">{{ apartment.name }}</h1>
      <div class="text-gray-600">{{ apartment.description }}</div>
      <div class="grid grid-cols-2 gap-4">
        <div><strong>Ціна:</strong> {{ apartment.price }} грн</div>
        <div><strong>Кількість кімнат:</strong> {{ apartment.number_of_rooms }}</div>
        <div><strong>Площа:</strong> {{ apartment.square }} м²</div>
        <div><strong>Доступність:</strong> <span :class="apartment.availability ? 'text-green-600' : 'text-red-500'">{{ apartment.availability ? 'Доступна' : 'Недоступна' }}</span></div>
        <div><strong>Власник:</strong> {{ apartment.owner }}</div>
        <div><strong>Slug:</strong> {{ apartment.slug }}</div>
      </div>
    </div>
    <div v-else class="text-red-500">Квартиру не знайдено</div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import axios from '@/lib/axios'

const apartment = ref(null)
const loading = ref(true)
const route = useRoute()

onMounted(async () => {
  try {
    const res = await axios.get(`/apartments/${route.params.id}/`)
    apartment.value = res.data
  } catch (err) {
    console.error(err)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
</style>