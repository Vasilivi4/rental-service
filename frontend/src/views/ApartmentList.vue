<template>
  <div class="p-4">
    <div class="flex gap-4 mb-4">
      <input v-model="filters.search" class="input" placeholder="Search..." />
      <input v-model.number="filters.price" class="input" type="number" placeholder="Max Price" />
      <input v-model.number="filters.rooms" class="input" type="number" placeholder="Rooms" />
      <label><input type="checkbox" v-model="filters.available" /> Available</label>
    </div>

    <div v-if="loading">Loading...</div>
    <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <router-link
        v-for="apt in apartments"
        :key="apt.id"
        :to="`/apartments/${apt.id}`"
        class="p-4 border rounded shadow hover:shadow-lg transition"
        :class="{ 'opacity-50 blur-sm': !apt.availability }"
      >
        <h2 class="text-xl font-bold">{{ apt.name }}</h2>
        <p>{{ apt.description }}</p>
        <p>
          <strong>Price:</strong> {{ apt.price }} | <strong>Rooms:</strong> {{ apt.number_of_rooms }}
        </p>
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import api from '@/api'

const apartments = ref([])
const loading = ref(true)
const filters = ref({ search: '', price: null, rooms: null, available: false })

const fetchData = async () => {
  loading.value = true
  const params = {}
  if (filters.value.search) params.search = filters.value.search
  if (filters.value.price) params.price_max = filters.value.price
  if (filters.value.rooms) params.rooms = filters.value.rooms
  if (filters.value.available) params.available = true
  const res = await api.get('/api/v1/apartments/', { params })
  apartments.value = res.data.results
  loading.value = false
}

onMounted(fetchData)
watch(filters, fetchData, { deep: true })
</script>