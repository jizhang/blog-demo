import { createApp, VNodeRef } from 'vue'
import { Toast } from 'bootstrap'

function makeToast(props: { message: string }) {
  const saveRef: VNodeRef = (el) => {
    if (el instanceof HTMLElement) {
      new Toast(el).show()
    }
  }

  return (
    <div class="toast position-fixed top-0 start-50 translate-middle-x mt-3" ref={saveRef}>
      <div class="d-flex">
        <div class="toast-body">
          {props.message}
        </div>
        <button type="button" class="btn-close m-auto me-3" data-bs-dismiss="toast"></button>
      </div>
    </div>
  )
}

export default (message: string) => {
  const div = document.createElement('div')
  document.body.appendChild(div)
  const vm = createApp(makeToast, { message })
  vm.mount(div)

  div.addEventListener('hidden.bs.toast', () => {
    vm.unmount()
    div.remove()
  })
}
