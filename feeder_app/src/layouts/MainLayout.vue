<template>
  <q-layout view="lHh Lpr lFf">
    <q-header unelevated no-shadow>
      <q-toolbar no-shadow>
        <q-btn
          flat
          dense
          round
          color="black"
          icon="visibility"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>Feeder</q-toolbar-title>
        <div class="q-pa-md q-gutter-md">
          <q-btn unelevated style="color: #ff0080" label="About" />
          <q-btn
            unelevated
            rounded
            color="primary"
            label="Buy"
            @click="httpreq"
          />
          <q-btn unelevated style="color: #ff0080" label="Login" />
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item-label header> Essential Links </q-item-label>

        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from "vue";
import EssentialLink from "components/EssentialLink.vue";

const linksList = [
  {
    title: "Docs",
    caption: "quasar.dev",
    icon: "school",
    link: "https://quasar.dev",
  },
  {
    title: "Github",
    caption: "github.com/quasarframework",
    icon: "code",
    link: "https://github.com/quasarframework",
  },
];

export default defineComponent({
  name: "MainLayout",

  components: {
    EssentialLink,
  },

  setup() {
    const leftDrawerOpen = ref(false);

    const httpreq = async () => {
      try {
        console.log("sending http request");
        const response = await fetch("http://cpen291-16.ece.ubc.ca");
        const data = await response.json();
        console.log(data);
      } catch (error) {
        console.error(error);
      }
    };

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
      httpreq,
    };
  },
});
</script>

<style lang="scss">
.q-header {
  background-color: white;
  color: black;
  padding: 1.5%;
}
</style>
