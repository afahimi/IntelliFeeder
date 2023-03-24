<script setup lang="ts">
import { FeedEvent } from "components/models";

const props = defineProps<{
  events: FeedEvent[],
  isLoading: boolean
}>()

</script>

<template>
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
