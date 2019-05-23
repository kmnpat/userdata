<template>
  <div id="showdata">
    <link href='https://fonts.googleapis.com/css?family=Kanit:400,300&subset=thai,latin' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.2.0/css/all.css" integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ" crossorigin="anonymous">

    <h1>User Data</h1>
    <div v-for="(b, index) in blog" :key="index" class="single-blog">
      <article>id: {{b.identify}}</article>
      <article>first name: {{b.first_name}}</article>
      <article>last name: {{b.last_name}}</article>
      <article>email: {{b.email}}</article>
      <article>gender: {{b.gender}}</article>
      <article>age: {{b.age}}</article>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      blog: [],
    };
  },
  created() {
    this.$http.get("http://127.0.0.1:5000/users").then(function(user) {
      console.log(user);
      this.blog = user.body.data;
    })
    .catch(function(error) {
          self.loadComplete = true;
          console.log("Error: ", error);
        });
  }
}

</script>

<style>
#showdata {
  max-width: 800px;
  margin: 0 auto;
  font-family: 'Kanit', sans-serif;
}
.single-blog{
  padding: 20px;
  margin: 20px 0;
  box-sizing: border-box;
  background: darkgrey;
  font-family: 'Kanit', sans-serif;
}

</style>
