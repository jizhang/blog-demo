<script setup lang="ts">
import 'bootstrap/dist/css/bootstrap.min.css'
import { postApi } from './api'

postApi.getPostList().then((response) => {
  console.log(response)
})
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
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
      </div>

      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
      </div>

      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
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
