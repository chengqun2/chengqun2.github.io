<script setup>
import HelloWorld from './components/HelloWorld.vue'
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


</script>

<template>
  <div>
    <HelloWorld :msg='msgStr' />
    <div>Man: {{ man.name }}, {{man.age}}</div>
    <div>Woman: {{ name }}, {{age}}</div>
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
