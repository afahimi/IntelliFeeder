<template>
<q-page padding>
    <div class="row q-col-gutter-md">
      <div class="col-6">
        <q-card style="height: 555px; width: 500px;" class="row items-center justify-evenly">
          <q-card-section>
          <q-scroll-area style="height: 500px; width: 400px;">
            <feeding-feed />
          </q-scroll-area>
        </q-card-section>
        </q-card>
      </div>
      <div class="col-6">
        <div>
          <q-img src="https://cdn.quasar.dev/img/parallax2.jpg"></q-img>
          <!--<q-video
            :ratio="16 / 9"
             src="https://www.youtube.com/embed/k3_tw44QsZQ?rel=0"
          />-->
        </div>
        <div >
          <q-toggle v-for="(_, i) in numInputs" v-model="toggled[i]" :key="i" keep-color/>
          <q-btn @click="sendRequest">Apply</q-btn>
          <q-btn @click="sendCatRequest">Cat</q-btn>
          <q-btn @click="sendDogRequest">Dog</q-btn>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import FeedingFeed from "components/FeedingFeed.vue";
import { reactive } from "vue";
import { useRoute } from "vue-router";

const numInputs = 4

const toggled = reactive(Array.from({ length: numInputs }, () => false ))

const route = useRoute();

const cat = {
  request: "Left"
};

const dog = {
  request: "Right"
};


async function sendRequest() {
  const response = await fetch('http://localhost:5000/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(toggled)
  });
  const data = await response.json();
  console.log(data);
}

async function sendCatRequest() {
  const response = await fetch('http://localhost:5000/api/v1/users/create', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(cat)
  });
  const data = await response.json();
  console.log(data);
}

async function sendDogRequest() {
  const response = await fetch('http://localhost:5000/api/v1/users/create', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(dog)
  });
  const data = await response.json();
  console.log(data);
}

</script>
