<template>
  <q-page padding>
    <div class="row q-col-gutter-md">
      <div class="col-6">
        <q-card
          style="height: 555px; width: 500px"
          class="row items-center justify-evenly"
        >
          <q-card-section>
            <q-scroll-area style="height: 500px; width: 400px">
              <feeding-feed :is-loading="isLoading" :events="events" />
            </q-scroll-area>
          </q-card-section>
        </q-card>
      </div>
      <div class="col-6">
        <div>
          <q-img style="border-radius: 8px;" src="https://cdn.quasar.dev/img/parallax2.jpg" class="shadow-1"></q-img>
          <!--<q-video
            :ratio="16 / 9"
             src="https://www.youtube.com/embed/k3_tw44QsZQ?rel=0"
          />-->
        </div>
        <div>
          <q-toggle
            v-for="(_, i) in numInputs"
            v-model="toggled[i]"
            :key="i"
            keep-color
          />
          <q-btn>Apply</q-btn>
          <q-btn @click="feedCat">Cat</q-btn>
          <q-btn @click="feedDog">Dog</q-btn>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import FeedingFeed from "components/FeedingFeed.vue";
import FeederOptions from "components/FeederOptions.vue";
import { onMounted, reactive } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";
import { computedAsync, useAsyncState } from "@vueuse/core";
import { ref } from "vue";
import { z } from "zod";
import { FeedEvent } from "components/models";

const numInputs = 4;

const toggled = reactive(Array.from({ length: numInputs }, () => false));

const route = useRoute();

const cat = {
  request: "Left",
} as const;

const dog = {
  request: "Right",
} as const;

interface FeedSide {
  request: "Left" | "Right";
}

const feedResponse = z.object({ request: z.string() });

async function sendFeedRequest(data: { request: "Left" | "Right" }) {
  const response = await axios.post("http://localhost:5000/api/feed", data);

  console.log(response.data);

  const responseData = feedResponse.safeParse(response.data);

  if (!responseData.success) {
    console.error("Invalid response", response.data);
    return;
  }

  // app.post('/feed/:id', (req, res) => {
  //   const body = feedRequestBody.safeParse(req.body);
  //   if(!body.success)
  //     return res.sendStatus(400);

  //   const id = req.params.id;

  //   const pet = await db.pets.findById(id);

  //   if(!pet)
  //     return res.sendStatus(404);

  //   // feed pet logic

  //   const entry = await db.insert({
  //     petId: id,
  //     title: 'Fed ' + pet.name,
  //     date: new Date()
  //   })

  //   return res.json(entry);
  // })

  if (responseData.data.request === "dog-success") {
    events.value.unshift({
      id: 1,
      title: "Fed Dog",
      date: new Date().toLocaleTimeString("en-US"),
    });
    return;
  }
  if (responseData.data.request === "cat-success") {
    events.value.unshift({
      id: 2,
      title: "Fed Cat",
      date: new Date().toLocaleTimeString("en-US"),
    });
    return;
  } else {
    console.error("Invalid response", response.data);
    return;
  }
}

async function feedCat() {
  sendFeedRequest(cat);
}

async function feedDog() {
  sendFeedRequest(dog);
}

const getEvents = () =>
  new Promise<FeedEvent[]>((resolve) =>
    setTimeout(() => resolve([] as FeedEvent[]), 500)
  );

const events = ref([] as FeedEvent[]);
const isLoading = ref(false);
onMounted(async () => {
  isLoading.value = true;
  events.value = await getEvents();
  isLoading.value = false;
});
</script>
