<script>
  export default{
    mounted(){
      this.list()
    },
    data(){
      return {
        id : 0,
        status : "",
        package_list : [],
        created_package : [],
        updated_package : [],
      }
    },
    methods : {
      list(){
        fetch('http://127.0.0.1:5000/packages', {method : 'GET', headers: { 'Access-Control-Allow-Origin': '*'}})
        .then((response) => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json(); 
        })
        .then((response) => {
          this.package_list = response;
        });
      },
      create(){
        fetch('http://127.0.0.1:5000/package', {method : 'POST', headers: { 'Access-Control-Allow-Origin': '*'}})
        .then((response) => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json(); 
        })
        .then((response) => {
          this.created_package = response;
        });
        window.location.reload;
      },
      update(){
        fetch('http://127.0.0.1:5000/package', {method : 'PUT', headers: { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json'}, body : JSON.stringify({'id' : this.id, 'status' : this.status})})
        .then((response) => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json(); 
        })
        .then((response) => {
          this.updated_package = response;
          console.log(this.updated_package);
        });
        window.location.reload;
      },
    }
  }
</script>

<template>
  <main>
    <h1>Packages</h1>
    <div>
      <div v-for="it in package_list">
        <p>ID: {{ it.id }}</p>
        <p>Status: {{ it.status }}</p>
      </div>
    </div>

    <h1>Create Package</h1>
    <div>
      <div v-for="it in created_package">
        <p>ID: {{ it.id }}</p>
        <p>Status: {{ it.status }}</p>
      </div>
    </div>
    <button @click="create()">Create</button>

    <h1>Update Package</h1>
    <form>
        <label for="id">ID:</label><br>
        <input type="number" v-model="id" name="id"><br><br>
        <label for="status">Status:</label><br>
        <input type="text" v-model="status" name="status"><br><br>
    </form>
    <button @click="update()">Update</button>
    <h4>Updated Package</h4>
    <div>
      <div v-for="it in updated_package">
        <p>ID: {{ it.id }}</p>
        <p>Status: {{ it.status }}</p>
      </div>
    </div>

  </main>
</template>