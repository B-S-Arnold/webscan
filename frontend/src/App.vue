<template>
  <div id="app">
    <img class="logo" alt="WebScan logo" src="./assets/logo.png">
    <SplashPage msg="Welcome to WebScan" />
  </div>
</template>

<script>
import SplashPage from './components/SplashPage.vue'

export default {
  name: 'App',
  components: {
    SplashPage
  }
}
</script>

<style scoped src="./App.css"></style>