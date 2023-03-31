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
          <q-img
            :src="imageUrl"
            style="border-radius: 8px"
            class="shadow-1"
          ></q-img>
          <q-btn @click="feedCat">Cat</q-btn>
          <q-btn @click="feedDog">Dog</q-btn>
          <feeder-options
            :toggled="toggled"
            @feed-cat="feedCat"
            @feed-dog="feedDog"
          />
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
  setInterval(updateImageUrl, 5000);

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
