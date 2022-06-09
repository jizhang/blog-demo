import { createApp } from 'vue'

const makeToast = (props: any) => {
  return <b>{ props.message }</b>
}

export default (message: string) => {
  const div = document.createElement('div')
  document.querySelector('#app')?.appendChild(div)
  createApp(makeToast, { message }).mount(div)
}

// TODO destroy
