<script setup>
import { ref } from 'vue'

defineProps({
  msg: String,
})

const count = ref(0)
console.log(`count: ${count.value}`)
const increment = () => {
  count.value++
}
import { reactive, toRefs } from 'vue'

const state = reactive({
  foo: 1,
  bar: 2
})

const { foo, bar } = toRefs(state)

// Both state.foo and foo.value will be synced
foo.value++
console.log(state.foo) // 2
state.foo++
console.log(foo.value) // 3

</script>

<template>
  <div>
    <h1>{{ msg }}</h1>

    <div class="card">
      <button type="button" @click="increment">count is {{ count }}</button>
      <p>
        foo: {{ foo }}
      </p>
    </div>

  </div>
  
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
