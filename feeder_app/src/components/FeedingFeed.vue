<script setup lang="ts">
import { FeedEvent } from "components/models";

// define an array of events passed as props to the component
const props = defineProps<{
  events: FeedEvent[],
  isLoading: boolean
}>()

</script>

<template>

  <!-- timeline component to display the events -->
  <q-timeline>
    <transition-group name="feed-entry">

    <!-- include each feeding entry as a typescript model to dynamically add more on feed-->
    <q-timeline-entry
      v-for="event in events"
      :key="event.id"
      :title="event.title"
      :subtitle="event.date"
    />

    <!-- loading animation -->
    </transition-group>
    <q-inner-loading :showing="isLoading" />
  </q-timeline>
</template>

<style lang="scss">

/* animation for the timeline entry pop-in */
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
