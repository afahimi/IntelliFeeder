<template>
<q-page padding>
    <div class="row q-col-gutter-md">
      <div class="col-6">
        <q-card>
          <q-card-section>
            <feeding-feed />
          </q-card-section>
        </q-card>
      </div>
      <div class="col-6">
        <div>
          <q-video
            :ratio="16 / 9"
            src="https://www.youtube.com/embed/k3_tw44QsZQ?rel=0"
          />
        </div>
        <div >
          <q-toggle v-for="(_, i) in numInputs" v-model="toggled[i]" :key="i" keep-color/>
          <q-btn>Apply</q-btn>
        </div>
      </div>
    </div>
    <router-link :to="{ name: 'feeder', query: { id: 'foo' } }" />
    <router-link to="/foo?id=foo" />
  </q-page>
</template>

<script setup lang="ts">
import FeedingFeed from "components/FeedingFeed.vue";
import { reactive } from "vue";
import { useRoute } from "vue-router";

const numInputs = 4

const toggled = reactive(Array.from({ length: numInputs }, () => false ))

const route = useRoute();

</script>
