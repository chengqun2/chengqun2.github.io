<script setup>
import { ref } from 'vue'


</script>
<template>
  <el-dropdown split-button type="primary">
    Default
  <template #dropdown>
    <el-dropdown-menu>
      <el-dropdown-item>Action 1</el-dropdown-item>
      <el-dropdown-item>Action 2</el-dropdown-item>
      <el-dropdown-item>Action 3</el-dropdown-item>
      <el-dropdown-item>Action 4</el-dropdown-item>
    </el-dropdown-menu>
  </template>
  </el-dropdown>
</template>
<style scoped>
:deep(.el-dropdown-menu__item:hover:not(.is-disabled)) {
  background-color: red; /* Replace with your desired color */
  color: #ffffff; /* Optional: change text color on hover */
}
</style>


<style scoped>
.read-the-docs {
  color: #888;
}
</style>
