<script setup>
import HelloWorld from './components/HelloWorld.vue'
import ElSelectDemo from './components/El-select-demo.vue'
import { reactive, ref, toRefs } from 'vue'
const msgStr = ref('')
msgStr.value = 'Hello, this is a message from parent.'

const man = reactive({
  'name': 'Ernest',
  'age': 30
})

const woman = reactive({
  'name': 'Jenny',
  'age': 29
})
const { name, age } = toRefs(woman)

const departureDate = ref(dateToString(new Date()))
const returnDate = ref(departureDate.value)
function dateToString(date) {
  return (
    date.getFullYear() +
    '-' +
    pad(date.getMonth() + 1) +
    '-' +
    pad(date.getDate())
  )
}
function pad(n, s = String(n)) {
  return s.length < 2 ? `0${s}` : s
}
</script>

<template>
  <div>
    <HelloWorld :msg='msgStr' />
    <div>Man: {{ man.name }}, {{man.age}}</div>
    <div>Woman: {{ name }}, {{age}}</div>
    <div>
      departureDate: <input type="date" v-model="departureDate" />
      returnDate: <input type="date" v-model="returnDate" />
    </div>
    <ElSelectDemo />
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
