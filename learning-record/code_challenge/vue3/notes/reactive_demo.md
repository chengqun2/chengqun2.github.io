<script setup>
import { reactive } from 'vue'

const messager = reactive({
  message: 'Hello, this is a dynamic message!',
  count: 0
})

const increment = () => {
  messager.count++
}

</script>

<template>
  <h1>{{messager.message}}</h1>
  <h2>
    {{messager.message.split('').reverse().join('')}}
  </h2>
  <input v-model="messager.message" />  <br />
  <button @click="increment()">
    {{messager.count}}
  </button>
</template>