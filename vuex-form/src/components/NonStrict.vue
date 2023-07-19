<template>
  <div class="page-non-script">
    <b-form @submit="handleSubmit">
      <b-row>
        <b-col cols="6">
          <b-form-group label="Table Name:">
            <b-form-input v-model="table.table_name" />
          </b-form-group>
        </b-col>
      </b-row>
      <b-row>
        <b-col cols="6">
          <b-form-group label="Category:">
            <b-form-select v-model="table.category">
              <option :value="0">Choose</option>
              <option v-for="option in categoryOptions" :key="option.value"
                :value="option.value" v-text="option.text" />
            </b-form-select>
          </b-form-group>
        </b-col>
        <b-col cols="6">
          <b-button variant="light" @click="handleAddCategory" style="margin-top: 31px;">
            <font-awesome-icon icon="plus" style="margin-right: 12px;" />Add Category
          </b-button>
        </b-col>
      </b-row>
      <b-row>
        <b-col cols="6">
          <table class="table table-sm" style="margin-top: 10px;">
            <tr>
              <th width="40%">Column Name</th>
              <th width="40%">Data Type</th>
              <th>Operation</th>
            </tr>
            <tr v-for="(column, index) in table.columns" :key="index">
              <td>
                <b-form-input v-model="column.column_name" size="sm" />
              </td>
              <td>
                <b-form-select v-model="column.data_type" size="sm">
                  <option value="">Choose</option>
                  <option v-for="option in dataTypeOptions" :key="option"
                    :value="option" v-text="option" />
                </b-form-select>
              </td>
              <td>
                <b-button size="sm" variant="light" @click="handleRemoveColumn(index)">
                  <font-awesome-icon icon="trash" style="margin-right:8px;" />Remove
                </b-button>
              </td>
            </tr>
          </table>
        </b-col>
      </b-row>
      <b-row>
        <b-col cols="12">
          <b-button variant="light" @click="handleAddColumn" style="margin-bottom: 20px;">
            <font-awesome-icon icon="plus" style="margin-right: 12px;" />Add Column
          </b-button>
        </b-col>
      </b-row>
      <b-row>
        <b-col cols="12">
          <b-button type="submit" variant="primary">Submit</b-button>
        </b-col>
      </b-row>
    </b-form>

    <b-modal v-model="addCategoryDialog" title="Add Category" @ok="handleSaveCategory"
      no-close-on-esc no-close-on-backdrop>
      <b-form>
        <b-form-group label="Category Name:">
          <b-form-input v-model="categoryName" :state="categoryNameState" />
          <b-form-invalid-feedback v-text="categoryNameError" />
        </b-form-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import _ from 'lodash'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'NonStrict',
  data () {
    return {
      addCategoryDialog: false,
      categoryName: '',
      categoryNameState: null,
      categoryNameError: ''
    }
  },

  mounted () {
    let id = _.get(this.$route.query, 'id')
    if (id > 0) {
      this.getTable(id)
    }
  },

  beforeDestroy () {
    this.resetTable()
  },

  computed: {
    ...mapState('table', [
      'table',
      'categoryOptions',
      'dataTypeOptions',
    ])
  },

  methods: {
    ...mapActions('table', [
      'addCategory',
      'saveTable',
      'resetTable',
      'getTable',
    ]),

    handleAddCategory () {
      this.categoryName = ''
      this.categoryNameState = null
      this.addCategoryDialog = true
    },

    handleSaveCategory (event) {
      if (!this.categoryName) {
        this.categoryNameState = false
        this.categoryNameError = 'category name cannot be empty'
      } else if (_.some(this.categoryOptions, ['text', this.categoryName])) {
        this.categoryNameState = false
        this.categoryNameError = 'category name already exists'
      } else {
        this.categoryNameState = true
      }

      if (!this.categoryNameState) {
        event.preventDefault()
      } else {
        this.addCategory(this.categoryName)
      }
    },

    handleAddColumn () {
      this.table.columns.push({
        column_name: '',
        data_type: '',
      })
    },

    handleRemoveColumn (index) {
      this.table.columns.splice(index, 1)
    },

    handleSubmit (event) {
      event.preventDefault()
      this.saveTable(this.table)
      this.$router.push('/table-list')
    },
  }
}
</script>

<style scoped>
.page-non-script {
  padding: 30px;
}
</style>
