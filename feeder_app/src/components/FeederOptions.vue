<template>
<div class="q-pa-md">
    <div style="max-width: 600px">
      <q-tabs v-model="tab" align="justify" narrow-indicator class="q-mb-lg">
        <q-tab class="text-purple" name="Dog" label="Dog" />
        <q-tab class="text-orange" name="Cat" label="Cat" />
      </q-tabs>

      <div class="q-gutter-y-sm">
        <q-tab-panels
          v-model="tab"
          animated
          transition-prev="scale"
          transition-next="scale"
          class="bg-white text-primary text-center"
        >
          <q-tab-panel name="Dog">
            <div class="text-h6">Dog</div>
            <div class="q-pa-lg">
              <label class="text-h6">Number of servings per day</label>
              <q-slider
                v-model="dogNumServings"
                color="primary"
                thumb-color="primary"
                markers
                marker-labels
                marker-labels-class="text-black"
                switch-marker-labels-side
                switch-label-side
                :min="1"
                :max="4"
              />
            </div>
            <div class="q-pa-md">
    <q-row>
      <q-col v-for="i in dogNumServings" :key="i">
        <q-input
          filled
          v-model="dogTimes[i - 1]"
          mask="time"
          :rules="['time']"
        >
          <template v-slot:append>
            <q-icon name="access_time" class="cursor-pointer">
              <q-popup-proxy
                cover
                transition-show="scale"
                transition-hide="scale"
              >
                <q-time v-model="dogTimes[i - 1]" :hour="12" :minute="0">
                  <div class="row items-center justify-end">
                    <q-btn
                      v-close-popup
                      label="Close"
                      color="primary"
                      flat
                    />
                  </div>
                </q-time>
              </q-popup-proxy>
            </q-icon>
          </template>
        </q-input>
      </q-col>
    </q-row>
  </div>
            <label style="padding-left: 5%" class="text-h6"
              >Portion Sizes</label
            >
            <div class="q-pa-md">
              <q-btn-toggle
                v-model="dogPortionSize"
                toggle-color="primary"
                :options="[
                  { label: 'Small', value: 'one' },
                  { label: 'Medium', value: 'two' },
                  { label: 'Large', value: 'three' },
                ]"
                @click.native="toggleDogStyle"
                :class="{ toggled: dogToggled }"
              />
            </div>
          </q-tab-panel>

          <q-tab-panel name="Cat">
            <div class="text-h6">Cat</div>
            <div class="q-pa-lg">
              <label class="text-h6">Number of servings per day</label>
              <q-slider
                v-model="catNumServings"
                color="primary"
                thumb-color="primary"
                markers
                marker-labels
                marker-labels-class="text-black"
                switch-marker-labels-side
                switch-label-side
                :min="1"
                :max="4"
              />
            </div>

            <div class="q-pa-md">
                <q-row>
      <q-col v-for="i in catNumServings" :key="i" cols="12">
        <q-input
          filled
          v-model="catTimes[i - 1]"
          mask="time"
          :rules="['time']"
        >
          <template v-slot:append>
            <q-icon name="access_time" class="cursor-pointer">
              <q-popup-proxy
                cover
                transition-show="scale"
                transition-hide="scale"
              >
                <q-time v-model="catTimes[i - 1]" :hour="12" :minute="0">
                  <div class="row items-center justify-end">
                    <q-btn
                      v-close-popup
                      label="Close"
                      color="primary"
                      flat
                    />
                  </div>
                </q-time>
              </q-popup-proxy>
            </q-icon>
          </template>
        </q-input>
      </q-col>
    </q-row>
  </div>
            <label style="padding-left: 5%" class="text-h6"
              >Portion Sizes</label
            >
            <div class="q-pa-md">
              <q-btn-toggle
                v-model="catPortionSize"
                toggle-color="primary"
                :options="[
                  { label: 'Small', value: 'one' },
                  { label: 'Medium', value: 'two' },
                  { label: 'Large', value: 'three' },
                ]"
                @click.native="toggleCatStyle"
                :class="{ toggled: catToggled }"
              />
            </div>
          </q-tab-panel>
        </q-tab-panels>
      </div>
    </div>
  </div>

  <!-- <div class="q-pa-lg">
      <label class="text-h6">Number of servings per day</label>
      <q-slider
        v-model="numServings"
        color="primary"
        thumb-color="primary"
        markers
        marker-labels
        marker-labels-class="text-black"
        switch-marker-labels-side
        switch-label-side
        :min="1"
        :max="4"
      />
    </div>
    
    <div class="q-pa-md">
      <div v-for="i in numServings" :key="i" class="q-gutter-sm row">
        <q-input filled v-model="times[i-1]" mask="time" :rules="['time']">
          <template v-slot:append>
            <q-icon name="access_time" class="cursor-pointer">
              <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                <q-time v-model="times[i-1]" :hour="12" :minute="0">
                  <div class="row items-center justify-end">
                    <q-btn v-close-popup label="Close" color="primary" flat />
                  </div>
                </q-time>
              </q-popup-proxy>
            </q-icon>
          </template>
        </q-input>
      </div>
    </div>
    <label style="padding-left: 5%;" class="text-h6">Portion Sizes</label>
    <div class="q-pa-md">
      <q-btn-toggle
        v-model="portionSize"
        toggle-color="primary"
        :options="[
          {label: 'Small', value: 'one'},
          {label: 'Medium', value: 'two'},
          {label: 'Large', value: 'three'}
        ]"
        @click.native="toggleStyle"
        :class="{ 'toggled': toggled }"
      />
    </div> -->
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    return {
      tab: ref("Dog"),
    };
  },
  data() {
    return {
      tab: 'Dog',
      dogNumServings: 1,
      dogTimes: ['0000', '0000', '0000','0000'],
      dogPortionSize: 'one',
      dogToggled: false,
      catNumServings: 1,
      catTimes: ['0000', '0000', '0000','0000'],
      catPortionSize: 'one',
      catToggled: false,
    }
  },
  methods: {
    toggleDogStyle() {
      this.dogToggled = !this.dogToggled
    },
    toggleCatStyle() {
      this.catToggled = !this.catToggled
    },
  },

};
</script>
