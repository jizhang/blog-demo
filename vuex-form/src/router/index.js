import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import TableList from '@/components/TableList'
import NonStrict from '@/components/NonStrict'
import LocalCopy from '@/components/LocalCopy'
import ExplictUpdate from '@/components/ExplicitUpdate'
import ComputedProperty from '@/components/ComputedProperty'
import MapFields from '@/components/MapFields'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/table-list',
      name: 'TableList',
      component: TableList,
    },
    {
      path: '/non-strict',
      name: 'NonStrict',
      component: NonStrict
    },
    {
      path: '/local-copy',
      name: 'LocalCopy',
      component: LocalCopy
    },
    {
      path: '/explicit-update',
      name: 'ExplictUpdate',
      component: ExplictUpdate
    },
    {
      path: '/computed-property',
      name: 'ComputedProperty',
      component: ComputedProperty
    },
    {
      path: '/map-fields',
      name: 'MapFields',
      component: MapFields
    }
  ]
})
