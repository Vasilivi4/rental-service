<template>
  <div class="p-4 bg-white rounded-xl shadow flex flex-wrap gap-4 items-end">
    <div>
      <label class="block text-sm font-medium">Пошук</label>
      <input v-model="filters.search" type="text" class="input" placeholder="Назва або опис" />
    </div>

    <div>
      <label class="block text-sm font-medium">Мін. ціна</label>
      <input v-model.number="filters.price_min" type="number" class="input" />
    </div>

    <div>
      <label class="block text-sm font-medium">Макс. ціна</label>
      <input v-model.number="filters.price_max" type="number" class="input" />
    </div>

    <div>
      <label class="block text-sm font-medium">Кімнати</label>
      <input v-model.number="filters.rooms" type="number" class="input" />
    </div>

    <div>
      <label class="block text-sm font-medium">Доступність</label>
      <select v-model="filters.available" class="input">
        <option value="">Усі</option>
        <option value="true">Доступні</option>
        <option value="false">Недоступні</option>
      </select>
    </div>

    <div class="flex gap-2">
      <button @click="$emit('apply', filters)" class="btn-primary">Застосувати</button>
      <button @click="reset" class="btn-secondary">Скинути</button>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue';

const props = defineProps({ modelValue: Object });
const emit = defineEmits(['apply']);

const filters = reactive({ ...props.modelValue });

const reset = () => {
  Object.assign(filters, {
    search: '',
    price_min: '',
    price_max: '',
    rooms: '',
    available: '',
  });
  emit('apply', filters);
};
</script>

<style scoped>
.input {
  @apply border border-gray-300 rounded p-2 w-40;
}
.btn-primary {
  @apply bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700;
}
.btn-secondary {
  @apply bg-gray-200 text-black px-4 py-2 rounded hover:bg-gray-300;
}
</style>
