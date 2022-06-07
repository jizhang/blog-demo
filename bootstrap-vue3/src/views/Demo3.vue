<script setup lang="ts">
import { ref } from 'vue'
import Modal from '../components/Modal.vue'

const dialogVisible = ref(false)

function launchDemoModal() {
  dialogVisible.value = true
}
</script>

<template>
  <button type="button" class="btn btn-primary" @click="launchDemoModal">
    Launch demo modal 3
  </button>

  <Modal v-model="dialogVisible" />
</template>
