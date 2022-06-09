import { createApp, ref, onMounted, defineComponent } from 'vue'
import { Toast } from 'bootstrap'

const MyToast = defineComponent({
  props: {
    message: String,
  },

  setup(props) {
    const toastRef = ref<HTMLElement | null>(null)
    onMounted(() => {
      if (toastRef.value) {
        new Toast(toastRef.value).show()
      }
    })

    return () => (
      <div class="toast position-fixed top-0 start-50 translate-middle-x mt-3" ref={toastRef}>
        <div class="d-flex">
          <div class="toast-body">
            {props.message}
          </div>
          <button type="button" class="btn-close m-auto me-3" data-bs-dismiss="toast"></button>
        </div>
      </div>
    )
  },
})

export default (message: string) => {
  const div = document.createElement('div')
  document.body.appendChild(div)
  createApp(MyToast, { message }).mount(div)
}

// TODO destroy
