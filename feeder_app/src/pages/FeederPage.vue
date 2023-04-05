<template>
  <q-page padding>
    <div class="row q-col-gutter-md ">

      <!-- container for all the content on the left -->
      <div class="col-6">

        <!-- container for the feeding history -->
        <q-card
          style="height: 600px; width: 500px"
          class="row items-center justify-evenly"
        >

          <!-- title for the feeding history -->
          <q-card-section>
            <h3 style="margin-top: 10%;" class="text-weight-medium">Feeding History</h3>

            <!-- scrollable list of feeding events with the dynamic history component -->
            <q-scroll-area style="height: 380px; width: 400px">

              <!-- component for the dynamic feeding history -->
              <feeding-feed :is-loading="isLoading" :events="events"/>
            </q-scroll-area>
          </q-card-section>
        </q-card>
      </div>

      <!-- container for all the content on the right -->
      <div class="col-6 flex-center">
        <div class = "flex-center row"
        style="background-color: #f0f7fa;
        border-radius: 4px;">

          <!-- image of the of your pet -->
          <q-img
            :src="imageUrl"
            style="border-radius: 4px; height: 400px;"
            class="shadow-1"></q-img>

          <!-- buttons to manually dispense food for each pet -->
          <div class="q-pa-md q-gutter-md ">
            <q-btn unelevated color="primary" @click="feedDog" label="Dispense for Dog" />
            <q-btn unelevated color="primary" @click="feedCat" label="Dispense for Cat" />
          </div>

          <!-- expansion block for the manual feeding settings -->
          <q-expansion-item
          icon="pets"
          label="Feeding Settings"
          header-class="text-primary"
          class = "full-width"
          color = "primary"
          expand-icon-class="text-primary"
          style="font-size: 16px; border-radius: 4px;"
          >

          <!-- manual feeding settings component -->
          <feeder-options
            :toggled="toggled"
            @feed-cat="feedCat"
            @feed-dog="feedDog"
          />
          </q-expansion-item>

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


// max number of times a user can feed their pet per day
const numInputs = 4;


// reactive array of booleans to keep track of the manual feeding settings
const toggled = reactive(Array.from({ length: numInputs }, () => false));

const route = useRoute();


// definitions of requests and responses for the feeder API
const cat = {
  request: "Left",
} as const;

const dog = {
  request: "Right",
} as const;

interface FeedSide {
  request: "Left" | "Right";
}


// zod schema for the feeder API response
const feedResponse = z.object({ request: z.string() });


// helper function to send a request to the feeder API to feed either the dog or cat
async function sendFeedRequest(data: { request: "Left" | "Right" }) {

  // send the request to the feeder API
  const response = await axios.post("http://localhost:5000/api/feed", data);

  console.log(response.data);

  const responseData = feedResponse.safeParse(response.data);

  // check if the response is valid
  if (!responseData.success) {
    console.error("Invalid response", response.data);
    return;
  }

  // push appropriate event to the feeding history based on the response
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
  }
  if (responseData.data.request === "dog-cat-success") {
    events.value.unshift({
      id: 3,
      title: "Fed Dog and Cat",
      date: new Date().toLocaleTimeString("en-US"),
    });
    return;
  } else {
    console.error("Invalid response", response.data);
    return;
  }
}

// manual feeding functions for the dog and cat
async function feedCat() {
  sendFeedRequest(cat);
}

async function feedDog() {
  sendFeedRequest(dog);
}


// helper function to get a unique image URL for the pet image
const getImageUrl = () => {
  const timestamp = new Date().getTime();
  return `/src/images/catdg.jpg?timestamp=${timestamp}`;
};

// reactive variable to store the pet image URL
const imageUrl = ref(getImageUrl());

// update the image URL every 30 seconds
const updateImageUrl = async () => {
  imageUrl.value = getImageUrl();
};

// update the image URL every 30 seconds
onMounted(async () => {
  setInterval(updateImageUrl, 30000);

  const eventsPromise = getEvents();
  isLoading.value = true;
  events.value = await eventsPromise;
  isLoading.value = false;
});


// function to receive the feeding history from the feeder API
const getEvents = () =>
  new Promise<FeedEvent[]>((resolve) =>
    setTimeout(() => resolve([] as FeedEvent[]), 500)
  );

// variables to store the feeding history and whether the history is loading
const events = ref([] as FeedEvent[]);
const isLoading = ref(false);
</script>

<style lang="scss">

</style>
