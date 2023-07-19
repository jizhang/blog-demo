<template>
  <div class="page-table-list">
    <b-table :fields="fields" :items="tableList">
      <template slot="category" slot-scope="data">
        {{getCategoryName(data.item.category)}}
      </template>
      <template slot="columns" slot-scope="data">
        {{data.item.columns.length}}
      </template>
      <template slot="operation" slot-scope="data">
        <b-dropdown text="Edit" size="sm" variant="primary">
          <b-dropdown-item :to="{ path: '/non-strict', query: { id: data.item.id } }">Non Strict</b-dropdown-item>
          <b-dropdown-item :to="{ path: '/local-copy', query: { id: data.item.id } }">Local Copy</b-dropdown-item>
          <b-dropdown-item :to="{ path: '/explicit-update', query: { id: data.item.id } }">Explicit Update</b-dropdown-item>
          <b-dropdown-item :to="{ path: '/computed-property', query: { id: data.item.id } }">Computed Property</b-dropdown-item>
          <b-dropdown-item :to="{ path: '/map-fields', query: { id: data.item.id } }">Map Fields</b-dropdown-item>
        </b-dropdown>
        <b-button variant="danger" size="sm" @click="handleDeleteTable(data.item)">Delete</b-button>
      </template>
    </b-table>
  </div>
</template>

<script>
import _ from 'lodash'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'TableList',
  computed: {
    ...mapState('table', [
      'tableList',
      'categoryOptions',
    ]),
  },

  data () {
    return {
      fields: [
        { key: 'id', label: 'ID' },
        { key: 'table_name', label: 'Table Name' },
        { key: 'category', label: 'Category' },
        { key: 'columns', label: 'Column Count' },
        { key: 'operation', label: 'Operation' },
      ]
    }
  },

  methods: {
    ...mapActions('table', [
      'deleteTable',
    ]),

    handleDeleteTable (table) {
      if (window.confirm('Are you sure?')) {
        this.deleteTable(table.id)
      }
    },

    getCategoryName (value) {
      let option = _.find(this.categoryOptions, ['value', value])
      return _.get(option, 'text', '-')
    },
  }
}
</script>

<style scoped>
.page-table-list {
  padding: 30px;
}
</style>
