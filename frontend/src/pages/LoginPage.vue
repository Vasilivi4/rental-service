<template>
  <div class="p-4 max-w-md mx-auto">
    <form @submit.prevent="submit">
      <input v-model="email" type="email" placeholder="Email" class="border p-2 block w-full mb-2" />
      <input v-model="password" type="password" placeholder="Пароль" class="border p-2 block w-full mb-2" />
      <button class="bg-blue-600 text-white p-2 w-full">Увійти</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { auth } from '../store/auth';
import { useRouter } from 'vue-router';

const email = ref('');
const password = ref('');
const router = useRouter();

async function submit() {
  try {
    await auth.login(email.value, password.value);
    router.push('/');
  } catch (e) {
    alert('Невірні дані');
  }
}
</script>
