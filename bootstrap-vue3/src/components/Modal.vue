<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { Modal } from 'bootstrap'

const props = defineProps<{
  modelValue: boolean
  title: string
}>()

const emit = defineEmits<{
  (e: 'update:modelValue', modelValue: boolean): void
}>()

const modalRef = ref<HTMLElement | null>(null)
let modal: Modal
onMounted(() => {
  if (modalRef.value) {
    modal = new Modal(modalRef.value)
  }
})

watch(() => props.modelValue, (modelValue) => {
  if (modelValue) {
    modal.show()
  } else {
    modal.hide()
  }
})

function close() {
  emit('update:modelValue', false)
}
</script>

<template>
  <div class="modal fade" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" ref="modalRef">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">{{ title }}</h5>
          <button type="button" class="btn-close" aria-label="Close" @click="close"></button>
        </div>
        <div class="modal-body">
          <slot />
        </div>
        <div class="modal-footer">
          <slot name="footer" />
        </div>
      </div>
    </div>
  </div>
</template>
