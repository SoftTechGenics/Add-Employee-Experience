<template>
  <NavBar/>
  <router-view/>
</template>
<script > 
import NavBar from "@/components/NavBar";
export default{
  name: 'App',
  components: {NavBar}

}
</script>


<style>

</style>
