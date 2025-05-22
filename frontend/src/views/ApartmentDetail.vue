<template>
  <div class="p-4">
    <div v-if="loading">Loading...</div>
    <div v-else>
      <h1 class="text-2xl font-bold">{{ apartment.name }}</h1>
      <p>{{ apartment.description }}</p>
      <p>Price: {{ apartment.price }}</p>
      <p>Rooms: {{ apartment.number_of_rooms }}</p>
      <p>Square: {{ apartment.square }}</p>
      <p>Status: <span :class="apartment.availability ? 'text-green-500' : 'text-red-500'">
        {{ apartment.availability ? 'Available' : 'Not Available' }}</span></p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import api from '@/api'

const route = useRoute()
const apartment = ref({})
const loading = ref(true)

onMounted(async () => {
  const res = await api.get(`/api/v1/apartments/${route.params.id}/`)
  apartment.value = res.data
  loading.value = false
})
</script>