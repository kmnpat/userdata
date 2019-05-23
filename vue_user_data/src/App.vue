<template>
  <div>
    <helloworld></helloworld>

  </div>
</template>

<script>
import HelloWorld from "./components/ShowAll.vue";


export default {
  data() {
    return {
      active: 1
    };
  },
  components: {
    "helloworld": HelloWorld,


  }
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
