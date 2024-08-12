<script setup>
import { ref } from 'vue'

// ref returns a object, this object contains a single property: value
const msg = ref('Hello')

</script>

<template>
  <h3>
    ref: {{msg}}
  </h3>
</template>