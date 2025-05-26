<template>

  <div class="font">
    <div class="bg-white/70 p-4 rounded-lg shadow-inner">
      <div v-if="apartment">
        <h1 class="text-2xl font-bold">{{ apartment.name }}</h1>
        <p>{{ apartment.description }}</p>
        <p>Ціна: {{ apartment.price }}</p>
        <p>Кімнат: {{ apartment.number_of_rooms }}</p>
        <p>Площа: {{ apartment.square }} м²</p>
        <p>Доступність: {{ apartment.available ? 'Так' : 'Ні' }}</p>
      </div>
      <div v-else>
        <p>Квартиру не знайдено.</p>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import api from '../services/api';

const apartment = ref(null);
const route = useRoute();

onMounted(async () => {
  const { data } = await api.get(`/api/v1/apartments/${route.params.slug}/`);
  apartment.value = data;
});
</script>
