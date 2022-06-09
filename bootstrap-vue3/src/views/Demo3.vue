<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { Toast } from 'bootstrap'
import Modal from '../components/Modal.vue'
import MyToast from '../components/Toast'

const toastRef = ref<HTMLElement | null>(null)
let toast: Toast
onMounted(() => {
  if (toastRef.value) {
    toast = new Toast(toastRef.value)
  }
})

const dialogVisible = ref(false)

function launchDemoModal() {
  dialogVisible.value = true
}

function closeModal() {
  dialogVisible.value = false
}

function saveChanges() {
  closeModal()
  toast.show()
}

MyToast('hello world1')
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

  <div class="toast position-fixed top-0 start-50 translate-middle-x mt-3" ref="toastRef">
    <div class="d-flex">
      <div class="toast-body">
        Changes saved.
      </div>
      <button type="button" class="btn-close m-auto me-3" data-bs-dismiss="toast"></button>
    </div>
  </div>
</template>
