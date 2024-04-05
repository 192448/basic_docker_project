<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div>
      <nav>
        <RouterLink to="/">Home</RouterLink>
      </nav>
      <nav>
        <RouterLink to="/about">Package Statistics</RouterLink>
      </nav>
    </div>
  </header>
  <RouterView />
</template>
