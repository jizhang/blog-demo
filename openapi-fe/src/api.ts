import { Configuration, PostApi } from './openapi'

const conf = new Configuration({
  basePath: '',
})

export const postApi = new PostApi(conf)
