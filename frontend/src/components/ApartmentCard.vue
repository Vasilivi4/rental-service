<template>
  <router-link :to="`/apartments/${apartment.id}`">
    <div :class="['border p-4 rounded shadow', !apartment.available && 'opacity-50 blur-sm']">
      <h2 class="text-lg font-bold">{{ apartment.name }}</h2>
      <p>{{ apartment.price }} грн / міс</p>
      <p>{{ apartment.number_of_rooms }} кімнат(и)</p>
    </div>
  </router-link>
</template>

<script setup>
defineProps(['apartment']);
</script>
