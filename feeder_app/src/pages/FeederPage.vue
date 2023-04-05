<template>
  <q-page padding>
    <div class="row q-col-gutter-md ">
      <div class="col-6">
        <q-card
          style="height: 600px; width: 500px"
          class="row items-center justify-evenly"
        >
          <q-card-section>
            <h3 style="margin-top: 10%;" class="text-weight-medium">Feeding History</h3>
            <q-scroll-area style="height: 380px; width: 400px">
              <feeding-feed :is-loading="isLoading" :events="events"/>
            </q-scroll-area>
          </q-card-section>
        </q-card>
      </div>
      <div class="col-6 flex-center">
        <div class = "flex-center row"
        style="background-color: #f0f7fa;
        border-radius: 4px;">
          <q-img
            :src="imageUrl"
            style="border-radius: 4px; height: 400px;"
            class="shadow-1"></q-img>
          <div class="q-pa-md q-gutter-md ">
            <q-btn unelevated color="primary" @click="feedDog" label="Dispense for Dog" />
            <q-btn unelevated color="primary" @click="feedCat" label="Dispense for Cat" />
          </div>
          <q-expansion-item
          icon="pets"
          label="Feeding Settings"
          header-class="text-primary"
          class = "full-width"
          color = "primary"
          expand-icon-class="text-primary"
          style="font-size: 16px; border-radius: 4px;"
          >
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

async function feedCat() {
  sendFeedRequest(cat);
}

async function feedDog() {
  sendFeedRequest(dog);
}

const getImageUrl = () => {
  const timestamp = new Date().getTime();
  return `/src/images/catdg.jpg?timestamp=${timestamp}`;
};

const imageUrl = ref(getImageUrl());

const updateImageUrl = async () => {
  imageUrl.value = getImageUrl();
};

onMounted(async () => {
  setInterval(updateImageUrl, 30000);

  const eventsPromise = getEvents();
  isLoading.value = true;
  events.value = await eventsPromise;
  isLoading.value = false;
});

const getEvents = () =>
  new Promise<FeedEvent[]>((resolve) =>
    setTimeout(() => resolve([] as FeedEvent[]), 500)
  );

const events = ref([] as FeedEvent[]);
const isLoading = ref(false);
</script>

<style lang="scss">

</style>
