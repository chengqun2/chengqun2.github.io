<script setup>
import { ref, reactive } from 'vue'
  
const msg = ref('Hello')
  
const messager = reactive({
  message: 'Hello, this is a dynamic message!',
  count: 0
})

const increment = () => {
  messager.count++
}

</script>

<template>
  <h3>
    ref: {{msg}}
  </h3>
  <h1>{{messager.message}}</h1>
  <h2>
    {{messager.message.split('').reverse().join('')}}
  </h2>
  <input v-model="messager.message" />  <br />
  <button @click="increment()">
    {{messager.count}}
  </button>
</template>