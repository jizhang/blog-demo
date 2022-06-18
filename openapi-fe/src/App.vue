<script setup lang="ts">
import 'bootstrap/dist/css/bootstrap.min.css'
import { onMounted, ref } from 'vue'
import dayjs from 'dayjs'
import { postApi } from './api'
import type { Post } from './openapi'

const posts = ref<Post[]>([])

onMounted(() => {
  postApi.getPostList().then((response) => {
    if (response.posts) {
      posts.value = response.posts
    }
  })
})

function formatDate(date?: Date) {
  if (!date) return '-'
  return dayjs(date).format('YYYY-MM-DD HH:mm:ss')
}
</script>

<template>
  <div class="container my-3">
    <div class="row">
      <div class="col-auto">
        <label class="col-form-label">Sort:</label>
      </div>
      <div class="col-auto me-auto">
        <select class="form-select">
          <option value="desc" selected>Descending</option>
          <option value="asc">Ascending</option>
        </select>
      </div>

      <div class="col-auto">
        <button type="button" class="btn btn-primary">New Post</button>
      </div>
    </div>

    <div class="d-grid gap-3 my-3">
      <div class="card" v-for="post in posts" :key="post.id">
        <div class="card-body">
          <h5 class="card-title">{{post.title}}</h5>
          <p class="card-text">{{post.content}}</p>
          <p class="card-text"><small class="text-muted">Updated at {{formatDate(post.updatedAt)}}</small></p>
        </div>
      </div>
    </div>

    <div class="d-flex justify-content-end">
      <nav>
        <ul class="pagination">
          <li class="page-item"><a class="page-link" href="#">Previous</a></li>
          <li class="page-item"><a class="page-link" href="#">1</a></li>
          <li class="page-item"><a class="page-link" href="#">2</a></li>
          <li class="page-item"><a class="page-link" href="#">3</a></li>
          <li class="page-item"><a class="page-link" href="#">Next</a></li>
        </ul>
      </nav>
    </div>
  </div>
</template>
