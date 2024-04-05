<script>
  export default{
    mounted(){
      this.list()
    },
    methods : {
      list(){
        fetch('http://127.0.0.1:9000/statistics', {method : 'GET', headers: { 'Access-Control-Allow-Origin': '*'}})
        .then((response) => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json(); 
        })
        .then((response) => {
          this.package_list = response;
        });
        console.log(this.package_list);
      },
    }
  }
</script>

<template>
  <main>
    <h1>Statistics</h1>
    <div>
    </div>
  </main>
</template>
