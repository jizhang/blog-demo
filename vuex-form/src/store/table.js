import _ from 'lodash'
import { getField, updateField } from 'vuex-map-fields'

const types = {
  ADD_CATEGORY: 'addCategory',
  DELETE_TABLE: 'deleteTable',
  ADD_TABLE: 'addTable',
  UPDATE_TABLE: 'updateTable',
  UPDATE_TABLE_FORM: 'updateTableForm',
  RESET_TABLE: 'resetTable',
  ADD_COLUMN: 'addColumn',
  DELETE_COLUMN: 'deleteColumn',
  UPDATE_COLUMN: 'updateColumn',
}

const getDefaultTable = () => {
  return {
    id: null,
    table_name: '',
    category: 0,
    columns: [],
  }
}

export default {
  namespaced: true,
  state: {
    tableList: [],
    table: getDefaultTable(),
    categoryOptions: [
      { value: 1, text: 'Sales' },
      { value: 2, text: 'Marketing' }
    ],
    dataTypeOptions: ['int', 'varchar', 'datetime']
  },

  getters: {
    getField,
  },

  mutations: {
    updateField,

    myUpdateField (state, payload) {
      const { path, value } = payload
      _.set(state, path, value)
    },

    setTable (state, payload) {
      state.table = payload
      // _.assign(state.table, payload)
      // state.table = _.cloneDeep(payload)
    },

    [types.ADD_CATEGORY] (state, payload) {
      let maxId = _(state.categoryOptions).map('value').max()
      state.categoryOptions.push({
        value: maxId + 1,
        text: payload
      })
    },

    [types.DELETE_TABLE] (state, payload) {
      let index = _.findIndex(state.tableList, ['id', payload])
      if (index !== -1) {
        state.tableList.splice(index, 1)
      }
    },

    [types.ADD_TABLE] (state, payload) {
      let maxId = _(state.tableList).map('id').max()
      payload.id = _.isUndefined(maxId) ? 1 : (maxId + 1)
      state.tableList = _(state.tableList)
        .concat(payload)
        .orderBy(['table_name'])
        .value()
    },

    [types.UPDATE_TABLE] (state, payload) {
      let table = _.find(state.tableList, ['id', payload.id])
      _.assign(table, payload)
    },

    [types.RESET_TABLE] (state, payload) {
      _.assign(state.table, getDefaultTable())
    },

    [types.UPDATE_TABLE_FORM] (state, payload) {
      _.assign(state.table, payload)
    },

    [types.ADD_COLUMN] (state, payload) {
      state.table.columns.push(payload)
    },

    [types.DELETE_COLUMN] (state, payload) {
      state.table.columns.splice(payload, 1)
    },

    [types.UPDATE_COLUMN] (state, payload) {
      const { index, column } = payload
      _.assign(state.table.columns[index], column)
    },
  },

  actions: {
    addCategory ({ commit }, payload) {
      commit(types.ADD_CATEGORY, payload)
    },

    deleteTable ({ commit }, payload) {
      commit(types.DELETE_TABLE, payload)
    },

    saveTable ({ commit, state }, payload) {
      let table = _.cloneDeep(payload)
      if (table.id > 0) {
        let exists = _.some(state.tableList, ['id', payload.id])
        if (exists) {
          commit(types.UPDATE_TABLE, table)
        }
      } else {
        commit(types.ADD_TABLE, table)
      }
    },

    resetTable ({ commit }) {
      commit(types.RESET_TABLE)
    },

    getTable ({ commit, state }, payload) {
      let table = _.find(state.tableList, ['id', payload])
      if (!_.isUndefined(table)) {
        commit(types.UPDATE_TABLE_FORM, _.cloneDeep(table))
      }
    },

    updateTableForm ({ commit }, payload) {
      commit(types.UPDATE_TABLE_FORM, payload)
    },

    addColumn ({ commit }, payload) {
      let column = _.assign({
        column_name: '',
        data_type: '',
      }, payload)
      commit(types.ADD_COLUMN, column)
    },

    deleteColumn ({ commit }, payload) {
      commit(types.DELETE_COLUMN, payload)
    },

    updateColumn ({ commit }, payload) {
      commit(types.UPDATE_COLUMN, payload)
    },
  }
}
