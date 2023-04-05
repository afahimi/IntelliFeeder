<template>
  <q-layout view="lHh Lpr lFf">
    <q-header unelevated>

      <!-- Top Navbar and overall content layout template for each webpage-->
      <q-toolbar >
          <q-img src="~/assets/intellifeeder.svg" @click="redirectToLanding"
        style="width: 400px; margin-top: 1.75%; margin-bottom: 1.75%; margin-left: 1%;"
        to="/landing" class="logo"
        />

      </q-toolbar>
    </q-header>
    <q-page-container>
      <div class="q-mx-auto" style="max-width: 1280px">
        <router-view />
      </div>
    </q-page-container>
  </q-layout>
</template>

<script>
//axios.post('http://cpen291-16.ece.ubc.ca/')
export default {

  //routes to landing page when logo is clicked on any other page
  methods: {
    redirectToLanding() {
      this.$router.push('/landing')
    }
  }
}

</script>

<style lang="scss">

/*logo styling on hover*/
.logo:hover {
  cursor: pointer;
}
</style>
