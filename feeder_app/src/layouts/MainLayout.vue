<template>
  <q-layout view="lHh Lpr lFf">
    <q-header unelevated>
      <q-toolbar>
        <q-img src="~/assets/intellifeeder.svg"
        style="width: 400px; margin-top: 1.75%; margin-bottom: 1.75%; margin-left: 1%;"
        to="/landing"
        />
      </q-toolbar>
    </q-header>
    <q-page-container>
      <div class="q-mx-auto" style="max-width: 1280px" >
        <router-view />
      </div>
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios'


//axios.post('http://cpen291-16.ece.ubc.ca/')


</script>

<style lang="scss">

</style>
