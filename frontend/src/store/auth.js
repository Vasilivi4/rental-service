import { reactive } from 'vue';
import api from '../services/api';

export const auth = reactive({
  token: localStorage.getItem('token') || '',
  async login(email, password) {
    const res = await api.post('/api/v1/token/', {
      email,
      password
    });
    this.token = res.data.access;
    localStorage.setItem('token', this.token);
  },
  logout() {
    this.token = '';
    localStorage.removeItem('token');
  }
});
