<script setup lang="ts">
import { ref } from "vue";
import { computedAsync } from "@vueuse/core";
import axios from "axios";

interface FeedEvent {
  id: number;
  title: string;
  date: string;
}

const getEvents = () =>
  new Promise<FeedEvent[]>((resolve) =>
    setTimeout(
      () =>
        resolve([
          {
            id: 1,
            title: "Fed Fido",
            date: new Date().toLocaleTimeString('en-US'),
          },
        ] as FeedEvent[]),
      500
    )
  );

const isLoading = ref(false);

const events = computedAsync(getEvents, [], isLoading);

async function feed() {
  events.value.push({
    id: events.value[events.value.length - 1].id + 1,
    title: "Fed Fido",
    date: new Date().toLocaleTimeString('en-US'),
  });

  const response = await axios.post("/api/feed");
  events.value = [...events.value, ...response.data];


}
</script>

<template>
  <q-btn @click="feed">FEED</q-btn>
  <q-timeline>
    <q-timeline-entry heading> Feeding History </q-timeline-entry>
    <transition-group name="feed-entry">
    <q-timeline-entry
      v-for="event in events"
      :key="event.id"
      :title="event.title"
      :subtitle="event.date"
    />
    </transition-group>
    <q-inner-loading :showing="isLoading" />
  </q-timeline>
</template>

<style lang="scss">

.feed-entry {

  &-enter-active, &-leave-active {
    transition: transform 0.12s cubic-bezier(0,0,0.2,1), opacity 0.12s linear;
  }

  &-enter-from, &-leave-to {
    opacity: 0;
    transform: translateX(-10px);
  }

}

</style>
