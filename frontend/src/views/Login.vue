<template>
  <div class="max-w-md mx-auto p-4">
    <form @submit.prevent="login">
      <input v-model="email" class="input w-full mb-2" type="email" placeholder="Email" required />
      <input v-model="password" class="input w-full mb-2" type="password" placeholder="Password" required />
      <button class="btn w-full bg-blue-500 text-white">Login</button>
      <p v-if="error" class="text-red-500 mt-2">{{ error }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import api from '@/api'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()

const login = async () => {
  try {
    const res = await api.post('/api/token/', { email: email.value, password: password.value })
    localStorage.setItem('token', res.data.access)
    router.push('/')
  } catch (err) {
    error.value = 'Invalid credentials'
  }
}
</script>
