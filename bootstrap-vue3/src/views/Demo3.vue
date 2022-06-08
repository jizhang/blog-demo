<script setup lang="ts">
import { ref } from 'vue'
import Modal from '../components/Modal.vue'

const dialogVisible = ref(false)

function launchDemoModal() {
  dialogVisible.value = true
}

function closeModal() {
  dialogVisible.value = false
}

function saveChanges() {
  alert('Changes saved.') // TODO Notification
  closeModal()
}
</script>

<template>
  <button type="button" class="btn btn-primary" @click="launchDemoModal">
    Launch demo modal 3
  </button>

  <Modal v-model="dialogVisible" title="Modal title">
    Woo-hoo, you're reading this text in a modal!
    <template #footer>
      <button type="button" class="btn btn-secondary" @click="closeModal">Close</button>
      <button type="button" class="btn btn-primary" @click="saveChanges">Save changes</button>
    </template>
  </Modal>
</template>
